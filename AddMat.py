def printmat(matrix):
 for i in range(len(matrix)):
  for j in range(len(matrix[0])):
   print(matrix[j][i], end="\t")
  print ("\n")


n=int(input("Enter the no. of rows in the matrix: "))
m=int(input("Enter the no. of columns in the matrix: "))

print("Enter the elements in the first matrix.")
x=[[0 for i in range(0,n)] for j in range(0,m)]

for i in range(0,len(x)):
 for j in range(0,len(x[0])):
  x[i][j]=int(input("Enter the element: "))

print("Enter the elements in the second matrix.")
y=[[0 for i in range(0,n)] for j in range(0,m)]

for i in range(0,len(y)):
 for j in range(0,len(y[0])):
  y[i][j]=int(input("Enter the element: "))


res=[[x[i][j]+y[i][j] for i in range(0,n)] for j in range(0,m)]

printmat(res)
