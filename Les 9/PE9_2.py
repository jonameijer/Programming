import datetime
import csv
bestand = 'inloggers.csv'
#gebruik hier een herhalingslus:
naam = input("Wat is je achternaam? ")
voorl = input("Wat zijn je voorletters? ")
gbdatum = input("Wat is je geboortedatum? ")
email = input("Wat is je e-mail adres? ")
#wanneer de volgende persoon inlogt is onbekend, dus schrijf meteen naar file

infilea = open('inloggers.csv','a')

date = '{:%Y-%m-%d %H:%M:&S}'.format(datetime.datetime.now)

list = date,';',voorl,';',naam,';',gbdatum,';',email
string = ''.join(list)

print(string)