uren = float(input('Hoeveel uur heb je gewerkt: '))

uurloon = float(input('Wat verdien je per uur: '))

verdiend = round((uren * uurloon), 2)

print('Je hebt ' + str(uren) + ' niet gewerkt en ' + str(verdiend) + ' verdiend')