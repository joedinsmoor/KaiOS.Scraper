# -----------------------------------------------------------------
# Scrape image metadata from sqlite db binaries
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
    start_index = image_data.find(b'GIF89a')
    # end_index = image_data.find(b'\xff\xd9')
    image_binary = image_data[start_index:]

    image_stream = io.BytesIO(image_binary)
    image = Image.open(image_stream)

    image.show()