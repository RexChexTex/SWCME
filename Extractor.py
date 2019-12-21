##Script will import the required modules and templates

from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

## Script will ask for an html page of the collection (hardcoded for now, will prompt for user input soon)
## takes the webpage and stores it as a variable 'source', then runs the html scrape through BS to product the xml
## For now, I'll output the XML as a test.

source = requests.get('https://pythonprogramming.net/parsememcparseface/').text
soup = BeautifulSoup(source, 'lxml')
print(soup)
## Script will download a local copy of the html document and locally scan it for mod ID's

## Script will record the mod ID's into a timestamped or named .csv file
 
## Script will output a total of discovered mods, and inform the user when the process is complete

## Script will output the stored location of the output file.



#below is a chunk of code sent to me by a friend that was used to parse through an html document for the values I needed.


#file_path = html.html
#csv_values = ",".join(list_of_found_items)

#with open(file_path, "r") as html_file:
#    html_text = html_file.readall()
#list_of_found_items = re.findall(r"[0-9]{9}(?=</PublishedFileId>)", html_text)
#
#    with open(file_path, "r") as html_file:
#    for line in html_file:
#        if "PublishedFileId" in line:
#            # parse number from single line