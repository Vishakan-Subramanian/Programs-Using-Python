def histogram(s):
 d=dict()
 for c in s:
  if c not in d:
   d[c]=1
  else:
   d[c]+=1
 return d


def print_hist(h):
 for c in h:
  print(c,h[c])

print("To find the no. of times a character appears in a string.")

word=raw_input("Enter a word: ")
d=histogram(word)
print_hist(d)
