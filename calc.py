a= float(input("Enter a number "))
b= float(input("Enter another number "))
opn=  input("Enter the math operation that you wish to perform( 1-(+),2-(-),3-(*),4-(/) ) ")
if(opn==1):
           print "The result is ",(a+b)
elif(opn==2):
             print "The result is ",(a-b)
elif(opn==3):
             print "The result is ",(a*b)
elif(opn==4):
             print "The result is ",(a/b)
else:
     print "The operation you specified cannot be performed."
