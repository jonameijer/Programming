cijferICOR = 6
cijferPROG = 8
cijferCSN = 7

gemiddelde = (cijferICOR + cijferPROG + cijferCSN)/3
beloning = 30
beloningtotaal = 3*(gemiddelde * beloning)

line1 = 'Mijn cijfers (gemiddeld een '
line2 = ') leveren een beloning van $ '
line3 = 'op!'
print(line1,gemiddelde,line2,beloningtotaal,line3)