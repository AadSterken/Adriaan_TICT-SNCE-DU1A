afstandKM = int(input('Afstand in KM: '))
prijs = float(0)
leeftijd = int(input('Leeftijd in jaren: '))
weekeind_Invoer = input('Is het weekeind? ')

if weekeind_Invoer == 'ja':
    weekeind = True
else:
    weekeind = False


def ritprijs(leeftijd, weekeind, afstandKM):
    afstandKM = standaardprijs(afstandKM)
    if (leeftijd < 12) or (leeftijd > 64):
        if weekeind == True:
            afstandKM = afstandKM * 0.65
        else:
            afstandKM = afstandKM * 0.70
        return round(afstandKM, 2)
    else:
        if weekeind == True:
            afstandKM = afstandKM * 0.60
            return afstandKM
        else:
            return round(afstandKM, 2)


def standaardprijs(afstandKM):
    if afstandKM < 0:
        afstandKM = 0

    if afstandKM < 50:
        afstandKM = 0.80 * afstandKM
    else:
        afstandKM = afstandKM * 0.60 + 15
    return afstandKM

print(ritprijs(leeftijd, weekeind, afstandKM))


