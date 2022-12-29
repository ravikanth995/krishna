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

f=open("example_file.py","r")
for x in f:
    print(x)
    print(f.read())
f.close()    

