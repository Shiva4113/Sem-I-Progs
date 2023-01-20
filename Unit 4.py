#USE LIST COMPREHENSION FOR THE FOLLOWING
'''
1. Form a list of strings made of the first and last characters from a given list of words, if the length of string is greater than or equal to 3.
2. Count the number of spaces in a string
3. Find all numbers which are odd and which are palindromes between a pair of numbers 20 and 100(both inclusive).
4. Create a list of numbers and a list of strings, both of the same size.
combine 2 lists to make a list of tuples.
5. Form a list of strings made of the first 2 and last 2 characters from a given list of words if the length of string is greater than 4
6. Find and display the intersection of 2 lists'''
#1
'''st = list(input().split())
L = [x[0]+x[-1] for x in st if len(x)>=3]
print(L)'''
#2
'''st = list(input())
L =  [ x for x in st if x == ' ' ]
print(len(L))'''
#3
'''L = [x for x in range(20,101) if str(x)==str(x)[::-1] and x%2!=0]
print(L)'''
#4
'''N = tuple(map(int,list(input().split())))
S = tuple(input().split())
L = [(x,y) for x,y in list(zip(N,S))]
print(L)'''
#5
'''st = list(input().split())
L = [x[0]+x[1]+x[-1]+x[-2] for x in st if len(x)>4]
print(L)'''
#6 
'''L1 = list(input().split())
L2 = list(input().split())
L = [x for x,y in list(zip(L1,L2)) if x == y]
print(L)'''