import random

def monopolyworp():
    double = 0
    while True:

        first = random.randrange(1, 7)
        second = random.randrange(1, 7)
        if double < 2:
            if first != second:

                print(str(first) + ' + ' + str(second) + ' = ' + str(first + second))
                double = 0
            elif first == second:
                double += 1
                print(str(first) + ' + ' + str(second) + ' = ' + str(first + second) + ' Double')


        else:
            print(str(first) + ' + ' + str(second) + ' = Go to jail\nGo directly to jail'
                                                     '\nDo not pass go\nDo not collect $200')
            break

monopolyworp()