# -----------------------------------------------------------------
# Scrapes full directories of SQLite dbs
# Written by: Joe Dinsmoor
# github: @joedinsmoor
# -----------------------------------------------------------------
import sqlite3
import os
import string
import sys
from pathlib import Path
from os.path import exists
sys.path.append('./src')
from src.unscrambleDB import unscramble
from src.image_handler import handle_photo
from src.decoder import decode
from src.logger import scraper_log
from src.timestamper import time_scrape
from src.image_handler import handle_photo



def dirScraper(filename, dirflag):
    #Scrapes full directory of SQLite dbs
    tablename = input("Enter name of table to parse (defaults to 'object_data if nothing is entered): ")

    dirflag = 1
    p = Path(filename)
    unscrambled = unscramble(p.name)
    os.makedirs(unscrambled) #Create directory for current sqlite DB


    conn = sqlite3.connect(filename)
    cur = conn.cursor()
    #Navigate to appropriate table and row
    try:
        if tablename == "":
            res = cur.execute("SELECT name FROM sqlite_master WHERE name='object_data'")
            res.fetchall()

        else:
            res = cur.execute("SELECT name FROM sqlite_master WHERE name=tablename")

        #Set character validity for decoding
        valid_chars = string.printable
        f = handle_photo(cur, dirflag)
        #Decode and remove extraneous hex data, leaving only ascii characters
        decode(cur, dirflag, unscrambled)
        time_scrape(cur)

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table: Error:", error)
        error_text = "Failed to read data from sqlite table: Error:".format(str(error)) 
        log_error = 1
        scraper_log(error_text, log_error)

    finally:
        if conn:
            conn.close()
            print("\nSQLite Connection Closed. \nLog saved in 'run.log'\n")
            if exists("phone_numbers.csv"):
                    print("Phone Numbers Found! Output in 'phone_numbers.csv'")
            if exists("timestamps.log"):
                    print("Timestamps Gathered! Timestamps in 'timestamps.log'")

