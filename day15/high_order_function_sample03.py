"""
Version: 1.0
Author: 李小婕
Date: 2025-10-17

函数功能
    这个函数接受一个初始值、一个运算函数和任意数量的参数，然后按照指定的运算规则对所有数字参数进行计算。

参数说明
    init_value：初始值
    op_func：运算函数（如加法、乘法等）
    *args：接收任意数量的位置参数
    **kwargs：接收任意数量的关键字参数
"""

def calc(init_value, op_func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result

def add(a = 1, b = 2):
    return a + b

# 从10开始，加上所有数字参数
print(calc(10, add, 1, 2, 3, x=4, y=5))
# 执行: 10 + 1 + 2 + 3 + 4 + 5 = 25


def maximum(a, b):
    return a if a > b else b

# 从0开始，找最大值
print(calc(0, maximum, 3, 7, 2, 9, x=5))
# 执行: max(0, 3, 7, 2, 9, 5) = 9




def custom_op(a, b):
    return a * 2 + b

print(calc(1, custom_op, 2, 3, 4))
# 执行: 
# 初始: result = 1
# 第一步: 1*2 + 2 = 4
# 第二步: 4*2 + 3 = 11  
# 第三步: 11*2 + 4 = 26