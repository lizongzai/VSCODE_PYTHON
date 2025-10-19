class Student:
    # 初始化方法（构造函数）
    # 当使用 Student() 创建对象时，这个方法会自动调用
    def __init__(self, name, student_id, age):
        # self 代表当前对象的实例，必须作为第一个参数
        # 将参数赋值给对象的属性
        self.name = name
        self.student_id = student_id
        self.age = age
        self.scores = []  # 用一个空列表来存储成绩
    
    # 方法：添加一门课的成绩
    def add_scores(self, course, score):
        self.scores.append((course, score))
        print(f'已为{self.name}添加{course}成绩: {score}')
    
    # 方法：计算平均分
    def average_scores(self):
        if not self.scores:
            return 0
        total = sum(score for _, score in self.scores)
        average =  total / len(self.scores)
        return average
    
    # 方法：显示学生信息
    def display_info(self):
        print(f'姓名: {self.name}')
        print(f'学号: {self.student_id}')
        print(f'年龄: {self.age}')
        if self.scores:
            for course, score in self.scores:
                print(f' - {course}: {score}')
            print(f'平均分: {self.average_scores():.2f}')
        else:
            print(f'暂无成绩')
        print("-" * 20)
                
                

# 创建 Student 对象（实例化）
student1 = Student("张三", "20240001", 20)
# student2 = Student("李四", "20240002", 19)


# 访问对象的属性
print(f"{student1.name}的学号是 {student1.student_id}， 年龄是 {student1.age}岁。")
# print(f"{student2.name}的学号是 {student2.student_id}， 年龄是 {student2.age}岁。")
# 输出：张三的学号是 20240001， 年龄是 20岁。


# 调用对象的方法
student1.add_scores("数学", 90)
student1.add_scores("英语", 85)
student1.add_scores("编程", 95)
# print(f"平均分：{student1.average_scores():.2f}")  # 保留两位小数

student1.display_info()