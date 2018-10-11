

while True:
    woord = input('Geef een woord van vier letter: ')
    if len(woord) == 4:
        print('Inlezen van correcte string: ' + str(woord) + ' is geslaagd')
        break
    else:
        print(str(woord) + ' heeft ' + str(len(woord)) + ' letters')



