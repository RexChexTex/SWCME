## Script will output a total of discovered mods
## Script will output the stored location of the output file
## TO DO: Remove hardcoded page variable, rename and allow user input of steam workshop ID OR URL

from lxml import html
import requests

page = requests.get('https://steamcommunity.com/sharedfiles/filedetails/?id=1724309839')
tree = html.fromstring(page.content)
idloc = tree.xpath('//div[@id="profileBlock"]//div[contains(@class, "collectionItem") and starts-with(@id, "sharedfile_")]')
idnum = [element.get("id").replace("sharedfile_","") for element in idloc]
modlist = ','.join(idnum)
filename = 'modlist.csv'   

print(modlist)
input('Press enter to write to file and continue')
outfile = open(filename,'w')
outfile.write(modlist)
outfile.close()
input('File generation complete, thanks!')
