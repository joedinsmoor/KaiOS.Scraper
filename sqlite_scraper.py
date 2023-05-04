import os
import sqlite3
import time
import string

filename = input("enter path to sqlite db: ")

f = open(filename, "r")

conn = sqlite3.connect(filename)
cur = conn.cursor()


res = cur.execute("SELECT name FROM sqlite_master WHERE name='object_data'")
res.fetchall()
print(res)

