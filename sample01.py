class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def massege(self):
        print(self.name+" "+" has got",self.marks)
    @classmethod
    def get_per(cls,name,marks):
        return cls(name, str((int(marks)/600)*100))
    @staticmethod
    def get_age(age):
        if age<17:
            print("Adult belongs to School")
        else:
            print("Does not belong to School")
s1=Student("Ravi","24")
s2=Student.get_per("Ravi","400")
s2.massege()
Student.get_age(17)                    
