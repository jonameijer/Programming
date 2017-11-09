import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

filedict = processXML('PE10FA.xml')
file = filedict['Stations']['Station']

print('Dit zijn de codes en types van de 4 stations:')
for data in file:
    print(data['Code'],'\t-',data['Type'])
print('\nDit zijn alle stations met één of meer synoniemen')
for data in file:
    try:
        print(data['Code'],'\t-',data['Synoniemen']['Synoniem'])
    except:
        pass
print('\nDit is de lange naam van elk station:')
for data in file:
    print(data['Code'],'\t-',data['Namen']['Lang'])