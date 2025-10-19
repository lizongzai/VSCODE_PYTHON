# 父类（基类）
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"你好，我叫 {self.name}，今年 {self.age} 岁。")

# 子类（派生类）Student 继承自 Person
class Student(Person):
    def __init__(self, name, age, student_id):
        # 使用 super() 调用父类的初始化方法
        super().__init__(name, age)
        # 添加子类特有的属性
        self.student_id = student_id

    # 重写父类的方法
    def introduce(self):
        # 可以先调用父类的方法
        # super().introduce()
        # 然后添加子类特有的行为
        print(f"你好，我是学生 {self.name}，学号是 {self.student_id}。")
        
        
# 另一个子类
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    # 重写 introduce 方法
    def introduce(self):
        print(f"大家好，我是 {self.subject} 老师，我叫 {self.name}。")

# 多态的体现
def person_intro(person):
    """这个函数接收一个 Person 类型的对象"""
    person.introduce()

# 创建不同类的对象
a_person = Person("普通人", 30)
a_student = Student("钱七", 19, "S1002")
a_teacher = Teacher("孙老师", 35, "数学")

# 传入不同的对象，调用相同的方法，但行为不同
person_intro(a_person)   # 输出：你好，我叫 普通人，今年 30 岁。
person_intro(a_student)  # 输出：你好，我是学生 钱七，学号是 S1002。
person_intro(a_teacher)  # 输出：大家好，我是 数学 老师，我叫 孙老师。

# 使用继承
# student = Student("赵六", 18, "S1001")
# student.introduce()  # 调用的是子类重写后的方法
# # 输出：你好，我是学生 赵六，学号是 S1001。