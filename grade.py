a= float(input("Enter English marks "))
b= float(input("Enter Math marks "))
c= float(input("Enter Python marks "))
d= float(input("Enter Physics marks "))
e= float(input("Enter Chemistry marks "))
avg=(a+b+c+d+e)/5
if(avg>=90):
            print "You have obtained A grade!"
elif((avg>=75)&(avg<90)):
                         print "You have obtained B grade!"
elif((avg>=60)&(avg<75)):
                         print "You have obtained C grade!"
else:
     print "You have obtained D grade!"
