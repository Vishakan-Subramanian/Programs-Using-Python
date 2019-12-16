print("Enter 10 student names: ")
lst=[]
for i in range(0,10):
 val=raw_input("Enter the name: ")
 lst.append(val)

newname=raw_input("Enter another name that you wish to add to the list: ")
lst.append(newname)

print(lst)

k=0
term=raw_input("Enter a name you wish to search for in the list: ")
for j in range(0, len(lst)):
 if(lst[j]==term):
  print "The name that you searched for was present in the index of ",j
  k+=1
if(k==0):
 print "The name was not found."
