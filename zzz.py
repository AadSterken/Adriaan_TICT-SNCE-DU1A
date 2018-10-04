height = int(input('height in inch: '))
weight = float(input('weight in pounds: '))

def BMI(h, w):
    b = (w*703)/h**2
    if b >= 25.0:
        return 'overweight'
    elif b >= 18.5:
        return 'normal'
    else:
        return 'underweight'

print(BMI(height, weight))

s ='Random access memory'

def acronym(s):
    f = ''
    for i in s.split(' '):
        f += i[0]
    print(f)

acronym(s)