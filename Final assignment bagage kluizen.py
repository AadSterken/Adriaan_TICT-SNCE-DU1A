


def kluisreg():

    regels = 0

    while True:



        print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
        print('2: Ik wil een nieuwe kluis')
        print('3: Ik wil even iets uit mijn kluis halen')
        print('4: Ik geef mijn kluis terug')
        invoer = int(input('Voer het gewenste nummer in: '))

        kluizen = open(r"C:\Users\Adriaan HU\PycharmProjects\Adriaan_TICT-SNCE-DU1A\kluizen.txt", 'w')
        regels = kluizen.readlines()

        # for line in kluizen.readlines():
        #     regels += 1

        if invoer == 1:
            print('Er zijn nog ' + str(10 - regels) + ' beschikbaar')
        elif invoer == 2:
            kluisnummer = input('voer uw kluisnummer in: ')
            code = input('voer uw code in: ')
            kluizen.writelines(code + '; ' + kluisnummer)

# ik zou het wegschrijven in het tekstbestand in een functie kunnen zetten

        elif invoer == 3:
            print(invoer)
            # kluisnummer = input('voer uw kluisnummer in: ')
            # code = input('voer uw code in: ')

# controleren of het overeenkomt
# zoniet dan foutmelding
# indien correct aangeven dat kluis oven kan

        elif invoer == 4:
            print(invoer)
            # kluisnummer = input('voer uw kluisnummer in: ')
            # code = input('voer uw code in: ')

# controleren of het overeenkomt
# zoniet dan foutmelding
# indien correct aangeven dat kluis oven kan
        elif (invoer <  1) or (invoer > 4):
            input('U heeft een fout nummer ingevoerd, type OK om weer terug te komen in het keuzemenu.')


kluisreg()