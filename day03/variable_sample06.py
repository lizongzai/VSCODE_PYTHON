"""
Version: 1.0
Author: Lizongzai
Description: 变量的类型检查和元组、列表的使用
"""


# 元组不可变，列表可变
tuple1 = (1, 2, 3)
print(type(tuple1))  # <class 'tuple'>
print(tuple1[0])  # 访问元组的第一个元素
print(tuple1[-1])  # 访问元组的最后一个元素
print(tuple1[1:3])  # 访问元组的第二个和第三个元素
print(len(tuple1))  # 元组的长度
# tuple1[0] = 10  # 这行会报错！元组不可修改

# 列表
list1 = [1, 2, 3]
list1[0] = 10  # 列表可以修改
print(list1)  # [10, 2, 3]
print(type(list1))  # <class 'list'>
print(list1[0])  # 访问列表的第一个元素
print(list1[-1])  # 访问列表的最后一个元素

# 元组的访问
fruits = ('apple', 'banana', 'cherry')
print(fruits[0])   # 'apple'
print(fruits[-1])  # 'cherry'
print(fruits[1:3]) # ('banana', 'cherry')
print(len(fruits))  # 3
print(type(fruits))  # <class 'tuple'>
print(isinstance(fruits, tuple))  # True
print(isinstance(fruits, list))   # False
print(isinstance(fruits, (list, tuple)))  # True
print(isinstance(fruits, (list, dict)))   # False
print(tuple1 + fruits)  # (1, 2, 3, 'apple', 'banana', 'cherry')
print(fruits * 2)      # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
print(2 in tuple1)     # True
print('banana' in fruits)  # True
print('orange' in fruits)  # False
print(tuple1.index(2))  # 1
print(fruits.count('apple'))  # 1
print(fruits.count('orange'))  # 0
