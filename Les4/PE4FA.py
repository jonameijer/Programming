def standaardtarief(afstandKM):
    if afstandKM > 50:
        output = 15 + afstandKM*.6
    else:
        output = afstandKM*.8
    if afstandKM < 0:
        output = 0
    return output


def ritprijs(leeftijd,weekendrit,afstandKM):
    if weekendrit == 'ja':
        if leeftijd < 12 or leeftijd >= 65:
            output = (standaardtarief(afstandKM))*.65
        else:
            output = (standaardtarief(afstandKM))*.6
    else:
        if leeftijd < 12 or leeftijd >= 65:
            output = (standaardtarief(afstandKM))*.7
        else:
            output = (standaardtarief(afstandKM))
    return output


a = eval(input('Hoe oud bent u: '))
b = input('Is het weekend? (ja, nee): ')
c = eval(input('Hoe ver rijst u: '))
print('Het kost',round(ritprijs(a,b,c),2),'euro voor een rit van',c,'kilometer.')