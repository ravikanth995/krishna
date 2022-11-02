from typing import Counter


class student:
    college='Govt. degree college'
    Counter=0
    def __ini__(self, name, age):
        self.name=name
        self.age=age
        student.counter=student.counter+1

    def msg(self):
        print(self.name+''+self.age) 

    @classmethod
    def obj_count(cls):
        return cls.counter

print(student.college)
s1=student('Ravikanth','22')
s2=student('kanth','24') 
student.obj_count()
print(student.obj_count())                 