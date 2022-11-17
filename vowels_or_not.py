word=input("Enter a Word")
vowel='aeiouAEIOU'
flag=0
for i in vowel:
    if i in word:
        flag=1
        break
if flag==1:
        print("Word Contains Vowel")
else:
        print("Word Doesn't contain Vowel")    
      
