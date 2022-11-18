# class product:
#     def __init__(self, name, items, price):
#         self.name=name
#         self.items=items
#         self.price=price

#     def get_price(self,n):
#         if n<10:
#             print("Regular Price is Charged for your orders")
#             cost=n*self.price
#             print("If you place above 9 items you get 10% discount") 
#             print("if you place above 99 items you get 20% discount")
#         elif n>10 and n<100:
#             print("10% discount is applied for your orders")
#             cost=n*self.price
#             discount=(cost*10)/100 
#             finalcost=cost-discount
#             print("Actual Cost:", cost)
#             print("10% discount:", finalcost)
#             print("If you place above 99 items you get 20% discount")
#         else:
#             print("20% discount is applied for your orders") 
#             cost=n*self.price
#             discount=(cost*20)/100
#             finalcost=cost-discount
#             print("Actual Cost:",cost)
#             print("20% discount:", discount)
#             print("Cost after 20% discount:", finalcost)

#     def my_purchase(self,n):
#         if n<10:
#             print("Regular price is charged for your orders")
#             cost=n*self.price
#             print("Final cost:",cost)
#         elif n>=10 and n<100:
#             print("10% discount is applied for your orders")
#             cost=n*self.price
#             discount=(cost*10)/100
#             finalcost=cost-discount
#             print("Actual Cost:", cost)
#             print("10% discount:", discount)
#             print("Final cost after 10% discount:", finalcost)
#             print("20% discount is applied for your orders")
#             cost=n*self.price
#             discount=(cost*20)/100
#             finalcost=cost-discount
#             print("Actual cost:", cost)
#             print("20% discount:", discount)
#             print("Final cost:", finalcost)

# p=product("Table", 200, 7)
# n=int(input("Enter Number of pens you want to buy:"))
# p.get_price(n)
# n=int(input("Enter Number of Tables you want to buy"))
# p.my_purchase(n)





class product:
    def __init__(self,name,items,price):
        self.name=name
        self.items=items
        self.price=price

    def get_price(self,n):
        if n<10:
            print("Regular price is charged for your order")    
            cost=n*self.price
            print("If you place above 9 items you get 10% discount")
            print("if you place above 99 items you get 20% discount")
        elif n>=10 and n<100:
            print("10% discount is applied for your orders")
            cost=n*self.price
            discount=(cost*10)/100
            finalcost=cost-discount
            print("Actual cost:", cost)
            print("10% discount:", finalcost)
            print("Cost after 10% discount:", discount)
            print("If you place above 99 items you get 20% discount")
        else:
            print("20% discount is applied for ypur orders")
            cost=n*self.price
            discount=(cost*20)/100
            finalcost=cost-discount
            print("Actual Cost:", cost) 
            print("20% discount:", discount)
            print("Cost aftter 20% discount:",finalcost)

    def my_purchase(self,n):
        if n<10:
            print("Regular price is charged for your orders")
            cost=n*self.price
            print("Final cost:", cost)

        elif n>=10 and n<100:
            print("10% discount is applied for your order")
            cost=n*self.price
            discount=(cost*10)/100
            finalcost=cost-discount
            print("Actual price:", cost) 
            print("10% discount:", discount)
            print("Final cost after 10% discount:", finalcost)
            print("20% discount is applied for your orders")
            cost=n*self.price
            discount=(cost*20)/100
            finalcost=cost-discount
            print("Actual Cost:", cost)
            print("20% discount:", discount)
            print("Final Cost after 20% discount:", finalcost)


p=product("Chair", 200, 9.8)
n=float(input("Enter Number of pens you want to purchase"))
p.get_price(n)
n=float(input("Enter Number of Pens you want to buy"))
p.my_purchase(n)