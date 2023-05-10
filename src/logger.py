def scraper_log(str):
    file = open("run.log", "w")
    file.write("\n")
    file.write(str)
    file.close()

def phone_numbers(str):
    file = open("phone_numbers.log", "w")
    file.write("\n")
    file.write(str)
    file.close()
