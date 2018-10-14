
def tuple():
    tuple = (1, 2, 3)
    regel = ['Tuples']
    try:
        tuple.sort()
        regel += ['ja']
    except:
        regel += ['nee']
    try:
        tuple[1] = tuple[0]
        regel += ['ja']
    except:
        regel += ['nee']
    try:
        for item in tuple:
            continue
        regel += ['ja']
    except:
        regel += ['nee']
    try:
        tuple = (1, 2, 2)
        regel += ['ja']
    except:
        regel += ['nee']
    return regel


def dictionary():
    dictionary = {1: 'big', 2: 'medium', 3: 'small'}
    regel = ['Dictionaries']
    try:
        dictionary.sort()
        regel += ['ja']
    except:
        regel += ['nee']
    try:
        dictionary[1] = tuple[0]
        regel += ['ja']
    except:
        regel += ['nee']
    try:
        for item in dictionary:
            continue
        regel += ['ja']
    except:
        regel += ['nee']
    try:
        dictionary = {1: 'big', 2: 'medium',1: 'big', 4: 'medium'}
        regel += ['ja']
    except:
        regel += ['nee']
    return regel

def set():
    set = {1, 2, 3}
    regel = ['Sets']
    try:
        set.sort()
        regel += ['ja']
    except:
        regel += ['nee']
    try:
        set[1] = tuple[0]
        regel += ['ja']
    except:
        regel += ['nee']
    try:
        for item in set:
            continue
        regel += ['ja']
    except:
        regel += ['nee']
    try:
        set = (1, 2, 2)
        regel += ['ja']
    except:
        regel += ['nee']
    return regel

def list():
    list = [1, 2, 3]
    regel = ['Lists']
    try:
        set.sort()
        regel += ['ja']
    except:
        regel += ['nee']
    try:
        set[1] = tuple[0]
        regel += ['ja']
    except:
        regel += ['nee']
    try:
        for item in set:
            continue
        regel += ['ja']
    except:
        regel += ['nee']
    try:
        set = (1, 2, 2)
        regel += ['ja']
    except:
        regel += ['nee']
    return regel

def table():
    tuple = tuple()
    dictionary = dictionary()
    set = set()
    list = list()


tuple = tuple()
dictionary = dictionary()
set = set()
list = list()

print('{0:14}''{1:14}''{2:14}''{3:14}''{4:14}'.format('', 'geordend', 'muteerbaar', 'iterable', 'Dubbele waarden toegestaan'))
print('{0:14}''{1:14}''{2:14}''{3:14}''{4:14}'.format(tuple[0], tuple[1], tuple[2], tuple[3], tuple[4]))
print('{0:14}''{1:14}''{2:14}''{3:14}''{4:14}'.format(dictionary[0], dictionary[1], dictionary[2], dictionary[3], dictionary[4]))
print('{0:14}''{1:14}''{2:14}''{3:14}''{4:14}'.format(set[0], set[1], set[2], set[3], set[4]))
print('{0:14}''{1:14}''{2:14}''{3:14}''{4:14}'.format(list[0], list[1], list[2], list[3], list[4]))
