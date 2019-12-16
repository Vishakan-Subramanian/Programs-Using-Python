lst=[]
lstn=[]
n=int(input("Enter the no. of students in the course: "))
for i in range(0,n):
 lst.append(raw_input("Enter the student name: "))

news=raw_input("Enter the new student's name: ")
lst.append(news)

print "No. of students in the course are: ",len(lst)

lst.sort()

print "The first student: ", lst[0], " and the last student: ",lst[n]

m=int(input("Enter the no. of new students in the course: "))
for i in range(0,m):
 lstn.append(raw_input("Enter the student name: "))
lst=lst+lstn

lst.sort()

r=int(input("Enter the index of the new student: "))
n1=raw_input("Enter the name of the new student: ")
lst.insert(r,n1)

k=0
search= raw_input("Enter the student name to search for: ")
for i in range(0,len(lst)):
 if(lst[i]==search):
  k+=1
  print "The student was found with the index: ",i
if(k==0):
 print "The student was not found."
rem= raw_input("Enter the student name to remove: ")
lst.remove(rem)

print(lst)
