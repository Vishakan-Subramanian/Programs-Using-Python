def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))


limit= int(input("Enter the limit upto which Fibonacci Sequence has to be generated. "))
for i in range(limit+1):
       print(fibo(i))

