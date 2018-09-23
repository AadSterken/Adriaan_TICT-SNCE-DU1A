old = (input('Enter your old password: '))
new = (input('Enter a new password: '))
a = True
b = False
x = 0


def new_password(n = new, o = old):
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
                return
        else:
            print(b)
    else:
        print(b)


new_password(new, old)
