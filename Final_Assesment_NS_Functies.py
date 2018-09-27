afstandKM = int(input('Afstand in KM: '))
leeftijd = int(input('Leeftijd in jaren: '))
weekeind_Invoer = input('Is het weekeind? ')

if weekeind_Invoer == 'ja':
    weekeind = True
else:
    weekeind = False


def ritprijs(l, w, a):
    a = standaardprijs(a)
    if (l < 12) or (l > 64):
        if w == True:
            a = a * 0.65
        else:
            a = a * 0.70
        return round(a, 2)
    else:
        if w == True:
            a = a * 0.60
            return round(a, 2)
        else:
            return round(a, 2)


def standaardprijs(a):
    if a < 0:
        a = 0
    if a < 50:
        a = 0.80 * a
    else:
        a = a * 0.60 + 15
    return round(a, 2)

print('Deze rit kost €' + str(ritprijs(leeftijd, weekeind, afstandKM)))


