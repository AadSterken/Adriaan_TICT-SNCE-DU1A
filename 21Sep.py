import math
def hyp(a,b):
    res = math.sqrt(a**2 + b**2)
    return(res)
print(hyp(3,4))

def hello(name):
    return 'Welcome, '+name+', to the world of Python'
print(hello('jos'))

def rng(lijst):
    res = max(lijst) - min(lijst)   #uitrekenen
    return res                      #return
print(rng([1,7,12,10]))

def swapFS(mylst[]):
    if len(mylst[]) >= 2:
        mylst[0],mylst[1]=mylst[1],mylst[0]
        return mylst[]

