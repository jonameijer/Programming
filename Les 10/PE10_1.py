import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

filedict = processXML('newfile.xml')
file = filedict['artikelen']['artikel']

for artikel in file:
    print(artikel['naam'])