
from lxml import html
import requests

page = requests.get('https://steamcommunity.com/sharedfiles/filedetails/?id=1724309839')
tree = html.fromstring(page.content)

idloc = tree.xpath('//div[@id="profileBlock"]//div[contains(@class, "collectionItem") and starts-with(@id, "sharedfile_")]')

idnum = [element.get("id").replace("sharedfile_","") for element in idloc]

output = ','.join(idnum)

print(output)

## Script will output a total of discovered mods
## Script will output the stored location of the output file
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