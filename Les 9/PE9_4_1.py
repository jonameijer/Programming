import csv

with open('newfile.csv','w',newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('artikelnummer','artikelcode','naam','voorraad','prijs'))

    while True:
        Artikelnummer = input('Artikelnummer: ')
        if Artikelnummer == '':
            break
        Artikelcode = input('Artikelcode: ')
        Naam = input('Naam: ')
        Voorraad = input('Voorraad: ')
        Prijs = input('Prijs: ')

        writer.writerow((Artikelnummer,Artikelcode,Naam,Voorraad,Prijs))