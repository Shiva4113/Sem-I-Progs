#PROG 1
'''class Matrix:
    def populate():
        L1 = []
        n = int(input("ORDER OF MATRIX:"))
        for i in range(n):
            L1.append([])
            for j in range(n):
                N = int(input("ELEMENT OF MATRIX:"))
                L1[i].append(N)
        return L1
    def add(m1,m2):
        
        res = []
        for i in range(len(m1)):
            res.append([])
            for j in range(len(m1)):
                res[i].append(m1[i][j]+m2[i][j])
        return res
    def display(L):
        for i in range(len(L)):
            for j in range(len(L)):
                print(L[i][j],end = ' ')
            print()
#MAIN

L1 = Matrix.populate()
L2 = Matrix.populate()
SM=Matrix.add(L1,L2)
print("FIRST MATRIX:");Matrix.display(L1)
print("SECOND MATRIX:");Matrix.display(L2)
print("SUM OF MATRICES:");Matrix.display(SM)

'''
#PROG 2
from datetime import *
class Bill:
    def items(nitems):
        i = 1
        d= {}
        iname = input("ENTER ITEM NAME:")
        icost = float(input("ENTER COST OF ITEM:"))
        while i<nitems:
            d[i].extend([iname,icost])

#MAIN
date = datetime.now()
CustomerName = input()
nitems = int(input())
