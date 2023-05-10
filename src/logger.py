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
    file = open("phone_numbers.log", "w")
    file.write("\n")
    file.write(str)
    file.close()
