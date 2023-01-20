#Prog 1
'''prod = lambda x,y:x*y
print(prod(5,6))
'''
'''s = input()
c = input()[0]
T = lambda s,c:s.startswith(c)
print(T(s,c))'''

'''from datetime import *
d = date.today()
print(d)
day = lambda d: d.day
month = lambda d: d.month
year = lambda d: d.year
t = str(time().hour)+':'+str(time().minute)+':'+str(time().second)
print(day(d),month(d),year(d),t)
'''

'''L = [{},{},{},{},{},{},{},{},{}]

sorter = lambda L,k, : sorted(L,key=k)
print(sorter())
'''



#PROG2
'''L = list(input().split())
print(list(filter(lambda s:s[0].isdigit()==False,L)))'''

'''L = list(map(int,list(input().split())))
m = lambda L:max(L)
print(m(L))'''

'''L = [(1,2),(4,2),(6,3)]
def manual(I):
    for i in I:
        if I[i][0]%I[i][1]==0:
            return True
        return False
F = filter(manual,L)
print(list(F))
'''
#PROG3
'''def myreduce(fxn,I):
    r = i[0]
    for i in r[1::]:
        fxn(i)
L = list(map(int,list(input().split())))
print(myreduce(maxi,L))
print(myreduce(conc,L))
#CHANGE AT HOME
'''


#Write a program to print the table of the given number using the generator.

n = int(input())
L = (x*n for x in range(1,11))
print(list(L))