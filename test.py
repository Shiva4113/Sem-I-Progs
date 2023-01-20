lst=[1,2,3,4]
lst1=[11,22,33]
a=zip(lst,lst1)
x, y=zip(*list(a)) # unpacking operation
print(x, y)
