# -----------------------------------------------------------------
# Scrape image metadata from sqlite db binaries -- Under Development
# Written by: Joe Dinsmoor
# github: @joedinsmoor
# -----------------------------------------------------------------


#from PIL import Image
import io
import sqlite3


def handle_photo(cur, dirflag = 0, dirname = ""):
    #Carve any images that exist in SQLite db - nonfunctional as of 5/11
    cur.execute("SELECT data FROM object_data")
    res = cur.fetchall()
    jpg_byte_start = b'\xff\xd8'
    jpg_byte_end = b'\xff\xd9'
    image_binary = bytearray()

    start = jpg_byte_start in res
    if start == '-1':
        print("Could not find .jpg file within Sqlite db")
        return
    end = jpg_byte_end in res

    image_binary.extend(res[start:end])
    print(f"Size: {end - start} bytes")

    with open(f'extracted_image.jpg', 'wb') as f:
        f.write(image_binary)
    return f
    
    