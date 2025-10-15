"""
Version:1.0
Author: 李小婕

Keyword arguments:
    year -- 输入年份
    argument -- 输入年份，闰年输出True，平年输出False
    Return: 返回一个布尔值，表示是否为闰年
Description: 判断是否为闰年
"""

def is_leap_year(year):
    """
    判断是否为闰年
    Version: 1.0
    Author: 李小婕
    Keyword arguments:
    year -- 输入年份
    Return: 返回一个布尔值，表示是否为闰年
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
# 输入年份并调用函数
year = int(input("请输入年份: "))
if is_leap_year(year):
    print(f"{year} 是闰年")
else:
    print(f"{year} 不是闰年")
print("--------判断是否为闰年---------\n")


