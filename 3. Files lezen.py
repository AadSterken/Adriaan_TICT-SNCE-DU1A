


def kaartnummers():
    file2 = open(r"C:\Users\Adriaan HU\PycharmProjects\Adriaan_TICT-SNCE-DU1A\kaartnummers.txt")
    file = file2.readlines()
    length = len(file)
    highest = 0
    counter = 0
    for regels in file:
        split = regels.split(",")
        nummer = int(split[0])
        if nummer > highest:
            highest = nummer
            counter += 1

    print('Deze file telt ' + str(length) + ' regels.')
    print('Het grootste kaartnummer is: ' + str(highest) + ' en dat staat op regel ' + str(counter))
    file2.close()



kaartnummers()
