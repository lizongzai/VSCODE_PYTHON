class Student:
    def __init__(self, name, student_id, age):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.grades = []  # 成绩列表

    # 方法：添加一门课的成绩
    def add_grade(self, course, grade):
        # 将成绩作为一个元组 (课程名， 分数) 添加到列表中
        self.grades.append((course, grade))
        print(f"已为 {self.name} 添加 {course} 成绩：{grade}")

    # 方法：计算平均分
    def get_average_grade(self):
        if not self.grades:  # 如果成绩列表为空
            return 0
        total = sum(grade for _, grade in self.grades)  # 使用列表推导式求和
        average = total / len(self.grades)
        return average
    
    # 方法：显示学生信息
    def display_info(self):
        print(f"学生姓名：{self.name}")
        print(f"学号：{self.student_id}")
        print(f"年龄：{self.age}")
        print("成绩单：")
        if self.grades:
            for course, grade in self.grades:
                print(f"  - {course}: {grade}")
            print(f"平均分：{self.get_average_grade():.2f}")  # 保留两位小数
        else:
            print("  暂无成绩")
        print("-" * 20)

# 使用类
student1 = Student("张三", "20240001", 20)

# 调用对象的方法
student1.add_grade("数学", 90)
# student1.add_grade("英语", 85)
# student1.add_grade("编程", 95)

student1.display_info()