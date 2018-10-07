invoer = input('type een zin: \n')

def gemiddelde(invoer):
    invoer = invoer.split(' ')
    totaal = 0
    teller = 0
    for woord in invoer:
        lengte = len(woord)
        totaal += lengte
        teller += 1
    print(totaal / teller)


gemiddelde(invoer)