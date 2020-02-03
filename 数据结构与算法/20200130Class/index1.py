#测试私有属性

class Employee:
    def __init__(self,name,age):
        self.name=name
        self.__age=age#私有属性

    def __work(self):
        print("好好学习，天天向上")


e=Employee("李敏",21)
print(e.name)
print(e._Employee__age)
#print(e.age)

# e._Employee__work()