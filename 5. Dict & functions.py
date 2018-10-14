
def name():
    namenlijst = {}
    invoer = input('Volgende naam:')
    naam = True
    while naam == True:
        count = 0
        if invoer != ' ':
            for item in namenlijst.items():
                if invoer == item[0]:
                    waarde = item[1]
                    waarde += 1
                    nieuweWaarde = waarde
                    namenlijst[item[0]] = nieuweWaarde
                else:
                    count += 1
            if count == len(namenlijst):
                namenlijst[invoer] = 1
            invoer = input('Volgende naam:')
        else:
            for item in sorted(namenlijst):
                if namenlijst[item] == 1:
                    print('Er is ' + str(namenlijst[item]) + ' student met de naam ' + str(item))
                else:
                    print('Er zijn ' + str(namenlijst[item]) + ' student met de naam ' + str(item))
            break


name()