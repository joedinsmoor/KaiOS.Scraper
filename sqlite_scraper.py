import os
import sqlite3
import time
import string


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
    row_decoded = ''.join(i for i in row_str if i in valid_chars)
    print(row_decoded)
