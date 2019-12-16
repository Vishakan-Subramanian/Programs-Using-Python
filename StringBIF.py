choice = int(input("Enter your choice: 1- Length of a word, 2- No. of occurrences of a group of characters in a given word, 3- Reverse of a word, 4- Replace a letter in a word by $, 5- Check whether given word is a Palindrome"))

if (choice==1):
 word=raw_input("Enter a word of your choice: ")
 wl=len(word)
 print "The length of the given word is: ",wl

elif choice==2 :
  word=raw_input("Enter a word: ")
  sub=raw_input("Enter a word/letter to check for occurrences in the given word: ")
  a=word.count(sub)
  print "The count is: ",a

elif(choice==3):
 word=raw_input("Enter a word: ")
 x="".join(reversed(word))
 print x

elif(choice==4):
 word=raw_input("Enter a word: ")
 c=raw_input("Enter a character to replace with $: ")
 x=word.replace(c, "$")
 print x

elif(choice==5):
 word=raw_input("Enter a word: ")
 x="".join(reversed(word))
 if(x==word):
  print "The given word is a palindrome."
 else:
  print "The given word is not a palindrome."

else:
 print "The entered choice does not exist."
