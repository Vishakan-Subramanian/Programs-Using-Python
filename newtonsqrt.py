n=int(input("Enter a number. "))
m=int(input("Enter the approximation limit. "))
sqrt=0
approx=0.5*n
for i in range((m+1)):
 sqrt=0.5*(approx + n/approx)
 approx= sqrt
print "The approximate square root of the number is: ",sqrt
