# 父类（基类）
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"你好，我叫 {self.name}，今年 {self.age} 岁。")

    def have_birthday(self):
        """过生日，年龄增加1岁"""
        self.age += 1
        print(f"祝 {self.name} 生日快乐！现在 {self.age} 岁了。")

# 子类：学生
class Student(Person):
    def __init__(self, name, age, student_id, major):
        # 调用父类的构造函数
        super().__init__(name, age)
        # 添加子类特有的属性
        self.student_id = student_id
        self.major = major
        self.courses = []

    # 重写父类的方法
    def introduce(self):
        print(f"你好，我是学生 {self.name}，学号 {self.student_id}，"
              f"主修 {self.major}，今年 {self.age} 岁。")

    # 子类特有的方法
    def enroll_course(self, course_name):
        self.courses.append(course_name)
        print(f"{self.name} 已选课：{course_name}")

    def show_courses(self):
        if self.courses:
            print(f"{self.name} 的选课列表：{', '.join(self.courses)}")
        else:
            print(f"{self.name} 还没有选任何课程")

# 子类：老师
class Teacher(Person):
    def __init__(self, name, age, department, employee_id):
        super().__init__(name, age)
        self.department = department
        self.employee_id = employee_id

    def introduce(self):
        print(f"大家好，我是 {self.department} 的教师 {self.name}，"
              f"工号 {self.employee_id}。")

    def teach(self):
        print(f"{self.name} 老师正在授课...")

# 使用示例
if __name__ == "__main__":
    # 创建 Person 对象
    person1 = Person("张三", 25)
    person1.introduce()
    person1.have_birthday()
    print()

    # 创建 Student 对象
    student1 = Student("李四", 20, "2024001", "计算机科学")
    student1.introduce()
    student1.enroll_course("Python编程")
    student1.enroll_course("数据结构")
    student1.show_courses()
    print()

    # 创建 Teacher 对象
    teacher1 = Teacher("王教授", 45, "计算机学院", "T1001")
    teacher1.introduce()
    teacher1.teach()
    print()

    # 多态演示：不同类型的对象调用相同的方法
    print("=== 多态演示 ===")
    people = [person1, student1, teacher1]
    
    for person in people:
        person.introduce()  # 同一个方法，不同行为