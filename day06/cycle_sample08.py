"""
Version: 1.0
Author: 李小婕
Description: 我们再来写一个从1到100求和的代码，并且在每次循环中打印当前数字。
Date: 2025-10-13
Keyword arguments:
argument -- description
Return: return_description
"""
sum = 0
i = 1
while i <= 100:
    sum += i
    print(i, end=' ')
    i += 1
print("1到100的数字之和为:", sum)

# 1.初始化变量 i = 1, sum = 0
# 2.条件 i <= 100
# 3.循环体 sum += i, print(i, end=' '), i += 1
# 4.重复2-3步
# 5.结束循环，打印结果 print("1到100的数字之和为:", sum)
# 6.优化代码 for i in range(1, 101)
# 7.优化代码 for i in range(2, 101, 2)
# 8.优化代码 while i <= 100, i += 2
# 9.优化代码 for i in range(2, 101, 2)
# 10.总结代码   从1到100的数字之和为: 5050
# 11.练习代码   如何将1到100的偶数之和的计算过程用函数封装起来？
def sum_of_even_numbers(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total
print("1到100的偶数之和为:", sum_of_even_numbers(100))

# 12.思考代码   如何将1到100的数字之和的计算过程用函数封装起来？
def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print("1到100的数字之和为:", sum_of_numbers(100))

# 13.扩展代码  将函数改为支持任意范围的数字之和计算
def sum_of_range(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total
print("1到100的数字之和为:", sum_of_range(1, 100))
print("50到150的数字之和为:", sum_of_range(50, 150))

# 14.应用代码   将函数改为支持计算偶数之和
def sum_of_even_numbers(start, end):
    total = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            total += i
    return total
print("1到100的偶数之和为:", sum_of_even_numbers(1, 100))

# 15.项目代码   将函数改为支持计算奇数之和
def sum_of_odd_numbers(start, end):
    total = 0
    for i in range(start, end + 1):
        if i % 2 != 0:
            total += i
    return total
print("1到100的奇数之和为:", sum_of_odd_numbers(1, 100))

# 16.实战代码·  将函数改为支持计算任意步长的数字之和
def sum_of_numbers_with_step(start, end, step):
    total = 0
    for i in range(start, end + 1, step):
        total += i
    return total
print("1到100的数字之和为:", sum_of_numbers_with_step(1, 100, 1))
print("1到100的偶数之和为:", sum_of_numbers_with_step(2, 100, 2))
print("1到100的奇数之和为:", sum_of_numbers_with_step(1, 100, 2))

# 17.案例代码   将函数改为支持计算任意范围和任意步长的数字之和
def sum_of_numbers_with_step(start, end, step):
    total = 0
    for i in range(start, end + 1, step):
        total += i
        print(i, end=' ')
    return total
print("1到100的数字之和为:", sum_of_numbers_with_step(1, 100, 1))
print("1到100的偶数之和为:", sum_of_numbers_with_step(2, 100, 2))
print("1到100的奇数之和为:", sum_of_numbers_with_step(1, 100, 2))

# 18.示例代码   将函数改为支持计算任意范围和任意步长的数字之和
def sum_of_numbers_with_step(start, end, step):
    total = 0
    for i in range(start, end + 1, step):
        total += i
        print(i, end=' ')
    return total
print("1到100的数字之和为:", sum_of_numbers_with_step(1, 100, 1))
print("1到100的偶数之和为:", sum_of_numbers_with_step(2, 100, 2))
print("1到100的奇数之和为:", sum_of_numbers_with_step(1, 100, 2))

# 19.样例代码   将函数改为支持计算任意范围和任意步长的数字之和
def sum_of_numbers_with_step(start, end, step):
    total = 0
    for i in range(start, end + 1, step):
        total += i
        print(i, end=' ')
    return total
print("1到100的数字之和为:", sum_of_numbers_with_step(1, 100, 1))
print("1到100的偶数之和为:", sum_of_numbers_with_step(2, 100, 2))
print("1到100的奇数之和为:", sum_of_numbers_with_step(1, 100, 2))

# 20.范例代码   将函数改为支持计算任意范围和任意步长的数字之和
def sum_of_numbers_with_step(start, end, step):
    total = 0
    for i in range(start, end + 1, step):
        total += i
        print(i, end=' ')
    return total
print("1到100的数字之和为:", sum_of_numbers_with_step(1, 100, 1))
print("1到100的偶数之和为:", sum_of_numbers_with_step(2, 100, 2))
print("1到100的奇数之和为:", sum_of_numbers_with_step(1, 100, 2))

# 21.模板代码   将函数改为支持计算任意范围和任意步长的数字之和
def sum_of_numbers_with_step(start, end, step):
    total = 0
    for i in range(start, end + 1, step):
        total += i
        print(i, end=' ')
    return total
print("1到100的数字之和为:", sum_of_numbers_with_step(1, 100, 1))
print("1到100的偶数之和为:", sum_of_numbers_with_step(2, 100, 2))
print("1到100的奇数之和为:", sum_of_numbers_with_step(1, 100, 2))

# 22.框架代码  将函数改为支持计算任意范围和任意步长的数字之和
def sum_of_numbers_with_step(start, end, step):
    total = 0
    for i in range(start, end + 1, step):
        total += i
        print(i, end=' ')
    return total
print("1到100的数字之和为:", sum_of_numbers_with_step(1, 100, 1))
print("1到100的偶数之和为:", sum_of_numbers_with_step(2, 100, 2))
print("1到100的奇数之和为:", sum_of_numbers_with_step(1, 100, 2))
# 23.结构代码 将函数改为支持计算任意范围和任意步长的数字之和
def sum_of_numbers_with_step(start, end, step):
    total = 0
    for i in range(start, end + 1, step):
        total += i
        print(i, end=' ')
    return total
print("1到100的数字之和为:", sum_of_numbers_with_step(1, 100, 1))
print("1到100的偶数之和为:", sum_of_numbers_with_step(2, 100, 2))
print("1到100的奇数之和为:", sum_of_numbers_with_step(1, 100, 2))
# 24.循环代码 将函数改为支持计算任意范围和任意步长的数字之和
def sum_of_numbers_with_step(start, end, step):
    total = 0
    for i in range(start, end + 1, step):
        total += i
        print(i, end=' ')
    return total    

print("1到100的数字之和为:", sum_of_numbers_with_step(1, 100, 1))
print("1到100的偶数之和为:", sum_of_numbers_with_step(2, 100, 2))
print("1到100的奇数之和为:", sum_of_numbers_with_step(1, 100, 2))