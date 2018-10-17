

def cond():

    totaal = 0
    aantal = -1
    invoer = 1

    while invoer != 0:

        invoer = int(input('Geef een getal dat niet 0 is: '))
        totaal += invoer
        aantal += 1

    print('Er zijn ' + str(aantal) + ' cijfers ingevoerd.\n Het totaal is ' + str(totaal))


cond()
