bp=float(input("Enter the basic pay amount"))
hra=bp*0.2
da=bp*0.4
ded=1200
gross=bp+hra+da
net=gross-ded
print "The net salary is ",net

