n=int(input("Enter the range of values: "))
lst=[]
even=[]
odd=[]
for i in range(0,n):
 lst.append(i)

for i in range(0,n):
 if(lst[i]%2==0):
  even.append(lst[i])
 else:
  odd.append(lst[i])

print "The even numbers list:"
print(even)

print "The odd numbers list:"
print(odd)
