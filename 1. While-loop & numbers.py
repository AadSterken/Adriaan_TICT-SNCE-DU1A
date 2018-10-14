

def cond():

    totaal = 0
    aantal = 0
    invoer = int(input('Geef een getal dat niet 0 is'))

    while invoer != 0:

        totaal += invoer
        aantal += 1
        invoer = int(input('Geef een getal dat niet 0 is'))


    print('Er zijn ' + str(aantal) + ' cijfers ingevoerd.\n Het totaal is ' + str(totaal))


cond()
