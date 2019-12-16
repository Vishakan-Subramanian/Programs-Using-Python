import string

choice = int(input("Enter your choice: 1- Check whether a character is in lowercase in given word, 2- Printing all octal and hexadecimal numbers"))

if(choice==1):
 x=0
 word=raw_input("Enter a letter of your choice: ")
 if(word in string.lowercase):
  x+=1
 if(x==0):
  print "The letter is not in lowercase!"
 else:
  print "The letter is in lowercase!"

elif(choice==2):
  print(string.octdigits)
  print(string.hexdigits)

else:
 print "The entered choice does not exist."
