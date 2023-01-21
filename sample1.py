class vehicle:
    def __init__(self,model,mileage,price):
        self.price=price        
        self.model=model
        self.mileage=mileage
        self.price=price
    def showData(self):
        print(f"model : {self.model}")
        print(f"price : {self.price}")
        print(f"mileage : {self.mileage}")
class bike(vehicle):
    def __init__(self,model,mileage,price,tyre,cc):
        super().__init__(model,mileage,price)          
        self.cc=cc
        self.tyre=tyre
    def showDetails(self):
        super().showData()
        print(f"CC :{self.cc}")
        print(f"tyres: {self.tyre}") 
    def rating(self):
        print("4 Star")
class Car(bike,vehicle):
    def rating(self):
        print("5 Star")

Bajaj=bike("Chetak",40,120000,2,500)
Tata=Car("Tata Sumo",25,8000000,4,2000)
Bajaj.showDetails()
Bajaj.showData()
Bajaj.rating()
print("-"*40)
Tata.showDetails()
Tata.showData()
Tata.rating()