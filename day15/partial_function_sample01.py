from functools import partial

# 原始函数
def multiply(a, b, c):
    return a * b * c

# 创建偏函数：固定第一个参数为 2
double = partial(multiply, 2)

print(double(3, 4))  # 输出: 24 (相当于 multiply(2, 3, 4))
print(double(5, 6))  # 输出: 60 (相当于 multiply(2, 5, 6))