# -----------------------------------------------------------------
# Scrape geolocation data from sqlite binaries - nonfunctional as of 5/26/23
# Written by: Joe Dinsmoor
# github: @joedinsmoor
# -----------------------------------------------------------------


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
    - uses geopy library with Nominatim to determine locations using given coordinates and plots on a map using tkinter library
    - Links to timestamp log so that if a location is clicked, a timestamp pops up with information on the event
    '''
    #coords = "x, y"
    #location = geo.reverse(coords)
    #address = location.raw['address']
