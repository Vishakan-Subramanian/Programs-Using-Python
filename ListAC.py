def Alias(ls):
 lst1=ls
 lst1.append("new")
 lst1.sort()
 print(lst1)

def Clone(ls):
 lst1=ls[:]
 lst1.append("new")
 lst1.sort()
 print(lst1)
lst=[]
n=int(input("Enter the limit of numbers: "))
for i in range(0,n+1):
 lst.append(i)
print(lst)
Alias(lst)
Clone(lst)
