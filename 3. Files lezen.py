file = open(r"C:\Users\Adriaan HU\PycharmProjects\Adriaan_TICT-SNCE-DU1A\kaartnummers.txt")
largest = max(open(r"C:\Users\Adriaan HU\PycharmProjects\Adriaan_TICT-SNCE-DU1A\kaartnummers.txt"))


def kaartnummers(file):
    hoogsteNummer = []
    aantal = 0
    for line in file.readlines():
        split = line.split(",")
        naam = split[0].rstrip()
        nummers = split[1].rstrip()
        if hoogsteNummer >= int(nummers):
            hoogsteNummer += nummers
    print(hoogsteNummer)






kaartnummers(file)