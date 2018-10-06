# text = 'all animals are equal but soe animals are more equal than other'
#
#
# def wordCount(text):
#     los = text.split(' ')
#     aantal = 0
#     for woord in los:
#         if woord = los[woord]:
#             aantal =+ 1
#             print(woord + aantal)
#         return aantal
#
#
# print(wordCount(text))
#
# nogEenRondje = True
# while nogEenRondje:
# 	print("Wwwwhhoooooeeeeeyyyyy")
# 	nogEenRondje=input("Nog een rondje").upper() == "J"
#
# woord = input("Geef een woord")
# index = 0
# while index <= len(woord):
# 	print(str(index)+" - "+woord[index])
# 	index = index + 1
#
# print("Start", end=" ")
# index = 1
# while False:
# 	print (str(index), end="")
# 	index = index+1
# print("Stop")
#
# while True:
# 	print("JaaaaabbbbbbaaaadaaaaabbbbaaaDDDDDoooooo")
# 	if input("nog een rondje").upper() != 'J':
# 		break
# regel=0
# while regel<3:
# 	print('regel '+str(regel), end=': ')
# 	for index in range(0, 3):
# 		if regel==1:
# 			break
# 			print('$', end=", ")
# 		elif index==0:
# 			pass
# 			print('@', end=", ")
# 		elif index==1:
# 			continue
# 			print("#", end=', ')
# 		print(str(index), end=', ')
# 	regel+=1
# 	print(end='\n')
import random

r = 5
c = 5


def game(r, c):
	tabel = (r * c) * []
	br = random.randrange(0, r)
	bc = random.randrange(0, c)
	bom = [br, bc]
	for pogingen in (r * c):
		gokregel = input('Geef coordinaten regel: ')
		gokkolom = input('Geef coordinaten kolom: ')
		gokcoord = [gokregel, gokkolom]
		pogingen += 1
		if bom == gokcoord:
			print('boem')



game(r, c)