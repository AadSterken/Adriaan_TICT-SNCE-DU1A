filename = r"C:\Users\Adriaan HU\PycharmProjects\Adriaan_TICT-SNCE-DU1A\filename.txt"

def ticker(filename):
    file = open(filename)
    filedict = {}
    for item in file:
        split = item.split(':')
        filedict[split[0]] = split[1].strip()
    return filedict
    file.close()

def uitvoer(filename):
    dictionary = ticker(filename)
    invoer = input('Enter company name: ')
    for item in dictionary:
        if invoer == item:
            print('Ticket symbol: ' + str(dictionary[item]) + '\n')

    invoer = input('Enter ticket symbol: ')
    for item in dictionary:
        if str(invoer) == str(dictionary[item]):
            print('Company name: ' + str(item))

uitvoer(filename)

