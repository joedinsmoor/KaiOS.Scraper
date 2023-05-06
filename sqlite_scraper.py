import os
import sqlite3
import time
import string
import re
from PIL import Image
import io


#Import extracted SQLite db
filename = input("enter path to sqlite db: ")

f = open(filename, "r")

conn = sqlite3.connect(filename)
cur = conn.cursor()

#Navigate to appropriate table and row
res = cur.execute("SELECT name FROM sqlite_master WHERE name='object_data'")
res.fetchall()

#Set character validity for decoding
valid_chars = string.printable

#Decode and remove extraneous hex data, leaving only ascii characters
for row in cur.execute("SELECT data FROM object_data"):
    row_str = str(row)
    row_str_decoded = bytes(row_str, "utf-8").decode("unicode_escape")
    row_decoded = re.sub('r\\\\x[0-9a-fA-F]{2}', "", row_str_decoded)
    print_me = row_decoded.encode('ascii', 'ignore').decode('ascii')
    print(print_me)


#Carve any images that exist in SQLite db - nonfunctional as of 5/6
cur.execute("SELECT data FROM object_data")
res = cur.fetchone()
image_data = res[0]
start_index = image_data.find(b'GIF89a')
# end_index = image_data.find(b'\xff\xd9')
image_binary = image_data[start_index:]

image_stream = io.BytesIO(image_binary)
image = Image.open(image_stream)

image.show()