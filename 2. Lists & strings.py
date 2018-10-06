lijst = eval(input('geef lijst met minimaal 10 strings'))

lijstVanVierLetterWoorden = []
for woord in lijst:
    if len(woord) == 4:
        lijstVanVierLetterWoorden += [woord]


print('De nieuw-gemaakte lijst met alle vier-letter strings is:')
print(lijstVanVierLetterWoorden)