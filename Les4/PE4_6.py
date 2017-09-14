lijst = ['a','b','c']
def wijzig(a):
    del a[0:len(a)]
    a.extend(['d','e','f'])

print(lijst)
wijzig(lijst)
print(lijst)