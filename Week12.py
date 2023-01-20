#PROG 1
'''def mymap(fxn,L):
    out = []
    for i in L:
        out.append(fxn(i))
    return out
L1 = list(input().split())
L2 = list(input().split())
L = [x for x in range(1,21,2)]
print(mymap(lambda x:x**2,L))
print(mymap(lambda x:str(x)+'ing',L2))
print(mymap(lambda x:(x,len(str(x))),L1))'''

#PROG 2
'''def myfilter(fxn,L):
    out = []
    for i in L:
        if fxn(i) == True:
            out.append(i)
    return out
L = list(input().split())
print(myfilter(lambda x:not x[0].isdigit(),L))
print(myfilter(lambda x:len(x)>6,L))
ch = input()
print(myfilter(lambda x:x.endswith(ch),L))'''

#PROG 3
'''def myreduce(fxn,L):
    out = ''
    for i in L:
        out = fxn(out,i)
    return out

def myreduce2(fxn,L):
    out = 0
    for i in L:
        out = fxn(out,i)
    return out

def myreduce3(fxn,L):
    out = 1
    for i in L:
        out = fxn(out,i)
    return out


def prod(x,y):
    return x*y

def part2(x,y):
    x+y
def concword(x,y):
    return x+y[0]
N = list(input().split())
print(myreduce(concword,N))
L = [m for m in range(1,10)]
print(myreduce2(lambda x,y:x+y ,L))
X = [l for l in range(1,10)]
print(myreduce3(prod,X))'''