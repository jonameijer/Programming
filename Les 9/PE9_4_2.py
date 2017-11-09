import csv

with open('newfile.csv','r') as myCSVFile:
    reader = csv.DictReader(myCSVFile, delimiter=';')

    duursteprijs = []
    duurstenaam = []
    duursteindex = 0
    kleinstevoorraad = []
    kleinsteartikelnummer = []
    kleinsteindex = 0
    voorraad = []

    for row in reader:
        duurstenaam.append(row['naam'])
        duursteprijs.append(row['prijs'])
        duursteindex = duursteprijs.index(max(duursteprijs))
        kleinstevoorraad.append(row['voorraad'])
        kleinsteartikelnummer.append(row['artikelnummer'])
        kleinsteindex = kleinstevoorraad.index(min(kleinstevoorraad))
        voorraad.append(int(row['voorraad']))

    print('Duurste prijs:',duursteprijs[duursteindex],'Naam:',duursteprijs[duursteindex])
    print('Kleinste voorraad:',kleinstevoorraad[kleinsteindex],'Artikelnummer',kleinsteartikelnummer[kleinsteindex])
    print('Er zijn',sum(voorraad),'Artikelen in voorraad')