word=raw_input("Enter a word: ")
sub=raw_input("Enter a letter to find its number of occurrences in the given word.")
val=0
for achar in word:
 if(achar==sub):
   val+=1
fo=word.index(sub)
print "The number of occurrences is/are: ",val, " and the first occurrence is at the index ",fo
