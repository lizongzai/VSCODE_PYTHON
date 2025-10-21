from abc import ABC, abstractmethod

class Person(ABC):
    """人（抽象基类，定义接口）"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}正在吃饭.')

    def sleep(self):
        print(f'{self.name}正在睡觉.')

    @abstractmethod
    def work(self):
        """抽象方法：不同角色有不同的工作"""
        pass


class Student(Person):
    """学生类"""

    def __init__(self, name, age):
        super().__init__(name, age)

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')

    def work(self):
        print(f'{self.name}的工作是学习和完成作业.')


class Teacher(Person):
    """老师类"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title

    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}.')

    def work(self):
        print(f'{self.name}{self.title}的工作是教授课程和指导学生.')


# 测试多态效果
people = [
    Student('白元芳', 21),
    Teacher('武则天', 35, '副教授')
]

for p in people:
    p.eat()
    p.work()  # 多态调用，不同子类表现不同
