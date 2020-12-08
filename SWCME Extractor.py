## The Steam Workshop Collection Modlist Extractor (SWCME) is intended to extract the mod ID's from workshop mod collections.
## The SWCME will accept the collection ID or it's URL, and process the page to create a .csv file of comma separated mod ID's.
## The SWCME will output the 'modlist.csv' to the current working directory of the script, as well as print it in the terminal.
## https://steamcommunity.com/sharedfiles/filedetails/?id=180077636 is the current development variable for the URL extractions.

from lxml import html
import requests

def greet():
    input('Welcome to the SWCME, press Enter to continue...')

def getModID():
    modId = int(0)
    while True:
        try:
            modId = int(input('Please provide the Steam Workshop Collection ID number. [Integers 0-9, max length 10] '))
        except ValueError:
            print('ERROR!: Input was not recognised as a number.')
        if 1 <= int(modId) <= 9999999999:
            break
        else:
            print('Please Try your input again.')
    return modId

def createWorkshopUrl():
    workshopUrlHead = str('https://steamcommunity.com/sharedfiles/filedetails/?id=')
    workshopUrl = str(workshopUrlHead) + str(getModID())    
    return workshopUrl

def pullCollectionInfo():
    while True:
        try:
            collectionInfo = requests.get(createWorkshopUrl())
        except requests.exceptions.HTTPError:
            print('HTTP Error returned from this URL, please try again.')
        if collectionInfo.status_code == 200:
            break
        else:
            print('Error in collection validation, please try again.')
    return html.fromstring(collectionInfo.content)

def treeExtraction():
    collectionTree = pullCollectionInfo()
    modIdLocation = collectionTree.xpath('//div[@id="profileBlock"]//div[contains(@class, "collectionItem") and starts-with(@id, "sharedfile_")]')
    modIdNumber = [element.get("id").replace("sharedfile_","") for element in modIdLocation]
    modList = ','.join(modIdNumber)
    print('Mod ID extraction complete! The following mod IDs have been located: ' + modList)
    input('Press Enter to contune to .csv creation.  The file will be created in the directory of this script.')
    return modList

def outfileGeneration():
    filename = 'modlist.csv'
    outfile = open(filename,'w')
    outfile.write(treeExtraction())
    outfile.close()

def stop():
    print('File generation complete, see script directory for the newly created modlist.csv')
    input('press Enter to exit the program.')
    quit()

def start():
    greet()

def main():
    start()
    outfileGeneration()
    stop()

if __name__ == "__main__":
    main()