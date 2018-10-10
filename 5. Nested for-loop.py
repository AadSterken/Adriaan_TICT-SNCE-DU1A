

for grondgetal in range(1, 11):
    for teller in range(1, 11):
        uitkomst = grondgetal * teller
        # print(str(grondgetal) + ' ' + 'X' + ' ' + str(teller) + ' ' + '=' + ' ' + str(uitkomst))
        print('{0:2}'' X ''{1:^2}'' = ''{2:2}'.format(grondgetal, teller, uitkomst))


