getallenlijst = [2, 5, 7, 3, 9, 2]
totaal = 0


def som(g, s):
    for t in range(g[0], g[5]):
        s = s + g[t-1]
        return s


print(som(getallenlijst, totaal))


