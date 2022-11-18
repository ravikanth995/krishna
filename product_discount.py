class product:
    def __init__(self,name,items,price):
        self.name=name
        self.items=items
        self.price=price

    def getprice(self,n):
        if n<10:
            print("Regular price charged for your order")
            cost=n*self.price
            print("if you place above 9 items you get 10% discount")
            print("if you place above 99 items you get 20% discount") 
        elif n>=10 and n<100:
            print("10% discount is applied for your orders") 
            cost=n*self.price
            discount=(cost*10/100)
            finalcost=cost-discount
            print("Actual Cost:", cost)
            print("10% discount:", finalcost)
            print("Cost after 10% discount:", discount)
            print("if you place above 99 items you get 20% discount")
        else:
            print("20% discount is applied for your orders")
            cost=n*self.price
            discount=(cost*20/100)
            finalcost=cost-discount
            print("Actual Cost:", cost)
            print("20% discount:", discount)
            print("Cost after 20% discount:", finalcost)

    def my_purchase(self,n):
        if n<10:
            print("Regular price is charged for your orders")
            cost=n*self.price
            print("Final Cost:", cost)
        elif (n>=10) and (n<100):
            print("10% discount is applied for your orders")
            cost=n*self.price
            discount=(cost*10/100)
            finalcost=cost-discount
            print("Actual Cost is :", cost)
            print("10% discount :", discount)
            print("Final Cost after 10% discount", finalcost)
            print("20% Discount is applied for your orders")
            cost-n*self.price
            discount=(cost*20/100)
            finalcost=cost-discount
            print("Actual cost:", cost)
            print("20% Discount:", discount)
            print("Final Cost after 20% discount", finalcost)
p=product("Pen",200,5)
n=int(input("Enter Number of Pens you want to buy"))
p.getprice(n)
n=int(input("Enter Number of pens you want to buy:")) 
p.my_purchase(n)           

