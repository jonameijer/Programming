string = input('Geef uw naam, locatie en bestemming: ')
ASCII = []
newASCII = []
newstring = []
for letter in string:
    ASCII.append(ord(letter))
for letter in ASCII:
    newASCII.append(letter+3)
for letter in newASCII:
    newstring.append(chr(letter))
print(''.join(newstring))
