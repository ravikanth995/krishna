#String Functions
#Count Built-in Function
#string.count(substring, start, end)
 
#Sub-string = String whose count is to be found
#Start= Starting index within the String where search starts
# end=optional

# txt=" I love, my India"
# x=txt.count("love")
# print(x) 

# txt="I love my India, I love Upanishad, i love Buddha"
# x=txt.count("love")
# print(x)

# txt="om mangalam, Bhagvan vishnu, om mangalam garud-adhvaja"
# x=txt.count("om")
# print(x)

# txt="yastu sarvani bhutani aatma-yen-anupashyati, sarvabhuteshu cha-atman tato na vijugupsate"
# x=txt.count("tato")
# print(x)

# txt="om shanti, om shanti, om shanti"
# x=txt.count("om")
# print(x)

# txt="i love python, i love java"
# x=txt.count("love")
# print(x)

# txt="everything is made of me, but i am not in them"
# x=txt.count("me")
# print(x)

# txt="pure chetna, pure chetna"
# x=txt.count("pure")
# print(x)

#find built-in Functions
#str.find(sub, start, end)
 #if start and end index is not provided then by default it takes 0 and length as -1
# txt="i lob u"
# x=txt.find("i")
# print(x)

# txt="i lob u "
# x=txt.find("u")
# print(x)

# txt="it takes nonne"
# x=txt.find("")
# print(x)

#rfind Built-in Functions
#Last occurance of the specified value
#string.rfind()
# txt=" i love my India"
# x=txt.rfind("i")
# print(x)

#capitalize  it coverts first latter of string to capital
#str.capitalize()
# txt= "a mine girl"
# x=txt.capitalize()
# print(x)

# txt="a hi bro"
# x=txt.capitalize()
# print(x)

#title built-in function
#str.title()
# txt="a 2mine is 3a 8god"
# x=txt.title()
# print(x)

# txt="welcomme 2my 3lord"
# x=txt.title()
# print(x)

#lower built-in functions
# txt="A IS A WORD"
# x=txt.lower()
# print(x)

#swapcase
# txt= "hOLLO mY nAME iS rAVI kANTH"
# x=txt.swapcase()
# print(x)

# a="HELLO"
# b="My"
# c="22 Names"
# d="This Is Pandu"
# print(a.istitle())
# print(b.istitle())
# print(c.istitle())
# print(d.istitle())

# a="JELLO"
# b="Hello"
# c="22 Name"
# d="Hi My Name Is ?"
# print(a.istitle())
# print(b.istitle())
# print(c.istitle())
# print(d.istitle())

#Reaplace built-in function
#the replace method replaces specified phrase with another specified phrase
#str.replace(oldvalue, newvalue, count)
# txt="My favourite fruit is apple"
# x=txt.replace("apple","vastunna")
# print(x)

# txt="My name is Kheema"
# x=txt.replace("Kheema", "Ravikanth")
# print(x)

# txt="My Name is Ravi"
# x=txt.replace("Ravi","KAnth")
# print(x)

# txt="Hi Bro.. Rajnikanth"
# x=txt.replace("Rajnikanth", "Ravikanth")
# print(x)

#Strip built-in Funnction
#str.strip()
# txt="   hi    "
# x=txt.strip(" ")
# print(x)
# str1="     Hi..      "
# x=str1.strip()
# print(x, "Is my Favourite")

# str1="Hello..."
# x=str1.strip()
# print(x, "My Man")

# txt="Hello"
# x=txt.strip()
# print(x, "Is My Fractuante")

#lStrip built-in function
#str.lstrip()
# txt="       hi"
# x=txt.lstrip()
# print("Hi bro",x,"NAmse")

# txt="    Hi"
# x=txt.lstrip()
# print("Namaste !",x,"WElcomes")

# txt="                    Ravikanth"
# x=txt.lstrip()
# print("Hi Bro...",x,"Welcomes You")

# txt="     Vastunaa"
# x=txt.lstrip()
# print("My Favourite is",x,"Song")

#rStrip() built-in function
# txt="ravikanth                               "
# x=txt.rstrip()
# print("Hi",x,"WElcome")

# txt="Ravikanth       "
# x=txt.rstrip()
# print("Hi",x,"Listening this")

#Partion() built-in function
# txt=" for me this"
# x=txt.partition("me")
# print(x)

# txt="for me above"
# x=txt.partition("m")
# print(x)

#Join built-in function
#str.join(iterable)
# myTuple=("aaaa","bbbb","cccc")
# x="@".join(myTuple)
# print(x)

# str1=("Hi","bro","how are you")
# x=" ".join(str1)
# print(x)

# str1=("Prajna","chetna","brahmam")
# x=" ".join(str1)
# print(x)

# myDict={"name":"ravi","country":"India"}
# my_separator="####"
# x=my_separator.join(myDict)
# print(x)

# myDict={"Name":"Ravi","Country":"India"}
# my_separator="##"
# x=my_separator.join(myDict)
# print(x)

# myDict={"India":"Country","Ravikanth":"Name"}
# separator=" "
# x=separator.join(myDict)
# print(x)

# myDict=("My","name","is","ravikanth")
# separator=" "
# x=separator.join(myDict)
# print(x)

#isspace()
# str1="   "
# x=str1.isspace()
# print(x)

# str1="  s  "
# x=str1.isspace()
# print(x)

# str1="ravikanthchauhan"
# x=str1.isalpha()
# print(x)

# str1="ravi kanth"
# x=str1.isalpha()
# print(x)

#isdigit()
# str1="\u0030" #unicode for 0
# str2="\u00B2"  #unicode for power
# print(str1.isdigit())
# print(str2.isdigit())

# str1="Num12"
# x=str1.isalnum()
# print(x)

#startswith()
# str1="Hello, Hi How are you"
# x=str1.startswith("Hello")
# print(x)

# str1="hello, Hi"
# x=str1.startswith("hello")
# print(x)

#endswith
str1="Hi.., How are you"
x=str1.endswith("you")
print(x)