kluizen = "kluizen.txt"


def toon_aantal_kluizen_vrij(kluizen):
    file = open(kluizen, "r")
    counter = 0
    for line in file.readlines():
        split = line.split(";")
        wachtwoord = split[1].rstrip()
        if wachtwoord == "":
            counter += 1
    file.close()
    return counter


def nieuwe_kluis(kluizen):
    fileRead = open(kluizen, "r")
    lines = fileRead.readlines()
    for line in lines:
        split = line.split(";")
        kluis = split[0].rstrip ()
        wachtwoord = split[1].rstrip()
        if wachtwoord == "":
            while True:
                invoer = input('Voer uw wachtwoord in: ')
                if len(invoer) >= 4:
                    lines[int(kluis) - 1] = kluis + ";" + str(invoer) + "\n"
                    fileWrite = open(kluizen, "w")
                    fileWrite.writelines(lines)
                    fileWrite.close()
                    print("U kluis is:" + str(kluis))
                    break
                else:
                    print("Uw wachtwoord is te kort")
        fileRead.close()


def kluis_openen(kluizen):
    file = open(kluizen, 'r')
    authenticated = False
    invoer_kluis = input('Voer uw kluisnummer in: ')
    invoer_ww = input('Voer uw wachtwoord in: ')
    for line in file.readlines():
        split = line.split(";")
        kluis = split[0].rstrip()
        wachtwoord = split[1].rstrip()
        if (invoer_kluis == str(kluis)) and (invoer_ww == str(wachtwoord)):
            print("Kluis:" + str(kluis) + " nu open!")
            authenticated = True
    if authenticated == False:
        print('Uw kluisnummer en wachtwoord komen niet overeen.')
    file.close()


def kluis_teruggeven(kluizen):
    released = False
    fileRead = open(kluizen, 'r')
    lines = fileRead.readlines()
    invoer_kluis = input('Voer uw kluisnummer in: ')
    invoer_ww = input('Voer uw wachtwoord in: ')
    for line in lines:
        split = line.split(";")
        kluis = split[0].rstrip ()
        wachtwoord = split[1].rstrip()
        if (invoer_kluis == str(kluis)) and (invoer_ww == str(wachtwoord)):
            lines[int(kluis) - 1] = kluis + ";" + "" + "\n"
            fileWrite = open(kluizen, "w")
            fileWrite.writelines(lines)
            fileWrite.close()
            print("U heeft kluis " + str(kluis) + " ingeleverd.")
            released = True
    if released == False:
        print("Kluis of wachtwoord incorrect")
    fileRead.close()




while True:
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
    print('2: Ik wil een nieuwe kluis')
    print('3: Ik wil even iets uit mijn kluis halen')
    print('4: Ik geef mijn kluis terug')
    print('5. Ik wil stoppen')
    invoer = input('')
    if invoer == str(1):
        print('er zijn nog ' + str(toon_aantal_kluizen_vrij(kluizen)) + ' kluizen vrij')
    elif invoer == str(2):
        nieuwe_kluis(kluizen)
    elif invoer == str(3):
        kluis_openen(kluizen)
    elif invoer == str(4):
        kluis_teruggeven(kluizen)
    elif invoer == str(5):
        break
    else:
        print('Uw heeft geen correcte invoer gegeven')

