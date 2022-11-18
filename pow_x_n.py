class power:
    def pow(self,x,n):
        print("pow(",x,",",n,")=",x**n)

p=power()
x=int(input("Enter X value"))
n=int(input("Enter n Value"))
p.pow(x,n)
