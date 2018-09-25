s = "Guido van Rossum heeft programmeertaal Python bedacht."


def klinkers(s):
    k = ""
    for i in range(len(s)):
        if (((s[i] == 'a') or (s[i] == 'e')) or
        (s[i] == 'i')) or ((s[i] == 'o') or (s[i] == 'u')):
            k = k + s[i]
            i = i + 1
    print(k)

klinkers(s)
