class Parent_Class:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def Employee_Details(self):
        return self.id, self.name
    def Employee_Check(self):
        if self.id>50000:
            return " Is valid Employee" 
        else:
            return "Invalid Employee" 
class Derived_Class(Parent_Class):
    def End(self):
        print("End of Program")

Employee1=Parent_Class("Ravikanth",1537199)
print(Employee1.Employee_Details(),Employee1.Employee_Check())

Employee2=Derived_Class("Employee 1", 1537198)
print(Employee2.Employee_Details, Employee2.Employee_Check())
