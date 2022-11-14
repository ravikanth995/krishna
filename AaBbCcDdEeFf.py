string1=input("Enter First String")
string2=input("Enter Second String")
if(len(string1)==len(string2)):
    print("Strings are of same length")
    result=""
    for i in range(len(string1)):
        result=result+(string2[i]+string1[i])
        print(result)
else:
    print("Strings are of same length")        