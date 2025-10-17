"""
Version: 1.0
Author: 李小婕
Date: 2025-10-17

函数功能:
这个函数接受任意数量的位置参数和关键字参数，从中提取所有数字（整数和浮点数）并进行求和。

参数说明:
  *args：接收任意数量的位置参数
  **kwargs：接收任意数量的关键字参数

"""
def calc(*args, **kwargs):
    items = list(args) + list(kwargs.values())
    print(args, kwargs)
    result = 0
    for item in items:
        if type(item) in (int, float):
            print(item)
            result += item
    return result

# print(calc(1, 2, 3))  # 输出: 6

# print(calc(1, 'hello', 2.5, [1,2], 3))  

# print(calc(10, 20, a=5, b=15, c='text'))

print(calc(1, 2.5, 'abc', True, x=10, y=3.14, z='hello'))