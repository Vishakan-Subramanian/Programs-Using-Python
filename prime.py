n = int(input("Enter a number"))
m=(n/2)+1
c=0;
for i in range( 2,m):
 if((n%i)==0):
  c+=1
if(c==0):
 print "The given number is prime."
else:
 print "The given number is not prime."
