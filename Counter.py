def counter(d):
 A=[]
 d1=dict()
 A=d.values()
 B=[]
 for i in A:
  if i not in B:
   B.append(i)
 for j in A:
  if j not in d1:
   d1[j]=1
  else:
   d1[j]+=1
 print d1
 c=0
 C=d1.values()
 for k in C:
  if k>1:
   c=c+1  
 print(c," values appear more than once in the dictionary,")

a={'one':1,'two':2,'three':3,'four':4,'five':1,'six':2,'seven':3,'eight':3}
counter(a)



