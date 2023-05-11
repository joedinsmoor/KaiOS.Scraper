import datetime
import time
import os
import requests
import re
from geopy.geocoders import Nominatim
from tkinter import *

win = Tk()
win.geometry("1280x720")


geo = Nominatim(user_agent="sqlite_scraper")


def geolocation(str):
    '''
    - Takes in string and searches for coordinates in latitude and longitude
    - sends to google earth API to create a heatmap or web to show locations at which certain events transpired
    - Links to timestamp log so that if a location is clicked, a timestamp pops up with information on the event
    '''