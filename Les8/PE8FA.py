
def inlezen_beginstation(stations):
    station = input('Wat is uw beginstation: ')
    while station not in stations:
        station = input('Wat is uw beginstation: ')
    return station

def inlezen_eindstation(stations,beginstation):
    station = input('Wat is uw eindstation: ')
    while station not in stations:
        station = input('Wat is uw eindstation: ')
    return station

def omroepen_reis(stations, beginstation, eindstation):
    print('Beginstation:',beginstation,', dit is het',stations.index(beginstation)+1,'ste station.')
    print('Eindstation:',eindstation,', dit is het',stations.index(eindstation)+1,'ste station')
    print('Aantal tussenstations:',stations.index(eindstation)-stations.index(beginstation)-1)
    print('Ritprijs:',(stations.index(eindstation)-stations.index(beginstation))*5,'euro')
    begin = int(stations.index(beginstation))
    eind = int(stations.index(eindstation))
    print('Stations',stations[begin:(eind+1)])

stations = ['Schagen','Heerhugowaard','Alkmaar','Castricum','Zaandam',
            'Amsterdam Sloterdijk','Amsterdam Centraal','Amsterdam Amstel',
            'Utrecht Centraal','’s-Hertogenbosch','Eindhoven','Weert',
            'Roermond','Sittard','Maastricht']
print(stations)
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)