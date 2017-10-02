student1 = [95,92,86]
student2 = [66,75,54]
student3 = [89,72,100]
student4 = [34,0,0]

studentencijfers = [student1,student2,student3,student4]

def gemiddelde_per_student(studentencijfers):
    for student in studentencijfers:
        print(round(sum(student)/len(student),2))


def gemiddelde_van_alle_studenten(studentencijfers):
    gemiddelde_cijfers = []
    for student in studentencijfers:
        gemiddelde_cijfers.append((sum(student)/len(student)))
    gemiddelde_van_iedereen = (sum(gemiddelde_cijfers)/len(gemiddelde_cijfers))
    print(round(gemiddelde_van_iedereen,2))

gemiddelde_per_student(studentencijfers)
print('\n')
gemiddelde_van_alle_studenten(studentencijfers)