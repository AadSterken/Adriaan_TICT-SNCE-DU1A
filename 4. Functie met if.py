o = (input('Enter your old password: '))
n = (input('Enter a new password: '))
a = True
b = False


def new_password(n, o):
    l=0
    if n != o:
        if len(n) > 5:
            for l in range(len(n)):
                s = n[l]
                if s.isdigit() == a:
                    print(a)
                    exit()
                else:
                    l + 1
            else:
                print(b)
        else:
            print(b)
    else:
        print(b)


new_password(n, o)
