file = open(r"C:\Users\Adriaan HU\PycharmProjects\Adriaan_TICT-SNCE-DU1A\kaartnummers.txt")



def kaartnummers(file):
    largest = max(open(r"C:\Users\Adriaan HU\PycharmProjects\Adriaan_TICT-SNCE-DU1A\kaartnummers.txt"))
    split = largest.split(', ')
    hoogste = int(split[0])
    aantal = 0
    regelNummer = 0
    for regels in file:
        aantal += 1
        split = regels.split(",")
        nummers = split[0].rstrip()
        if int(nummers) == int(hoogste):
            regelNummer = aantal

    print('Deze file telt ' + str(aantal) + ' regels.')
    print('Het grootste kaartnummer is: ' + str(hoogste) + ' en dat staat op regel ' + str(regelNummer))


kaartnummers(file)
