celsius = 0
print('{0:^6}{1:^6}'.format(" F", " C"))

def convert(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit


def table(celsius):
    fahrenheit = convert(celsius)
    for celsius in range(-30, 50, 10):
        print('{0:6} {1:6}'.format(convert(celsius), fahrenheit))



table(celsius)
