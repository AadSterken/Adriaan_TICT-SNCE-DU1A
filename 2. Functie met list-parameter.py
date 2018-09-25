getallenlijst = [2, 5, 7, 3, 9, 2]
totaal = 0


def som(g, totaal):
    for t in range(g[0], g[-1]):
        totaal = totaal + g[t-1]
        return totaal


print(som(getallenlijst, totaal))


