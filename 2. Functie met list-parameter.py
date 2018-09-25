getallenlijst = [2, 5, 7, 3, 9, 2, 8]
totaal = 0


def som(g, s):
    for t in range(0, (len(g))):
        s = s + g[t]
        t=t+1
    return s


print(som(getallenlijst, totaal))



