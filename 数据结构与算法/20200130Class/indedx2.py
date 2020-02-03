#@property修饰器的使用
# 针对的是私有变量

class Student():
    def __init__(self,name,school,age):
        self.name=name
        self.school=school
        self.__age=age


    # def getAge(self):
    #     return self.age
    # def setAge(self,age):
    #     self.age=age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        self.__age=age

s=Student("詹士","师大",21)
#print(s.getAge())
s.age=10
print(s.age)
