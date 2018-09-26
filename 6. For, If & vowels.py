s = "Guido van Rossum heeft programmeertaal Python bedacht."


def klinkers(s):
    for i in s:
        if i in "aeuio":
            print(i)

klinkers(s)