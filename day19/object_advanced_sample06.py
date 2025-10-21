class Animal:
    """动物基类"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        raise NotImplementedError("子类必须实现speak方法")
    
    def eat(self):
        print(f"{self.name}正在吃东西")
    
    def sleep(self):
        print(f"{self.name}正在睡觉")

class Dog(Animal):  # Dog继承Animal
    """狗类"""
    
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # 调用父类的构造方法
        self.breed = breed
    
    def speak(self):
        return f"{self.name}说: 汪汪!"
    
    def fetch(self):
        print(f"{self.name}正在接飞盘")

class Cat(Animal):  # Cat继承Animal
    """猫类"""
    
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def speak(self):
        return f"{self.name}说: 喵喵!"
    
    def climb(self):
        print(f"{self.name}正在爬树")

# 使用继承
print("=== 继承示例 ===")
dog = Dog("旺财", 3, "金毛")
cat = Cat("咪咪", 2, "白色")

print(dog.speak())  # 旺财说: 汪汪!
print(cat.speak())  # 咪咪说: 喵喵!

# 继承的方法
dog.eat()    # 从Animal继承
cat.sleep()  # 从Animal继承

# 子类特有的方法
dog.fetch()  # Dog特有的
cat.climb()  # Cat特有的