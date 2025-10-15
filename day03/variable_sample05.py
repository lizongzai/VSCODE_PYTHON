"""
Version: 1.0
Author: Lizongzai
Description: 变量的类型检查
"""

# 使用type函数检查变量的类型
# isinstance()函数用于判断一个对象是否是某种类型

x = 100 # 变量x是整数类型
y = "hello" # 变量y是字符串类型
print(isinstance(x, int))  # True
print(isinstance(x, str))  # False

print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>

# isinstance()函数也可以判断一个变量是否是某几种类型中的一种
print(isinstance(x, (int, float, str)))  # True



# 列表
my_list = [1, 2, 3]
print(type(my_list))  # <class 'list'>

# 元组
my_tuple = (1, 2, 3)
print(type(my_tuple))  # <class 'tuple'>

# 字典
my_dict = {"name": "Alice", "age": 20}
print(type(my_dict))  # <class 'dict'>