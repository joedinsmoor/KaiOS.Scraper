import os
import sqlite3
import time
import string
import re


#Import extracted SQLite db
filename = input("enter path to sqlite db: ")

f = open(filename, "r")

conn = sqlite3.connect(filename)
cur = conn.cursor()

#Navigate to appropriate table and row
res = cur.execute("SELECT name FROM sqlite_master WHERE name='object_data'")
res.fetchall()
print(res)

#Set character validity for decoding
valid_chars = string.printable

#Decode and remove extraneous hex data, leaving only ascii characters
for row in cur.execute("SELECT data FROM object_data"):
    row_str = str(row)
    row_str_decoded = bytes(row_str, "utf-8").decode("unicode_escape")
    row_decoded = re.sub('r\\\\x[0-9a-fA-F]{2}', "", row_str_decoded)
    print(row_decoded)
