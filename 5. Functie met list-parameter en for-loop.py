grondgetallen = [3, 9, -5, 2, -5]


def kwadratensom(g):
    s = 0
    for i in g:
        if i > 0:
            s += (i**2)
    print(s)

kwadratensom(grondgetallen)
