# ======================
# 父类（基类）：Person
# ======================
class Person:
    def __init__(self, name, age):
        # 将属性设置为“私有”属性（外部不可直接访问）
        self.__name = name
        self.__age = age

    # 封装属性访问方法（getter / setter）
    @property
    def name(self):
        """获取姓名"""
        return self.__name

    @name.setter
    def name(self, value):
        """修改姓名"""
        if not value:
            print("姓名不能为空！")
        else:
            self.__name = value

    @property
    def age(self):
        """获取年龄"""
        return self.__age

    @age.setter
    def age(self, value):
        """修改年龄，增加校验逻辑"""
        if value < 0:
            print("年龄不能为负数！")
        else:
            self.__age = value

    def introduce(self):
        """打印自我介绍"""
        print(f"你好，我叫 {self.__name}，今年 {self.__age} 岁。")

    def have_birthday(self):
        """过生日，年龄 +1"""
        self.__age += 1
        print(f"祝 {self.__name} 生日快乐！现在 {self.__age} 岁了。")


# ======================
# 子类：学生
# ======================
class Student(Person):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)
        self.__student_id = student_id
        self.__major = major
        self.__courses = []  # 私有选课列表

    def introduce(self):
        """重写介绍方法"""
        print(f"你好，我是学生 {self.name}（学号：{self.__student_id}），"
              f"主修 {self.__major}，今年 {self.age} 岁。")

    def enroll_course(self, course_name):
        """添加选课"""
        self.__courses.append(course_name)
        print(f"{self.name} 已选课：{course_name}")

    def show_courses(self):
        """查看选课"""
        if self.__courses:
            print(f"{self.name} 的选课列表：{', '.join(self.__courses)}")
        else:
            print(f"{self.name} 还没有选任何课程")


# ======================
# 子类：老师
# ======================
class Teacher(Person):
    def __init__(self, name, age, department, employee_id):
        super().__init__(name, age)
        self.__department = department
        self.__employee_id = employee_id

    def introduce(self):
        """重写介绍方法"""
        print(f"大家好，我是 {self.__department} 的教师 {self.name}，工号 {self.__employee_id}。")

    def teach(self):
        print(f"{self.name} 老师正在授课...")


# ======================
# 主程序
# ======================
if __name__ == "__main__":
    person1 = Person("张三", 25)
    person1.introduce()
    person1.have_birthday()
    print()

    student1 = Student("李四", 20, "2024001", "计算机科学")
    student1.introduce()
    student1.enroll_course("Python编程")
    student1.show_courses()
    print()

    teacher1 = Teacher("王教授", 45, "计算机学院", "T1001")
    teacher1.introduce()
    teacher1.teach()
    print()

    # 测试封装的安全性
    print("=== 测试封装 ===")
    # print(student1.__student_id)  # ❌ 会报错：外部不能直接访问私有属性
    student1.name = "李小四"        # ✅ 通过 setter 修改
    print("修改后的姓名：", student1.name)
