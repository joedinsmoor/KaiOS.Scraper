# -----------------------------------------------------------------
# Logging for different datatypes scraped from sqlite db binaries
# Written by: Joe Dinsmoor
# github: @joedinsmoor
# -----------------------------------------------------------------


import csv
import os
import logging


def scraper_log(str, unscrambled, error_text="", flag=False, dirflag = 0):
    logging.basicConfig(level=logging.DEBUG, filename='run.log', format='%(asctime)s %(levelname)s:%(message)s')
    if not flag:
        if dirflag:
            os.chdir(unscrambled)
            logging.debug(str + '\n')
            #file.close()
        else:
            logging.debug(str + '\n')
            #file.close()
    else:
        if dirflag:
            os.chdir(unscrambled)
            file = open("error.log", "w")
            file.write(str)
            #file.write(error_text)
            file.close()
        else:
            file = open("error.log", "w")
            file.write(str)
            #file.write(error_text)
            file.close()

def phone_numbers(str, unscrambled, dirflag = 0):
        if dirflag:
            if not os.path.isdir(unscrambled):
                result = ''.join(i for i in unscrambled if not i.isdigit())
                os.makedirs(result)
            os.chdir(unscrambled)
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

def timestamper_log(str, unscrambled, dirflag = 0):
    if dirflag:
        os.chdir(unscrambled)
        logging.debug(str + '\n')
        #file.close()
    else:
        file = open("timestamps.log", "w")
        file.write(str)
        file.write("\n")
        file.close()
