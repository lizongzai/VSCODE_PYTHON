"""
Version: 1.0
Author: 李小婕
Keyword arguments:
    radius -- 输入的圆半径 (float)
    Return: 返回一个包含周长和面积的元组 (perimeter, area)
argument -- 输入半径计算圆的周长和面积
Return: 返回计算结果
"""

import math

def calculate_circle(radius):
    """
    计算圆的周长和面积
    Version: 1.0
    Author: 李小婕
    Keyword arguments:
    radius -- 输入半径，用于计算圆的周长和面积
    Return: 返回一个包含周长和面积的元组 (perimeter, area)
    """
    perimeter = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return perimeter, area


# 调用函数并打印结果
r = float(input("请输入圆的半径："))
perimeter, area = calculate_circle(r)

print(f"半径为 {r} 的圆：")
print(f"周长 = {perimeter:.2f}")
print(f"面积 = {area:.2f}")
