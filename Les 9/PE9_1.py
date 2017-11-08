prijs = 4356
try:
    personen = int(input('aantal personen: '))
except ValueError:
    print('Dit is geen getal')

try:
    if personen < 0:
        print('Negatieve getallen mogen niet')
    else:
        try:
            ans = prijs // personen
        except ZeroDivisionError:
            print('Delen door nul kan niet')
        except NameError:
            pass
except NameError:
    pass

try:
    print(ans)
except:
    pass