def look(d,v):
 item=d[v]
 return item

d=dict()
print("Enter the state name and its dish: ")
n=int(input("Enter the no. of states: "))

for i in range(0,n):
 st=raw_input("Enter the state name: ")
 di=raw_input("Enter the dish name: ")
 d[st]=di

print("Searching a dish")

state=raw_input("Enter the state: ")
dish=look(d,state)
print("The dish ",dish," belongs to the state: ",state)
