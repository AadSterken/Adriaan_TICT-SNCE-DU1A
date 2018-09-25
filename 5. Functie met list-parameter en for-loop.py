grondgetallen = [3, 9, -5, 2, -5]


def kwadratensom(g):
    s = 0
    for i in range(len(g)):
        if g[i] > 0:
            k = g[i]**2
            s = s + k
            i = i + 1
    print(s)

kwadratensom(grondgetallen)
