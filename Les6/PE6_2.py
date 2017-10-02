woorden = []
woorden.append(input('Geef een woord: '))
while len(woorden) < 10:
    woorden.append(input('Geef nog een woord: '))
print('Dit zijn alle woorden:\n',woorden,'\n')

vierletterwoorden = []
for woord in woorden:
    if len(woord) == 4:
        vierletterwoorden.append(woord)


print('De nieuw-gemaakte lijst met alle vierletterwoorden is:\n',vierletterwoorden)