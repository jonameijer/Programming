bruin = ['Boxtel','Best','Breukenlaan','Eindhoven','Helmond \'t hout','Helmond','Helmond Brouwhuis','Deurne']
groen = ['Boxtel','Best','Breukenlaan','Eindhoven','Geldrop','Heeze','Weert']
bruin = set(bruin)
groen = set(groen)

print('Groen:',groen)
print('Bruin:',bruin)
print('Overeenkomsten')
print(bruin & groen,'\n')

print('Verschillen')
print('Wel in bruin:',bruin - groen)
print('Wel in groen:',groen - bruin)