
a=float(input("Enter the co-efficient of the second degree variable in the equation"))
b=float(input("Enter the co-efficient of the first degree variable in the equation"))
c=float(input("Enter the constant value in the equation"))
d=((b**2)-(4*a*c))**0.5
value1=(-b+d)/(2*a)
value2=(-b-d)/(2*a)
print "The roots of the equation are " , value1 , value2

