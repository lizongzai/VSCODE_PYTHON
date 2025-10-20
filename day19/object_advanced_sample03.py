class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

stu = Student('王大锤', 20)
print(stu.name)  # 王大锤
stu.name = '李小白'
print(stu.name)  # 李小白