## The Steam Workshop Collection Modlist Extractor (SWCME) is intended to extract the mod ID's from workshop mod collections.
## The SWCME will accept the collection ID or it's URL, and process the page to create a .csv file of comma separated mod ID's.
## The SWCME will output the 'modlist.csv' to the current working directory of the script, as well as print it in the terminal.

from lxml import html
import requests

input('Welcome to the SWCME, press Enter to continue...')

modid = int(0)
while True:
    try:
        modid = int(input('Please provide the Steam Workshop Collection ID number. [Integers 0-9, max length 10] '))
    except ValueError:
        print('ERROR!: Input was not recognised as a number.')
    if 1 <= int(modid) <= 9999999999:
        break
    else:
        print('Please Try your input again.')

page = requests.get('https://steamcommunity.com/sharedfiles/filedetails/?id=' + str(modid))
tree = html.fromstring(page.content)
idloc = tree.xpath('//div[@id="profileBlock"]//div[contains(@class, "collectionItem") and starts-with(@id, "sharedfile_")]')
idnum = [element.get("id").replace("sharedfile_","") for element in idloc]
modlist = ','.join(idnum)
filename = 'modlist.csv'
print('Mod Extraction complete! The following mod IDs have been located:')   
print(modlist)
input('Press Enter to write to file and continue.')
outfile = open(filename,'w')
outfile.write(modlist)
outfile.close()
input('File generation complete, press Enter to exit.')
quit()
