maand = input('welke maand? ')



def seizoen(maand):
    maandlijst = ['januari', 'februari', 'maart', 'april', 'mei',
                  'juni', 'juli', 'augustus', 'september', 'oktober',
                  'november', 'december']
    maandnummer = maandlijst.index(maand)

    if maandnummer >= 2 and  maandnummer < 5:
        print('lente')
    elif maandnummer >= 5 and  maandnummer < 8:
        print('zomer')
    elif maandnummer >= 8 and  maandnummer < 11:
        print('herfst')
    else:
        print('winter')

seizoen(maand)