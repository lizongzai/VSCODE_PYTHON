"""
Version: 1.0
Author: 李小婕
Description: 
1. 一旦使用 `__slots__` 会**严格限制**类实例只能拥有指定的属性，不能动态添加额外的属性。
2.添加额外的属性时，提示报错'StudentWithSlots' object has no attribute <error_name>'
3.除非去掉这段代码： __slots__ = ('name', 'age')

Keyword arguments:
argument -- description
Return: return_description
"""

class StudentWithSlots:
    __slots__ = ('name', 'age')  # 只允许这两个属性
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 创建对象
stu = StudentWithSlots('张三', 20)

# 允许的操作 ✅
stu.name = '李四'    # 修改已有属性
stu.age = 21         # 修改已有属性

# 不允许的操作 ❌
try:
    stu.gender = '男'  # 尝试添加新属性
except AttributeError as e:
    print(f"错误: {e}")  # 'StudentWithSlots' object has no attribute 'gender'

try:
    stu.score = 95    # 尝试添加另一个新属性
except AttributeError as e:
    print(f"错误: {e}")  # 'StudentWithSlots' object has no attribute 'score'