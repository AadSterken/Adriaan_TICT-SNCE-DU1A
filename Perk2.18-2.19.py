print('2.18')
flowers = ['rose', 'bougainvillea', 'yucca', 'marigold', 'daylilly', 'lilli of the valley']
print('potato' in flowers)
thorny = [flowers[0]] + [flowers[1]] + [flowers[2]]
poisonous = [flowers[-1]]
dangerous = [thorny] + [poisonous]
print(dangerous)
print(' ')
print('2.19')
answers = ['Y', 'Y', 'N', 'Y', 'N', 'N', 'Y', 'N', 'Y', 'N', 'N', 'N', 'Y']
numYes = answers.count('Y')
numNos = answers.count('N')
percentYes = round(numYes / (len(answers) / 100), 2)
answers.sort()
f = answers.index('Y')
print(f)
print(' ')
print('2.28')
lst = [7, 1, 8, 6, 4, 7, 8, 6, 5, 9, 4, 8, 2, 6, 5, 6, 3]
middleChar = lst[int(abs(len(lst)/2))]
print(middleChar)
middleIndex = int((len(lst)/2)-1)
print(middleIndex)
lst.sort()
lst.append(lst[0])
lst.remove(lst[0])
print(' ')
print('2.31')
print('extend() appends multiple items to the list. copy()'
      ' copies the list into a new list object. clear() takes all content out of the list')
print(' ')
print('3.17')
test1 = eval('2 * 3 + 1')
test2 = eval("'hello'")
test3 = eval("'hello' + ' ' + 'world'")
test4 = eval("'ASCII'.count('I')")
test5 = eval("'x = 5'")
print(test5)
print(' ')
print('3.18')
print('zie printscreens in huiswerk map')
print(' ')
print('3.22')
lst2 = [2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(lst2)):
    if (((lst2[i])**2) % 8) == 0:
        print(lst2[i])
print(' ')
print('3.23')
for f in range(2):
    print(f)
for g in range(3, 6):
        print(g)
