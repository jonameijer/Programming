def gemiddelde(zin):
    zinsplit = zin.split()
    lenlist = []
    for woord in zinsplit:
        lenlist.append(len(woord))
    return sum(lenlist)/len(lenlist)

input = input('Geef een zin: ')
print('Het gemiddelde woord in deze zin is',round(gemiddelde(input),2),'letters lang.')