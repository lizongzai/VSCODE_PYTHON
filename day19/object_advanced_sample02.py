class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

stu = Student('王大锤', 20)
print(stu.get_name())  # 王大锤