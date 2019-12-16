word=raw_input("Enter a word: ")
enc=""
for achar in word:
 chno=ord(achar)
 chno+=3
 ch=chr(chno)
 enc=enc+ch
print "The encrypted word is: ",enc
