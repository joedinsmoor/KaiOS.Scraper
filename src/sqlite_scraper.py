import os
import sqlite3
import string
from importer import input_file
from image_handler import handle_photo
from decoder import decode

#Import extracted SQLite db
filename = input_file()
if filename == "":
    print("No file entered.")
    filename = input_file()

tablename = input("Enter name of table to parse:")

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

    #Decode and remove extraneous hex data, leaving only ascii characters
    decode(cur)

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)

finally:
    if conn:
        conn.close()
        print("SQLite Connection Closed. ")



    

#images = handle_photo(cur)



