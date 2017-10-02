print('1: Ik wil weten hoeveel kluizen vrij zijn')
print('2: Ik wil een nieuwe kluis')
print('3: Ik wil mijn kluis openen')
print('4: Ik geef mijn kluis terug')

infiler = open('PE6FA.txt','r')
infilea = open('PE6FA.txt','a')

keuzenummer = eval(input('Geef uw optienummer: '))

def toon_aantal_kluizen_vrij():
    kluizen = infiler.readlines()
    print('Er zijn ',12-len(kluizen),' kluizen beschikbaar.')

def nieuwe_kluizen():
    kluisnummers = [1,2,3,4,5,6,7,8,9,10,11,12]
    kluizen = infiler.readlines()
    open_kluizen = []
    open_kluisnummers = []
    for line in kluizen:
        (nummer, wachtwoord) = line.split(';')
        open_kluisnummers.append(nummer)
    for line in open_kluisnummers:
        open_kluizen.append(int(line.replace('\n','')))
    lege_kluizen = [x for x in kluisnummers if x not in open_kluizen]
    print('Dit zijn de lege kluizen: ',lege_kluizen)
    kluiskeuze = eval(input('Welke kluis wil je: '))
    if kluiskeuze not in lege_kluizen:
        print('Dit is niet mogelijk')
    while kluiskeuze not in lege_kluizen:
        kluiskeuze = eval(input('Welke kluis wil je: '))
    infilea.write(str(kluiskeuze))
    infilea.write(';')
    infilea.write(input('Geef een wachtwoord: '))
    infilea.write('\n')
    print('Kluis geregistreerd.')


def kluis_openen():
    kluizen = infiler.readlines()
    kluisnummer = input('Geef uw kluisnummer: ')
    kluiswachtwoord = input('Geef uw wachtwoord: ')
    kluiscode = kluisnummer,';',kluiswachtwoord,'\n'
    kluisstring = ''.join(kluiscode)
    if kluisstring in kluizen:
        print('Uw kluis is open.')
    else: print('Kluisnummer en wachtwoord combinatie niet gevonden.')

def kluis_teruggeven():
    kluizen = infiler.readlines()
    kluisnummer = input('Geef uw kluisnummer: ')
    kluiswachtwoord = input('Geef uw wachtwoord: ')
    kluiscode = kluisnummer, ';', kluiswachtwoord, '\n'
    kluisstring = ''.join(kluiscode)
    infilew=open('PE6FA.txt','w')
    if kluisstring in kluizen:
        for line in kluizen:
            if line != kluisstring:
                infilew.write(line)
                infilew.write('\n')
    infilew.close()
    print('Wachtwoord verwijdert.')



if keuzenummer == 1:
    toon_aantal_kluizen_vrij()
if keuzenummer == 2:
    nieuwe_kluizen()
if keuzenummer == 3:
    kluis_openen()
if keuzenummer == 4:
    kluis_teruggeven()

infiler.close()
infilea.close()

