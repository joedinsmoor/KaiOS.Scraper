import datetime
import time
import os
import re
import sqlite3
from logger import *


def time_scrape(cur):
    ''' 
    - Ingest data row by row - done
    - Do normal conversion through decoder module
    - Once extraneous data is removed, search for the the substring “Timestamp=“
    - Capture 8 bytes after that, and translate to proper date and time conventions
    - Save to timestamps.log using logger module
    - Eventually tie to additional module relating to geolocation with timestamps
    - Geolocation will be difficult, KaiOS phone did not have GPS capabilities enabled for some reason
    '''

    for row in cur.execute("SELECT data from object_data"):
        row_str = str(row)
        row_str_decoded = bytes(row_str, "utf-8").decode("unicode_escape")
        if "Timestamp=" in row_str_decoded:
            timestamper_log(row_str_decoded)
            #Change format to human readable D/M/Y format, rather than Hexadecimal, time in HH:MM:SS format




