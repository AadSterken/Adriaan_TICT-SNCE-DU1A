invoer = "5-9-7-1-7-8-3-2-4-8-7-9"


def uitvoer(invoer):
    list = invoer.split('-')
    getallenlijst = []
    for item in list:
        item = int(item)
        getallenlijst.append(item)
        getallenlijst.sort()
    print('Gesorteerde list van ints: ' + str(getallenlijst))
    gemiddelde = sum(getallenlijst) / len(getallenlijst)
    print('Grootste getal: ' + str(max(getallenlijst)) + ' en kleinste getal: ' + str(min(getallenlijst)))
    print('Aantal getallen: ' + str(len(getallenlijst)) + ' en Som van de getallen: ' + str(sum(getallenlijst)))
    print('Gemiddelde: ' + str(gemiddelde))


uitvoer(invoer)
