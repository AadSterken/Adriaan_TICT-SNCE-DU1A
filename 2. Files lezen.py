

filename = "kaartnummers.txt"


def kaartnummers(filename):

    file = open(filename,'r')


    
    for line in file.readlines():
        split = line.split(",")
        naam = split[0].rstrip()
        nummers = split[1].rstrip()
        print('{0:^8}{1:^2}'.format(nummers + ' heeft kaartnummer: ', naam))
    file.close()




kaartnummers(filename)



