class Parent:
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
class Child(Parent):
    def __init__(self,name,age):
        Parent.__init__(self,name)
        self.age=age
    def get_Age(self):
        return self.age
class Grand_child(Child):
    def __init__(self,name,age,location):
        Child.__init__(self,name,age)
        self.location=location
    def getLocation(self):
        return self.location

ge=Grand_child("Ravikanth",59,"Chittapur")
print(ge.getName(),ge.get_Age(), ge.getLocation())        

