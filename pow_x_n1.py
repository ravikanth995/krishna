class power:
    def pow(self,x,n):
        print("pow(",x,",",n,")=",x**n)
     #   print("pow(",x,",",n,")=",x**n)


p=power()
x=int(input("Enter  X Number:"))
n=int(input("Enter Number:")) 
p.pow(x,n)       