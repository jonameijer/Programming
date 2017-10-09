woord = input('Geef een string van vier letters: ')
while len(woord) != 4:
    print(woord, 'heeft', len(woord),'letters')
    woord = input(':')
print('Inlezen van correcte string: ',woord,'is geslaagd')