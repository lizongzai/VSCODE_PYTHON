"""
Version: 1.0
Author: Lizongzai
Description: 变量的类型检查
"""

print("--------变量的类型检查---------")
a = 100
b = 123.45
c = 'hello, world'
d = True

print(f"变量a的值: {a}, 类型: {type(a)}")  # <class 'int'>
print(f"变量b的值: {b}, 类型: {type(b)}")  # <class 'float'>
print(f"变量c的值: {c}, 类型: {type(c)}")  # <class 'str'>
print(f"变量d的值: {d}, 类型: {type(d)}")  # <class 'bool'>
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>
print(isinstance(a, int))    # True
print(isinstance(b, float))  # True
print(isinstance(c, str))    # True 
print(isinstance(d, bool))   # True
print(isinstance(a, (int, float, str)))  # True
print(isinstance(b, (int, float, str)))  # True
print(isinstance(c, (int, float, str)))  # True
print(isinstance(d, (int, float, str)))  # False
print("--------变量的类型检查---------\n")


# 元组不可变，列表可变
print("--------元组和列表的使用---------")
tuple1 = (1, 2, 3)
print(type(tuple1))  # <class 'tuple'>
print(tuple1[0])  # 访问元组的第一个元素
print(tuple1[-1])  # 访问元组的最后一个元素
print(tuple1[1:3])  # 访问元组的第二个和第三个元素
print(len(tuple1))  # 元组的长度
print("--------元组和列表的使用---------\n")
# tuple1[0] = 10  # 这行会报错！元组不可修改

# 列表
print("--------列表的使用---------")
list1 = [1, 2, 3]
list1[0] = 10  # 列表可以修改
print(list1)  # [10, 2, 3]
print(type(list1))  # <class 'list'>
print(list1[0])  # 访问列表的第一个元素
print(list1[-1])  # 访问列表的最后一个元素
print(len(list1))  # 列表的长度
print("--------列表的使用---------\n")
# 元组的访问


print("--------元组的访问---------")
mixed_tuple = (1, "hello", 3.14, True, [1, 2, 3])
print(mixed_tuple[0])    # 1
print(mixed_tuple[1])    # 'hello'
print(mixed_tuple[2])    # 3.14
print(mixed_tuple[3])    # True
print(mixed_tuple[4])    # [1, 2, 3]
print(type(mixed_tuple))  # <class 'tuple'>
print(isinstance(mixed_tuple, tuple))  # True
print(isinstance(mixed_tuple, list))   # False
print(isinstance(mixed_tuple, (list, tuple)))  # True
print(isinstance(mixed_tuple, (list, dict)))   # False
print(mixed_tuple + (4, 5, 6))  # (1, 'hello', 3.14, True, [1, 2, 3], 4, 5, 6)
print(mixed_tuple * 2)      # (1, 'hello', 3.14, True, [1, 2, 3], 1, 'hello', 3.14, True, [1, 2, 3])
print(3.14 in mixed_tuple)  # True
print('world' in mixed_tuple)  # False
print(mixed_tuple.index(True))  # 3
print(mixed_tuple.count(1))  # 1
print(mixed_tuple.count('hello'))  # 1
print("--------元组的访问---------\n")



print("--------模拟数据库配置---------")
DATABASE_CONFIG = ('localhost', 3306, 'my_db', 'user', 'password')
print(DATABASE_CONFIG)
print(type(DATABASE_CONFIG))  # <class 'tuple'>
print(isinstance(DATABASE_CONFIG, tuple))  # True
print(isinstance(DATABASE_CONFIG, list))   # False
print(isinstance(DATABASE_CONFIG, (list, tuple)))  # True
print(isinstance(DATABASE_CONFIG, (list, dict)))   # False
print(DATABASE_CONFIG[0])  # 'localhost'
print(DATABASE_CONFIG[1])  # 3306
print(DATABASE_CONFIG[2])  # 'my_db'
print(DATABASE_CONFIG[3])  # 'user'
print(DATABASE_CONFIG[4])  # 'password'
print(len(DATABASE_CONFIG))  # 5
print("--------模拟数据库配置---------\n")



print("--------函数返回多个值---------")
def get_user_info():
    name = "Alice"
    age = 25
    score = 95.5
    return name, age, score  # 自动打包成元组

user_info = get_user_info()
print(user_info)  # ('Alice', 25, 95.5)

