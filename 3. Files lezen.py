file = open(r"C:\Users\Adriaan HU\PycharmProjects\Adriaan_TICT-SNCE-DU1A\kaartnummers.txt")


def kaartnummers(file):
    largest = max(open(r"C:\Users\Adriaan HU\PycharmProjects\Adriaan_TICT-SNCE-DU1A\kaartnummers.txt"))
    largest = largest.split(', ')
    largest = int(largest[0])
    aantal = 0
    regelNummer = 0
    for regels in file:
        aantal += 1
        if regels[aantal] == largest:
            regelNummer = aantal


    print(largest)
    print(aantal)
    print(regelNummer)


kaartnummers(file)

