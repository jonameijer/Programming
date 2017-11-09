import csv

with open('scores.csv','r') as myCSVFile:
    reader = csv.DictReader(myCSVFile, delimiter=';')
    scores = []
    names = []
    dates = []
    index = 0
    for row in reader:
        scores.append(row['score'])
        names.append(row['name'])
        dates.append(row['date'])
        index = scores.index(max(scores))
    print('De hoogste score is:',scores[index],'op',dates[index],'behaald door',names[index])