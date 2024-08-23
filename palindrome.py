word=input("enter a word : ")
l=len(word)
palindrome=0
for i in range(int(l/2)):
    if word[i]!=word[l-i-1]:
        palindrome=1

if palindrome==0:
  print(word + "is a palindrome")
else:
  print(word + "is not a plaindrome")
  
    
        
