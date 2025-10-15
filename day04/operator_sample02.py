"""
赋值运算符和复合赋值运算符

Version: 1.0
Author: 骆昊
"""
a = 10
b = 3
a += b        # 相当于：a = a + b
a *= a + 2    # 相当于：a = a * (a + 2)
print(a)      # 大家算一下这里会输出什么


"""
海象运算符

Version: 1.0
Author: 骆昊
"""
# SyntaxError: invalid syntax
# print((a = 10))
# 海象运算符
print("--------海象运算符---------")
print((a := 10))  # 10
print(a)          # 10
print((b := a * 2))  # 20
print(b)             # 20
print("--------海象运算符---------\n")

# 在条件表达式中使用海象运算符
print("--------在条件表达式中使用海象运算符---------")
print((n := len("hello")) > 5)  # False
print(n)                        # 5
print((n := len("hello, world")) > 5)  # True
print(n)                               # 12
print("--------在条件表达式中使用海象运算符---------\n")

# 在列表推导式中使用海象运算符
print("--------在列表推导式中使用海象运算符---------")
print([y := f"Item {x}" for x in range(5)])  # ['Item 0', 'Item 1', 'Item 2', 'Item 3', 'Item 4']
print(y)  # Item 4
print("--------在列表推导式中使用海象运算符---------\n")

# 在循环中使用海象运算符
print("--------在循环中使用海象运算符---------")
while (line := input("请输入内容，输入exit退出: ")) != "exit":
    print(f"你输入的内容是: {line}")
print("--------在循环中使用海象运算符---------\n")

# 注意：海象运算符不能取代所有的赋值语句
# 例如下面的代码就会报错
# if (n := len(input("请输入内容: "))) > 5 and n < 10:
#     print("你输入的内容长度在5到10之间")
# print(n)  # NameError: name 'n' is not defined
# 正确的写法应该是
n = len(input("请输入内容: "))
if n > 5 and n < 10:
    print("你输入的内容长度在5到10之间")
print(n)  # 这里的n是可以访问的
# 另外，海象运算符不能用于为多个变量赋值
# (x := y := 0)  # SyntaxError: cannot assign to operator
# 只能用于为单个变量赋值
# x = y = 0  # 这是正确的写法
x = 0
y = 0
print(x, y)  # 0 0
print("--------赋值运算符和复合赋值运算符---------\n")
a = 10
b = 3
a += b        # 相当于：a = a + b
a *= a + 2    # 相当于：a = a * (a + 2)
print(a)      # 大家算一下这里会输出什么
print("--------赋值运算符和复合赋值运算符---------\n")
