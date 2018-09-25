getallenlijst = [2, 5, 7, 3, 9, 2]
totaal = 0


def som(g, s):
    for t in range(1, (len(g))):
        while t < (len(g) + 1):
            s = s + g[t]
        return s


print(som(getallenlijst, totaal))



