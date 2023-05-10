def scraper_log(str):
    file = open("run.log", "w")
    file.write("\n")
    file.write(str)
    file.close()
