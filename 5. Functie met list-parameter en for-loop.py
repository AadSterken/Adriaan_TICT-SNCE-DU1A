grondgetallen = [3, 9, -5, 2, -5]
som = 0

def kwadratensom(g, s):
    for i in range(len(g)):
        if g[i] > 0:
            k = g[i]**2
            s = s + k
            i = i + 1
    print(s)

kwadratensom(grondgetallen, som)
