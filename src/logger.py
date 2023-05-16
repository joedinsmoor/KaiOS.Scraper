# -----------------------------------------------------------------
# Logging for different datatypes scraped from sqlite db binaries
# Written by: Joe Dinsmoor
# github: @joedinsmoor
# -----------------------------------------------------------------


import csv


def scraper_log(str, error=0, flag=0):
    if not flag:
        file = open("run.log", "w")
        file.write("\n")
        file.write(str)
        file.close()
    else:
        file = open("error.log", "w")
        file.write(str)
        file.write(error)
        file.close()

def phone_numbers(str):
        pfile = open("phone_numbers.csv", "w")
        writer = csv.writer(pfile)
        writer.writerow([str])
        pfile.close()

def timestamper_log(str):
    file = open("timestamps.log", "w")
    file.write(str)
    file.write("\n")
    file.close()
