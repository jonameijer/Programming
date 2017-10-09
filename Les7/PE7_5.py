naam = input(': ')
namen = []
while naam != '':
    namen.append(naam)
    naam = input(': ')

def frequency(itemlist):
    counters = {}
    for item in itemlist:
        if item in counters:
            counters[item] += 1
        else:
            counters[item] = 1
    return counters

dic = frequency(namen)

for key in dic:
    if dic[key] >1:
        print('Er zijn',dic[key],'studenten met de naam',key)
    else:
        print('Er is',dic[key],'student met de naam',key)