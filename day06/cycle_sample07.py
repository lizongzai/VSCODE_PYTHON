"""
Version: 1.0
Author: 李小婕
Description: 使用while循环实现从1到100偶数求和，并且在每次循环中打印当前的偶数。
Date: 2025-10-13
Keyword arguments:
argument -- description
Return: return_description
"""
sum = 0
i = 2
while i <= 100:
    sum += i
    print(i, end=' ')
    i += 2
print("1到100的偶数之和为:", sum)

# 1.初始化变量 i = 2, sum = 0
# 2.条件 i <= 100
# 3.循环体 sum += i, print(i, end=' '), i += 2
# 4.重复2-3步
# 5.结束循环，打印结果 print("1到100的偶数之和为:", sum)
