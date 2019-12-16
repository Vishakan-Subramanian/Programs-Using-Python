def palindrome(word):
 rev=word[::-1]
 if(rev==word):
  print "The word is a palindrome!"
 else:
  print "The word is not a palindrome!"

word=raw_input("Enter a word: ")
palindrome(word)
