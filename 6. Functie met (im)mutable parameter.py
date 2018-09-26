lijst = ['a', 'b', 'c']
print(lijst)

def wijzig(l):
    l.clear()
    l.append('d')
    l.append('e')
    l.append('f')

wijzig(lijst)
print(lijst)
