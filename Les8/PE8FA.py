
def inlezen_beginstation(stations):
    input = []
    while input not in stations:
        input = input('Wat is uw beginstation: ')
    return input

def inlezen_eindstation(stations,beginstation):
    input2 = []
    output = [beginstation]
    while input2 not in stations:
        input2 = input('Wat is uw eindstation: ')
    output.append(input2)
    return eindstation

stations = ['Schagen','Heerhugowaard','Alkmaar','Castricum','Zaandam',
            'Amsterdam Sloterdijk','Amsterdam Centraal','Amsterdam Amstel',
            'Utrecht Centraal','’s-Hertogenbosch','Eindhoven','Weert',
            'Roermond','Sittard','Maastricht']
print(stations)
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)