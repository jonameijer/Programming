import csv

with open('scores.csv','r') as myCSVFile:
    reader = csv.DictReader(myCSVFile, delimiter=';')
    scores = []
    for row in reader:
        scores.append(row['score'])

geen idee