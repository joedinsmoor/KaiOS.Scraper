# -----------------------------------------------------------------
# Logging for different datatypes scraped from sqlite db binaries
# Written by: Joe Dinsmoor
# github: @joedinsmoor
# -----------------------------------------------------------------


import csv
import os


def scraper_log(str, error_text="", flag=False, dirflag = 0, dirname =""):
    if not flag:
        if dirflag:
             os.chdir(dirname)
             file = open('run.log', "w")
             file.write(str + '\n')
             file.close()
        else:
            file = open("run.log", "w")
            file.write(str + '\n')
            file.close()
    else:
        if dirflag:
            os.chdir(dirname)
            file = open("error.log", "w")
            file.write(str)
            #file.write(error_text)
            file.close()
        else:
            file = open("error.log", "w")
            file.write(str)
            #file.write(error_text)
            file.close()

def phone_numbers(str,  dirname, dirflag = 0):
        if dirflag:
            os.chdir(dirname)
            filename = "phone_numbers.csv"
            pfile = open(filename, "w")
            writer = csv.writer(pfile)
            writer.writerow([str])
            pfile.close()
        else: 
            pfile = open("phone_numbers.csv", "w")
            writer = csv.writer(pfile)
            writer.writerow([str])
            pfile.close()

def timestamper_log(str, dirflag = 0):
    if dirflag:
        file = open("timestamps.log", "w")
        file.write(str)
        file.write("\n")
        file.close()
    else:
        file = open("timestamps.log", "w")
        file.write(str)
        file.write("\n")
        file.close()
