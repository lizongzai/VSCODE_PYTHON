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
class Student(Person):   # ✅ 继承 Person
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)   # 调用父类构造方法
        self.student_id = student_id
        self.major = major
        self.courses = []  # ✅ 建议拼写改成 courses（课程）

    def enroll_course(self, course):
        """选课"""
        self.courses.append(course)
        print(f"{self.name} 已选课程：{course}")

    def show_courses(self):
        """显示所有已选课程"""
        if not self.courses:
            print(f"{self.name} 暂无选课。")
        else:
            print(f"{self.name} 的选课列表：{', '.join(self.courses)}")

# 主程序入口
if __name__ == "__main__":
    # 创建 Person 对象
    person = Person("张三", 20)
    person.introduce()
    person.have_birthday()
    print()

    # 创建 Student 对象
    student1 = Student("李四", 20, "2024001", "计算机科学")
    student1.introduce()  # ✅ 调用了父类的方法
    student1.enroll_course("Python编程")
    student1.enroll_course("数据结构")
    student1.show_courses()
