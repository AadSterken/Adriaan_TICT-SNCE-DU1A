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
# # 		break
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


def nieuwe_kluis(kliuzen):
    file = open(kluizen, "r")
    counter = 0
    for line in file.readlines():
        split = line.split(";")
        kluis = split[0].rstrip ()
        wachtwoord = split[1].rstrip()
        counter += 1
        if wachtwoord == "":
            while True:
                wachtwoord = input('Type uw wachtwoord: ')
                if len(wachtwoord) >= 4:
                    filewrite = open(kluizen, "w")
                    line = kluis + ";" + input('Type uw wachtwoord: ') + "\n"
                    filewrite.writelines(line)
                    filewrite.close()
                    print("U kluis is:" + str(counter))
                    break
                else:
                    print("Uw wachtwoord is te kort")