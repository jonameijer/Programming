def kwadraten_som(grondgetallen):
    kwadraten = []
    for grondgetal in grondgetallen:
        if grondgetal > 0:
            kwadraten.append(grondgetal**2)
    return sum(kwadraten)

lst = [4,5,3,-81]

print(kwadraten_som(lst))
