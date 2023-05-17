# -----------------------------------------------------------------
# Deciper the name of SQLite database stored on KaiOS 
# -----------------------------------------------------------------
import re
from string import digits

def valid_input(text: str) -> bool:
    " Check given string contains a '.' (filename indicator) and is alphanumeric"
    valid = False
    if text.__contains__('.'):
        valid = True
    elif not text.isalnum():
        valid = False
    return valid 

def extract(text) -> str:
    " Extract main encoded name (without numbers or file extension) & print "
    text = re.split('\.', text)[0]
    text = text.lstrip(digits)
    print("Extracted name: " + text) 
    return text

def unscramble(text: str) -> str:
    " Given a .sqlite filename string, decode the original name "
    newText = ""
    text = extract(text) # Get base name 
    n = len(text)
    if n % 2 == 0: 
        # Length of string is even
        text = text[::2] + text[::-2]
        newText = text
    elif n % 2 == 1:
        # Length of string is odd
        newText = text[::2]
        c = n
        while (c > 1 and len(newText) <= n):
            newText = newText + text[(c-2)]
            c = c - 2

    # Replace unprintable characters found in result ("%2F" -> "/")
    while (newText.__contains__("%2F")):
        newText = newText.replace("%2F", "/")

    print("\nDecoded result:\n\t" + newText)
    return newText 

if __name__ == '__main__':
    text = ""
    while (not valid_input(text)):
        text = input("Enter VALID encoded KaiOS SQLite DB filename (e.g. '226660312ssm.sqlite'): ")
    unscramble(text)