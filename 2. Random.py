import random

def monopolyworp():
    dubbel = 0
    while True:

        first = random.randrange(1, 7)
        second = random.randrange(1, 7)
        if dubbel < 3:
            if first != second:

                print(str(first) + ' + ' + str(second) + ' = ' + str(first + second))
                dubbel = 0
            elif first == second:
                dubbel += 1
                print(str(first) + ' + ' + str(second) + ' = ' + str(first + second) + ' Dubbel')


        else:
            print('Go to jail\nGo directly to jail\nDo not pass go\nDo not collect $200')
            break












monopolyworp()