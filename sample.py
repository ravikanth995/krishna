class Vehicle:
    def __init__(self,model,mileage,price):
        self.price=price
        self.model=model
        self.mileage=mileage
        self.price=price
    def showData(self):
        print(f"model : {self.model}") 
        print(f"price : {self.price}")
        print(f"mileage : {self.mileage}")
class Bike(Vehicle):
    def __init__(self,model,mileage,price,tyre,cc):
        super().__init__(model,mileage,price)
        self.cc=cc
        self.tyre=tyre
    def showDetails(self):
        super().showData()
        print(f"CC :{self.cc}")
        print(f"tyres: {self.tyre}")
    # Method of derived class
    def rating(self):
        print("4 Star")
class Car(Bike,Vehicle):
    def rating(self):
        print("5 Star")
Bajaj=Bike("Dommar",40,145000,2,500)
print("-"*30) 
Tata=Car("Safari",25,80000,7,2000)
Bajaj.showDetails()
Bajaj.rating()
print("-"*30)
Tata.showDetails()
# Bajaj.showData()
Tata.rating()
print("-"*30)
