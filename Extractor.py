import re

## Script will ask for an html page of the collection

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