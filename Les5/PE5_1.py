def convert(temp):
    'converts celsuis to fahrenheit'
    return temp*1.8+32

def table():
    'Puts all temperatures within celsius range -30 to 50 into a talbe'
    print('{:7}{:10}{:10}'.format('','C','F'))
    for temp in range(-30,50,10):
        print('{:10.2f}{:10.2f}'.format(temp,convert(temp)))

table()