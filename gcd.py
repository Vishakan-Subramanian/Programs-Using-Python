a= int(input("Enter a number"))
b=int(input("Enter another number"))
r=1
if(a<b):
 a,b=b,a
while(r!=0):
 r=a%b
 a=b
 b=r
print "The GCD of the given two numbers is: ",a
