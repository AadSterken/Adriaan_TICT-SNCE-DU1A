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


# def kaartnummers(file):
#     largest = max(file)         # str
#     split = largest.split(', ') # lst
#     hoogste = int(split[0])     # int
#     aantal = 0
#     regelNummer = 0
#     for line in file:
#         split = line.split(",")
#         nummers = split[0].rstrip()
#
#         if nummers != split:
#             aantal += 1
#
#


        # largest = max(file)
        # if nummers == largest:
        # #     regelNummer = aantal
        #     print(regelNummer)

# def kaartnummers():
#     for line in file.readlines():
#         split = line.split(",")
#         naam = split[0].rstrip()
#         nummers = split[1].rstrip()
#         num_list.append(largest)
#         largest = num_list.split(',')
#         print(naam, nummers, sep=": ")
#     print("Deze file telt:", len(open(r"C:\Users\Home\PycharmProjects\untitled\Opdrachten\kaartnummers.txt").readlines()), "regels")
#     print("Het grootste kaartnummer is:", max(num_list),  "en staat op regel:", (num_list.index(max(num_list)))+1)
#
#
#
# kaartnummers()


