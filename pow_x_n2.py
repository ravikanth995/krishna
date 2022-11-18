class power():
    def pow(self,x,n):
        print("pow(",x,",",n,")=",x**n)

p=power()
x=int(input("Enter X value"))
n=int(input("Enter N value"))        
p.pow(x,n)