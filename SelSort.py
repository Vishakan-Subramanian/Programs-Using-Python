n=int(input("Enter the no. of elements in the list. "))
A=[]
for i in range(0,n):
 x=int(input("Enter a number: "))
 A.append(x)

for i in range(len(A)):
    min = i
    for j in range(i+1, len(A)):
        if A[min] > A[j]:
            min = j        
    A[i], A[min] = A[min], A[i]

print(A)
