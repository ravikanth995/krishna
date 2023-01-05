#File Handling
# fileObject=open("GCD.py","w")
# print("File name:",fileObject.name)
# print("file mode:", fileObject.mode)
# print("Is File readable :",
#      fileObject.readable())
# print("Is File Writable: ",
#      fileObject.writable())
# print("is file closed:", fileObject.closed)
# fileObject.close()
# print("Is File Closed:",fileObject.closed)          

# FileObject=open("FileObject.py","w")
# print("File Name:",FileObject.name)
# print("File Mode:",FileObject.mode)
# print("Is File Readable:",FileObject.readable())
# print("IS File Writable:",FileObject.writable())
# print("If file closed:",FileObject.closed)
# FileObject.close()
# print("Is File Closed:",FileObject.closed)

# fileObject=open("FileObject.py","w")
# print("File Name:",fileObject.name)
# print("File Mode:",fileObject.mode)
# print("is file readable:",fileObject.readable())
# print("Is File Writable :",fileObject.writable())
# print("Is File Closed:",fileObject.closed)
# fileObject.close()
# print("Is File Object closed:",fileObject.closed)

# fileObject=open("FileObject1.py","w")
# print("File Name:", fileObject.name)
# print("File Mode:",fileObject.mode)
# print("Is file readable:",fileObject.readable())
# print("is file writable:",fileObject.writable())
# print("Is File closed:",fileObject.closed)
# fileObject.close()
# print("is file closed:",fileObject.closed)

#After file closure
# file=open("GCd.py","r")
# print("File name",file.name)
# file.close()
# print("Is file closed:",file.closed)
# print("File read:",file.read())

# f=open("example_file.py","r")
# print(f.read())
# f=open("example_file.py","r")
# print(f.read(5))

# f=open("example_file.py","r")
# print(f.readline())
# f.close()

# f=open("example_file.py","r")
# for x in f:
#     print(x)
#     print(f.read())
# f.close()    

#Writing on to a file
# fileObject=open("test_file.txt","w")
# fileObject.write("Hi Man.. How are you")
# fileObject.close()

# try:
#     fileObject=open("test_example.txt","w")
# finally:
#     fileObject.close()

# fileObject=open("test_file.txt","r")
# data=fileObject.read()
# print(data)
# fileObject.close()

# fileObject=open("test_file.txt","r")
# data=fileObject.read()
# print(data)
# fileObject.close()

# fileObject=open("write.txt","r")
# data=fileObject.read()
# print(data)
# fileObject.close()

# fileObject=open("write.txt","r")
# data=fileObject.read()
# print(data)
# fileObject.close()

# fileObject=open("write.txt","r")
# data=fileObject.read()
# print(data)
# fileObject.close()

# fileObject=open("write.txt","r")
# data=fileObject.read()
# print(data)
# fileObject.close()

# fileObject=open("write.txt","r")
# data=fileObject.readline(7)
# print(data)
# fileObject.close()

# fileObject=open("write.txt","r")
# data=fileObject.readline(12)
# print(data)
# fileObject.close()

# fileObject=open("write.txt","r")
# data=fileObject.readlines(10)
# print(data)

# fileObject=open("write.txt","r")
# data=fileObject.readlines(10)
# print(data)
# fileObject.close()

# fileObject=open("write.txt","r")
# data1=fileObject.readline()
# data2=fileObject.readline()
# data3=fileObject.readline()
# print(data1)
# print(data2)
# print(data3)
# fileObject.close()

# fileObject=open("write.txt","r")
# print(fileObject.readlines())

# fileObject=open("write.txt","r")
# print(fileObject.readlines())

#Write()
# fileObject=open("write.txt","a")
# fileObject.write("\nHello main kaun hu??\n")
# fileObject.close()
# fileObject=open("write.txt","r")
# print(fileObject.read())
# fileObject.close

# fileObject=open("write.txt","a")
# fileObject.write("\n Nainam Chidanti Shastrani\nNainam dahati pawahka\nna chainam kledayanpappo\nna shoshayati marutah")
# fileObject.close()
# fileObject=open("write.txt","r")
# print(fileObject.read())
# fileObject.close()

#writelines()
#fileObject.writelines(list)
# fileObject=open("hello.txt",'w')
# lines_of_text=["a line of text","another line of text","a third line of text"]
# fileObject.writelines(lines_of_text)
# fileObject.close()

# fileObject=open("hello1.txt",'w')
# lines=["Hi Gustakh Miyaa","\nKya Karre","\nkuch nhi miyaa jaan","\nok Miyaa Jaan"]
# fileObject.writelines(lines)
# fileObject.close()
# fileObject=open("hello1.txt","r")
# data=fileObject.read()
# print(data)
# fileObject.close()

# fileObject=open("hello1.txt",'w')
# lines=["Arre..","\nKya hua","\nMaine na yeh jaan","\nArre re","kuch ho gaya"]
# fileObject.writelines(lines)
# fileObject.close()
# fileObject=open("hello1.txt",'r')
# data=fileObject.read()
# print(data)
# fileObject.close()

# fileObject=open("hello1.txt",'w')
# lines=["Arre..","\nKya hua","\nMaine na yeh jaan","\nArre re","kuch ho gaya"]
# fileObject.writelines(lines)
# fileObject.close()
# fileObject=open("hello1.txt","r")
# data=fileObject.read()
# print(data)
# fileObject.close()

#tell() used to get the position of the file handle. returns the current position of the file object
#fileObject.tell()

# fileObject=open('write.txt','r')
# print("File position",fileObject.tell())
# print("1st Line",fileObject.tell())
# print("FileObject:",fileObject.tell())
# print("2nd Position:",fileObject.tell())
# print("file position:",fileObject.tell())
# fileObject.close()

#seek() : method sets the current file position to set the current file stream position
# fileObject.seek(offset)
# fileObject=open("hello.txt",'r')
# print("File Position:",fileObject.tell())
# print(fileObject.readline())
# fileObject.seek(4)
# print(fileObject.readline())
# print("File Position:",fileObject.seek(4))


