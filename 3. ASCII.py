invoerstring = input('naamvertrekaankomst: ')

def code(invoerstring):
    woord = ''
    for letter in invoerstring:
        letter = ord(letter)
        letter = letter + 3
        letter = chr(letter)
        woord += letter
    print(woord)

code(invoerstring)