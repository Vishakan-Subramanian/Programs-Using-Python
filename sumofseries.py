print "To find the sum of 1 + x^2 + x^4 +...+x^n"
x = int(input("Enter the value of x in the series."))
n = int(input("Enter the no. of terms in the series."))
if(x==1):
 print "The sum of the series is: ",n
else:
 y=x**2
 sum= ((y**n)-1)/(y-1)
 print "The sum of the series is: ",sum 
