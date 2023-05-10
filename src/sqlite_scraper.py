import os
import sqlite3
import string
from importer import input_file
from image_handler import handle_photo
from decoder import decode

#Import extracted SQLite db
filename = input_file()
conn = sqlite3.connect(filename)
cur = conn.cursor()

#Navigate to appropriate table and row
res = cur.execute("SELECT name FROM sqlite_master WHERE name='object_data'")
res.fetchall()

#Set character validity for decoding
valid_chars = string.printable

#Decode and remove extraneous hex data, leaving only ascii characters
decode(cur)

#images = handle_photo(cur)
