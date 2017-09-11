leeftijd = eval(input('Geef je leeftijd: '))
nationaliteit = input('Nederlands paspoort: ')
line1 = 'Gefeliciteerd, je mag stemmen!'
line2 = 'Je mag niet stemmen.'
if leeftijd>=18 and nationaliteit=='ja':
    print(line1)
else:
    print(line2)