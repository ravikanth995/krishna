
fileObject=open("hello1.txt",'w')
lines=["Arre..","\nKya hua","\nMaine na yeh jaan","\nArre re","kuch ho gaya"]
fileObject.writelines(lines)
fileObject.close()
fileObject=open("hello1.txt",'r')
data=fileObject.read()
print(data)
fileObject.close()