import os
import sqlite3

def input_file():
    filename = input("enter path to sqlite db: ")
    return filename

def open_sqlite_db_readonly(path):
    '''Opens an sqlite db in read-only mode, so original db (and -wal/journal are intact)'''
    if is_platform_windows():
        if path.startswith('\\\\?\\UNC\\'):  # UNC long path
            path = "%5C%5C%3F%5C" + path[4:]
        elif path.startswith('\\\\?\\'):  # normal long path
            path = "%5C%5C%3F%5C" + path[4:]
        elif path.startswith('\\\\'):  # UNC path
            path = "%5C%5C%3F%5C\\UNC" + path[1:]
        else:  # normal path
            path = "%5C%5C%3F%5C" + path
    return sqlite3.connect(f"file:{path}?mode=ro", uri=True)

def is_platform_windows():
    '''Returns True if running on Windows'''
    return os.name == 'nt'
