choice = int(input("Enter your choice: 1- Occurrence of a word/letter in a given word, 2- First occurrence from the end of the word, 3- Right Justification, 4- Capitalization of first word, 5- Check whether given word is alphanumeric"))

if(choice==1):
 word=raw_input("Enter a word of your choice: ")
 sub=raw_input("Enter a word/letter to check for occurrence in the given word: ")
 oc=word.find(sub)
 if(oc==-1):
  print "The word/letter does not occur in the given word!"
 else:
  print "The word/letter occurs in the given word at the index of: ",oc

elif(choice==2):
  word=raw_input("Enter a word of your choice: ")
  sub=raw_input("Enter a word/letter to check for first occurrence in the given word from the end: ")
  oc=word.rfind(sub)
  if(oc==-1):
   print "The word/letter does not occur in the given word!"
  else:
   print "The word/letter occurs in the given word at the index of: ",oc

elif(choice==3):
 word=raw_input("Enter a word: ")
 x=word.rjust(10)
 print x

elif(choice==4):
 word=raw_input("Enter a word: ")
 x=word.capitalize()
 print x

elif(choice==5):
 word=raw_input("Enter a word: ")
 x=word.isalnum()
 if(x==True):
  print "The given word consists of alphanumeric characters."
 else:
  print "The given word does not contain only alphanumeric characters."

else:
 print "The entered choice does not exist."
