getallenlijst = [2, 5, 7, 3, 9, 2]
totaal = 0


def som(g, a):
    s=a
    for t in range(g[0], g[len(g)-1]):
        while t < len(g):
            s = s + g[t-1]


som(getallenlijst, totaal)
print(totaal)