# 解包元组
name, age, score = get_user_info()
print(f"Name: {name}, Age: {age}, Score: {score}")
print(type(user_info))  # <class 'tuple'>
print(isinstance(user_info, tuple))  # True
print(isinstance(user_info, list))   # False
print(isinstance(user_info, (list, tuple)))  # True
print(isinstance(user_info, (list, dict)))   # False
print(len(user_info))  # 3
print(user_info[0])  # 'Alice'
print(user_info[1])  # 25
print(user_info[2])  # 95.5
print(user_info.count('Alice'))  # 1
print(user_info.count(30))       # 0
print(user_info.index(25))  # 1
print(user_info + ('extra', 123))  # ('Alice', 25, 95.5, 'extra', 123)
print(user_info * 2)  # ('Alice', 25, 95.5, 'Alice', 25, 95.5)
print(25 in user_info)  # True
print(100 in user_info)  # False
print(type(name))  # <class 'str'>
print(type(age))   # <class 'int'>
print(type(score)) # <class 'float'>
print(isinstance(name, str))  # True
print(isinstance(age, int))    # True
print(isinstance(score, float)) # True

print("--------函数返回多个值---------\n")



print("--------元组作为字典的键---------")
# 元组可以作为字典的键（因为不可变）
coordinates_map = {
    (0, 0): "起点",
    (0, 1): "障碍物",
    (1, 2): "宝藏位置",
    (3, 4): "终点"
}
print(coordinates_map)
print(type(coordinates_map))  # <class 'dict'>
print(isinstance(coordinates_map, dict))  # True
print(isinstance(coordinates_map, list))  # False
print(isinstance(coordinates_map, (list, dict)))  # True
print(isinstance(coordinates_map, (list, tuple)))  # False
print(len(coordinates_map))  # 3
print(coordinates_map[(0, 0)])  # "起点"
print(coordinates_map[(0, 1)])  # "障碍物"
print(coordinates_map[(1, 2)])  # "宝藏位置"
print(coordinates_map.get((3, 4)))  # "终点"
print((1, 2) in coordinates_map)  # True
print((2, 3) in coordinates_map)  # False
print(list(coordinates_map.keys()))    # [(0, 0), (0, 1), (1, 2), (3, 4)]
print(list(coordinates_map.values()))  # ['起点', '障碍物', '宝藏位置', '终点']
print(list(coordinates_map.items()))   # [((0, 0), '起点'), ((0, 1), '障碍物'), ((1, 2), '宝藏位置'), ((3, 4), '终点')]
print(coordinates_map.get((2, 3), "未知位置"))  # "未知位置"
print(coordinates_map.keys())    # dict_keys([(0, 0), (0, 1), (1, 2), (3, 4)])
print(coordinates_map.values())  # dict_values(['起点', '障碍物', '宝藏位置', '终点'])
print(coordinates_map.items())   # dict_items([((0, 0), '起点'), ((0, 1), '障碍物'), ((1, 2), '宝藏位置'), ((3, 4), '终点')])
print(type(coordinates_map.keys()))    # <class 'dict_keys'>
print(type(coordinates_map.values()))  # <class 'dict_values'>
print(type(coordinates_map.items()))   # <class 'dict_items
print(isinstance(coordinates_map.keys(), dict_keys))    # True --- IGNORE ---
print(isinstance(coordinates_map.values(), dict_values))  # True --- IGNORE ---
print(isinstance(coordinates_map.items(), dict_items))   # True --- IGNORE ---
print("--------元组作为字典的键---------\n")



print("--------变量的多重赋值和交换---------")
# 同时赋值
a, b, c = (1, 2, 3)
print(a, b, c)  # 1 2 3

# 交换变量
x, y = 10, 20
x, y = y, x  # 交换（实际上是元组解包）
print(x, y)   # 20 10
print("--------变量的多重赋值和交换---------\n")



print("--------使用星号进行解包---------")
# 使用星号进行解包
first, *middle, last = (1, 2, 3, 4, 5)
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
print(type(middle))  # <class 'list'>
print(isinstance(middle, list))  # True
print(isinstance(middle, tuple))  # False
print(isinstance(middle, (list, tuple)))  # True
print(isinstance(middle, (tuple, dict)))  # False
print(len(middle))  # 3
print(middle[0])  # 2
print(middle[1])  # 3
print(middle[2])  # 4
print(middle[-1]) # 4
print(middle.count(3))  # 1
print(middle.count(10)) # 0
print(middle.index(4))  # 2
print(middle + [6, 7])  # [2, 3, 4, 6, 7]
print(middle * 2)       # [2, 3, 4, 2, 3, 4]
print(3 in middle)      # True
print(10 in middle)     # False
print("--------使用星号进行解包---------\n")

