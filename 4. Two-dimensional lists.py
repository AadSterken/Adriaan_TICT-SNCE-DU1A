studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]


# def gemiddelde_per_student(studentencijfers): # Dit is miijn eigen code
#     studentnummer = 0
#     antw = []
#     for student in studentencijfers:
#         studentnummer += 1
#         aantal = 0
#         totaal = 0
#         for cijfer in student:
#             aantal += 1
#             totaal = totaal + cijfer
#         gem = totaal / aantal
#         antw.append(gem)
#     return antw

def gemiddelde_per_student(studentencijfers): # Deze is van Leo
    ant = []
    for ii in studentencijfers:
        ant.append(sum(ii)/len(ii))
    return ant





def gemiddelde_van_alle_studenten(studentencijfers):
    aantalCijfers = 0
    totaal = 0
    for gemiddelde in gemiddelde_per_student(studentencijfers):
        totaal = totaal + gemiddelde
        aantalCijfers += 1
    antw = totaal / aantalCijfers
    return round(antw)

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))