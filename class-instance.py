class student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def msg(self):
        print(self.name+''+self.age)

print('Object 1')
s1=student('Praveen', '23')
print(s1.name)
print(s1.age)
s1.msg()

print('Object 2')
s2=student('Ravikanth', '22')
print(s2.name)
print(s2.age)
s2.msg()
