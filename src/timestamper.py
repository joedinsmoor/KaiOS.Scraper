import datetime
import os
import re
import sqlite3
from logger import *


def time_scrape(cur):
    ''' 
    Scrape timestamps from any calls, texts, emails, or any other communications. Potentially scrape metadata from images as well. 
    Eventually, set up timeline within a time.log file of exact nature of phone use. Potentially tied to geolocation as well. 
    '''
    for row in cur.execute("SELECT data from object_data"):
        row_str = str(row)
        row_str_decoded = bytes(row_str, "utf-8").decode("unicode_escape")
        if "Timestamp=" in row_str_decoded:
            timestamper_log(row_str_decoded)
        



