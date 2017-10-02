def seizoen(maand):
    if maand == 12:
        print('Het is winter in December')
    elif maand == 1:
        print('Het is winter in Januari')
    elif maand == 2:
        print('Het is winter in Februari')
    elif maand == 3:
        print('Het is lente in Maart')
    elif maand == 4:
        print('Het is lente in April')
    elif maand == 5:
        print('Het is lente in Mei')
    elif maand == 11:
        print('Het is winter in November')
    elif maand == 10:
        print('Het is winter in Oktober')
    elif maand == 9:
        print('Het is winter in September')
    elif maand == 8:
        print('Het is winter in Augustus')
    elif maand == 7:
        print('Het is winter in Juli')
    elif maand == 6:
        print('Het is winter in Juni')
    elif maand > 12 or input < 0:
        print('Dat is geen maandnummer')


input = eval(input('Welk maandnummer is het: '))
seizoen(input)