class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say__age(self):
        print("年龄、年龄，this is 秘密～")

class Student(Person):
    def __init__(self,name,age,score):
        Person.__init__(self,name,age)
        self.score=score

s=Student("战三",21,99.9)# Object -> Person ->Student
print(Student.mro())
print(s)
