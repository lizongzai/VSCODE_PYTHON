"""
输入M和N计算C(M,N)

Version: 0.1
Author: 骆昊
"""

# 定义函数：def是定义函数的关键字、fac是函数名，num是参数（自变量）
def fac(num):
    """求阶乘"""
    result = 1
    for i in range(1, num + 1):  # 使用i作为循环变量
        result *= i
        print(f"i={i}: result={result}")
    return result

m = int(input('m = '))  # m = 4
n = int(input('n = '))  # n = 3

# 当需要计算阶乘的时候不用再写重复的代码而是直接调用函数fac
# 调用函数的语法是在函数名后面跟上圆括号并传入参数
print(fac(m) // fac(n) // fac(m - n))
