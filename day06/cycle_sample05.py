"""
Version: 1.0
Author: 李小婕
Description: 我们再来写一个从1到100偶数求和的代码，并且在每次循环中打印当前的偶数。
Date: 2025-10-13

Keyword arguments:
argument -- description
Return: return_description
"""
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum += i
        print(i, end=' ')
print("1到100的偶数之和为:", sum)
