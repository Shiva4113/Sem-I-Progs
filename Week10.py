#PROG1
'''L2 = list(input().split())
L1 = list(map(int,list(input().split())))
print((max(L1),L2[L1.index(max(L1))]))'''
#PROG2
'''D = {'A':'fruit','B':'Veg','C':'Mammal','M':"Mammal","Banana":"fruit"}
S = set(D.values())
D1 = {}
for i,j in D.items():
    if j not in D1.keys():
        D1[j] = [i]
    else:
        D1[j].append(i)
print(D,D1,sep="\n")'''
#PROG3
'''def is_square(x):
    if x**0.5 == int(x**0.5)+0.0:
        return True
    return False
def is_even(x):
    if x%2 == 0:
        return True
    return False
#a
n = int(input())
if is_square(n) == True:
    print('Perfect Square')
#b
B1,B2 = [],[]
for i in range(n):
    if is_square(i) == True and is_even(i) == True:
        B1.append(i)
for i in range(n):
    if is_square(i) == False and is_even(i) == True:
        B2.append(i)
print("Numbers which are square and even:",B1)
print("Numbers which are square but not even:",B2)'''
#PROG4
'''def encrypt(s):
    s1=''
    for i in s:
        s1+=chr(ord('a')+ord('z')-ord(i))
    return s1
st = input()


print(encrypt(st))'''
#PROG4 - 2
'''def encrypt(s):
    s1 = ''
    for i in s:
        if i=='z':
            s1+='a'
        else:
            s1+=chr(ord(i)+1)
    return s1
print(encrypt('abcdefghijklmnopqrstuvwxyz'))'''

#PROG5
'''
def idm(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                print(1,end = '\t')
            else:
                print(0,end = '\t')
        print()
    return ''
def tm(n):
    print("Lower Tm")
    for i in range(n):
        for j in range(n):
            if i>=j:
                print(1,end = '\t')
            else:
                print(0,end = '\t')
        print()
    print("\nUpper TM")
    for i in range(n):
        for j in range(n):
            if i<=j:
                print(1,end = '\t')
            else:
                print(0,end = '\t')
        print()
    return ''
n = int(input())
print(idm(n))
print("\n\n",tm(n))'''