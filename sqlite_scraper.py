import os
import sqlite3
import string
import sys
import glob
from time import sleep
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
from src.ks_gui import *



fileList = []
n = 0

menu = load_gui()

if (menu == '1'):
    #Import extracted SQLite db
    filename = main_gui('1')
    while filename == "":
        print("No file entered.\nPress ctrl+c to exit.")
        filename = main_gui(1)

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
        sleep(0.1)
        #Decode and remove extraneous hex data, leaving only ascii characters
        decode(cur)
        sleep(0.1)
        time_scrape(cur)
        sleep(0.1)
        

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table: Error:", error)
        error_text = "Failed to read data from sqlite table: Error:".format(str(error)) 
        log_error = 1
        flag = True
        scraper_log(error_text, log_error, flag)

    finally:
        if conn:
            conn.close()
            print("\nSQLite Connection Closed. \n\nLog saved in 'run.log'")
            if exists("phone_numbers.csv"):
                    print("Phone Numbers Found! Output in 'phone_numbers.csv'\n")
            if exists("timestamps.log"):
                    print("Timestamps Gathered! Timestamps in 'timestamps.log'\n")

elif (menu == '2'):
    #import all filenames to list, parse all dbs in parallel using Threading

    dirflag = 1

    dir = main_gui('2')
    tablename = input("Enter name of table to parse (defaults to 'object_data if nothing is entered): ")
    os.chdir(dir)
    dir_list = os.listdir(dir)
    print(dir_list)
    n = len(dir_list)
    for i in range(n):
        if(dir_list[i].endswith(".sqlite")):
            if(dir_list[i].endswith(".sqlite-wal")):
                 pass
            elif(dir_list[i].endswith(".sqlite-shm")):
                 pass
            else:
                sleep(0.5)
                dirScraper(dir_list[i], dirflag, tablename)
                os.chdir(dir)
        else:
            i+=1
else:
    print("------------menu option invalid------------\n")
    exit()






