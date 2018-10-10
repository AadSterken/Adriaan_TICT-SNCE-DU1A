getallenlijst = [2, 5, 7, 3, 9, 2, 8]


def som(g):
    s=0
    for t in range(0, (len(g))):
        s = s + g[t]
        t += 1
    return s


print(som(getallenlijst))



