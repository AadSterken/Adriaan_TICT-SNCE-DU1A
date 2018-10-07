import datetime

file = open(r"C:\Users\Adriaan HU\PycharmProjects\Adriaan_TICT-SNCE-DU1A\Hardlopers.txt", 'w')

aantal = 0

while True:



    # if aantal < 5:
    #     aantal += 1


    def datum():
        vandaag = datetime.datetime.today()
        datum = vandaag.strftime("%a %d %b %Y")
        return datum


    def invoer():
        invoer = input('Vul hier je tijd en je naam in in het volgende format: 11:15:48 Jan Janssen.\n '
                       'Type \'stop\' om te stoppen \n')
        # invoer = invoer.split('')
        # print(invoer)
        return invoer


    def bestand(file, invoer, datum):
        if invoer != 'stop':
            invoer = invoer.split(' ')
            naam = invoer[1] + ' ' + invoer[2]
            tijd = invoer[0]
            file.writelines('{0:8} {1:8} {2:8}'.format(datum, tijd, naam) + '\n')
        else:
            exit()

    invoer = invoer()
    datum = datum()
    bestand(file, invoer, datum)


