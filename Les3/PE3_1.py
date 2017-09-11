score = eval(input('Geef je score: '))
line1 = 'Gefeliciteerd!'
line2 = 'Met een score van'
line3 = 'ben je geslaagd!'
line4 = 'Helaas.'
line5 = 'ben je gezakt.'
if score>15:
    print(line1)
    print(line2,score,line3)
#else:
#    print(line4)
#    print(line2,score,line5)