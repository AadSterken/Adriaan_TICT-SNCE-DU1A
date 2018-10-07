
file = open(r"C:\Users\Adriaan HU\PycharmProjects\Adriaan_TICT-SNCE-DU1A\kaartnummers.txt")
largest = max(open(r"C:\Users\Adriaan HU\PycharmProjects\Adriaan_TICT-SNCE-DU1A\kaartnummers.txt"))


def kaartnummers(file):
    regels = 0
    for line in file.readlines():
        split = line.split(",")
        naam = split[0].rstrip()
        nummers = split[1].rstrip()
        print('{0:^8}{1:^2}'.format(nummers + ' heeft kaartnummer: ', naam))




kaartnummers(file)



