# -----------------------------------------------------------------
# Scrape image metadata from sqlite db binaries -- Under Development
# Written by: Joe Dinsmoor
# github: @joedinsmoor
# -----------------------------------------------------------------


from PIL import Image
import io
import sqlite3


def handle_photo(cur):
    #Carve any images that exist in SQLite db - nonfunctional as of 5/11
    cur.execute("SELECT data FROM object_data")
    res = cur.fetchone()
    image_data = res[0]
    start_index = image_data.find(b'\xFF\xD8')
    end_index = image_data.find(b'\xFF\xD9')
    end = image_data.find(end_index, start_index) + len(end_index)
    image_binary += image_data[start_index:end]
    if image_binary != '':
        with open(f'extracted-img.jpg', 'wb') as f:
            f.write(image_binary)
    