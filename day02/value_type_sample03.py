"""
Version: 1.0
Author: Changmingze
Description: 查看类型

Keyword arguments:
argument -- description
Return: return_description
"""
print("类型示例:")
# 数值类型
a = 10        # 正整数
b = -3        # 负整数
c = 0         # 零
d = 3.14      # 浮点数
e = -0.001    # 负浮点数
f = 2 + 3j    # 复数
print("\n数值类型:")
print(f"a: {a}, 类型: {type(a)}")
print(f"b: {b}, 类型: {type(b)}")
print(f"c: {c}, 类型: {type(c)}")

print(f"d: {d}, 类型: {type(d)}")
print(f"e: {e}, 类型: {type(e)}")
print(f"f: {f}, 类型: {type(f)}")
# 字符串类型
str1 = "Hello, World!"
str2 = 'Python 编程'
print("\n字符串类型:")
print(f"str1: {str1}, 类型: {type(str1)}")
print(f"str2: {str2}, 类型: {type(str2)}")
