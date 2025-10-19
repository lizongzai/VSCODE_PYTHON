
# 第一步：定义类
class StudentInformation:

    # 初始化方法（构造函数）
    # 当使用 Student() 创建对象时，这个方法会自动调用    
    def __init__(self, name, stu_id, age):
        self.name = name
        self.stu_id = stu_id
        self.age = age
        self.grades = []
        
    def eat(self):
        print("I'm a college student from Peiking Univercity")


# 第二步：创建对应
student1 = StudentInformation("Jason", "1001", 22);
student2 = StudentInformation("Ocean", "1002", 21);

# 第三步：给对象发消息
print(student1.name)
student1.eat()
