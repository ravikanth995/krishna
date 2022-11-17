file=open("temps.txt","w")
line=file.readlines()
file1=open("ftemps.txt","w")
for i in range(len(line)):
    c=line[i].strip()
    f=round((float(c)*1.8)+32,2)
    file1=write(str(f)+"\n")
file1.close()    