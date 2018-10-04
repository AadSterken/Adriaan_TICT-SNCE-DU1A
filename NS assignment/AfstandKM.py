def standaardprijs(afstandKM):
    if afstandKM < 0:
        afstandKM = 0

    if afstandKM < 50:
        afstandKM = 0.80 * afstandKM
    else:
        afstandKM = afstandKM * 0.60 + 15
    return afstandKM