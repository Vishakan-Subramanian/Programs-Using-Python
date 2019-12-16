jee=[]
neet=[]
common=[]
jeeo=[]
neeto=[]

n= int(input("Enter the no. of students who have passed JEE: "))
for i in range(0,n):
 jee.append(raw_input("Enter the name: "))

m= int(input("Enter the no. of students who have passed NEET: "))
for i in range(0,m):
 neet.append(raw_input("Enter the name: "))


if(m>=n):
 for i in range(0,m):
  if(neet[i] in jee):
   common.append(neet[i])
else:
  for i in range(0,n):
   if(jee[i] in neet):
    common.append(jee[i])

for i in range(0,n):
  if(jee[i] not in common):
   jeeo.append(jee[i])

for i in range(0,m):
  if(neet[i] not in common):
   neeto.append(neet[i])

print "The students who have qualified both exams are: "
print(common)

print "The students who have qualified only JEE are: "
print(jeeo)

print "The students who have qualified only NEET are: "
print(neeto)

print "The students who have written both exams are: "
print(jeeo+neeto+common)
