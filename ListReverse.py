def rev(lst):
 lstr=[]
 for i in range(1,len(lst)+1):
  lstr.append(lst[-i])
 print(lstr)


lst=[]
n=int(input("Enter the no. of values in the list: "))
for i in range(0,n):
 lst.append(raw_input("Enter the element: "))
rev(lst)

