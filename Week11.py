#PROG1
'''def deco(fxn):
    def wrapper(n):
        print("My salary is $",end='')
        fxn(n)
    return wrapper

@deco
def day_earnings(number):
    print(number)
day_earnings(800)
day_earnings(500)
day_earnings(1000)'''

#PROG2
'''import datetime
def deco(fxn):
    def wrapper():
        if 7<=datetime.datetime.now().hour <22:
            fxn()
    return wrapper

@deco
def say_hello():
    print("Hello!")
say_hello()'''

#PROG3
'''authors = ['Rabindranath Tagore', 'Khushwant Singh', 'Vikram Chandra', 'Mulk Raj Anand', 'R K Narayan ', 'Jhumpa Lahiri']
print(sorted(authors,key=len))

def ln(s):
    return s.split()[-1]

print(sorted(authors,key=ln))'''

#PROG4
'''L=[("890","ram",(95,88,99)),("123","kishan",(90,98,99)),("567","arjun",(59,68,100))]
def name(s):
    return s[1]
names = sorted(L,key = name)
print(names)
#part2
def marks(s):
    return sum(s[2])
marksort = sorted(L,key = marks)
marksort.reverse()
print(marksort)'''