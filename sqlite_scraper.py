import os
import sqlite3
import string
import sys
import glob
#import pandas
#from jinja2 import Environment
from os.path import exists
from pathlib import Path
sys.path.append('./src')
from src.unscrambleDB import unscramble
from src.importer import *
from src.image_handler import handle_photo
from src.decoder import decode
from src.logger import scraper_log
from src.timestamper import time_scrape
from src.dirScrape import *


menu = input("Enter 1 to scrape a single db, Enter 2 to scrape a full directory of sqlite dbs: ")

fileList = []
n = 0

if (menu == '1'):
    #Import extracted SQLite db
    filename = input_file()
    while filename == "":
        print("No file entered.\nPress ctrl+c to exit.")
        filename = input_file()

    tablename = input("Enter name of table to parse (defaults to 'object_data if nothing is entered): ")


    p = Path(filename)

    unscrambled = unscramble(p.name)

    conn = open_sqlite_db_readonly(filename)
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
        image = handle_photo(cur)
        #Decode and remove extraneous hex data, leaving only ascii characters
        decode(cur)
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

elif (menu == '2'):
    #import all filenames to list, parse all dbs in parallel using Threading

    dirflag = 1

    dir = input("enter directory to scrape: ")
    tablename = input("Enter name of table to parse (defaults to 'object_data if nothing is entered): ")
    os.chdir(dir)
    dir_list = os.listdir(dir)
    print(dir_list)
    n = len(dir_list)
    for i in range(n):
        if(dir_list[i].endswith(".sqlite")):
            dirScraper(dir_list[i], dirflag, tablename)
            os.chdir(dir)
        else:
            i+=1

    

else:
    print("------------menu option invalid------------\n")
    exit()






