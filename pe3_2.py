leeftijd = int(input('Geef je leeftijd: '))
nationaliteit = input('Nederlands paspoort: ')


def stemrecht(a, b):
    if (a == 'ja') and (b > 17):
        print('gefeliciteerd je mag stemmen!')
    else:
        print('Je mag niet stemmen')


stemrecht(nationaliteit, leeftijd)
