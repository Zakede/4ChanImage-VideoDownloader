#FINAL FOR SURE
import requests
import wget
import re
import os,sys,time

#Lists
items = []

#Pattern
pattern = r'''[a-z0-9]+.[a-z0-9]+.org/[a-z0-9]+/[0-9]+[.][a-z]+'''

#Main Code
x = input("Write The Link You'd Like To Scrape and Download From 4Chan:")
url = requests.get(x)
res = url.text
items = re.findall(pattern, res)

#Downloading Part of the code
print("Found " + str(len(list(dict.fromkeys(items)))) + " Items Incl. Webm and Images.")


for char in "Downloading Now!":
    print(char, end='')
    sys.stdout.flush()
    time.sleep(.001)

for i in list(dict.fromkeys(items)):
    wget.download(("https://"+ i), os.getcwd())

print("All Files Have Been Downloaded.")
time.sleep(5)