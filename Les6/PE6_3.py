invoer = '5-9-7-1-7-8-3-2-4-8-7-9'
numbers = []
invoer.split()
for num in invoer:
    numbers.append(num)
while '-' in numbers:
    numbers.remove('-')
numbers = list(map(int,numbers))

print('De gegeven getallen:\n',numbers)
numbers.sort()
print('De gesorteerde getallen:\n',numbers)
print('Het grootste getal:\n',max(numbers))
print('Het kleinste getal:\n',min(numbers))
print('Het aantal getallen:\n',len(numbers))
print('De som van de getallen:\n',sum(numbers))
print('Het gemiddelde van de getallen:\n',((sum(numbers)/len(numbers))))
