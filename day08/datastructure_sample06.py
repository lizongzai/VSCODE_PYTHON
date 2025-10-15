"""
Version: 1.0
Author: 李小婕
Description: 元组
Date: 2025-10-14

Keyword arguments:
argument -- description
Return: return_description
"""


t1 = (30, 10, 55) # 定义一个三元组
t2 = ('骆昊', 40, True, '四川成都') # 定义一个四元组

# 查看元组变量的类型
print(type(t1), type(t2))

# 查看元组中元素的数量
print(len(t1), len(t2))

# 通过索引运算获取元组中的元素
print(t1[0], t1[2])
print(t2[1], t2[3])


# 循环遍历元组中的元素
for memeber in t2:
    print(memeber)
      
# 成员运算
print(100 in t1) # false
print(40 in t2)  # true

# 拼接
t3 = t1 + t2
print(t3)           # (30, 10, 55, '骆昊', 40, True, '四川成都')

# 切片
print(t3[::3])      # (30, '骆昊', '四川成都')

# 比较运算
print(t1 == t3)    # False
print(t1 >= t3)    # False
print(t1 < (30, 11, 55))    # True