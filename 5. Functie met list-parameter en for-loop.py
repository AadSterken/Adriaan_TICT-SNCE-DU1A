grondgetallen = [3, 9, -5, 2, -5]


def kwadratensom(g):
    s = 0
    for i in g:
        if i > 0:
            k = i**2
            s = s + k
    print(s)

kwadratensom(grondgetallen)
