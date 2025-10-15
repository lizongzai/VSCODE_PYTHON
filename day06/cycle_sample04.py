"""
Version: 1.0
Author: 李小婕
Date: 2025-10-13
Description: 从1到100的整数求和

Keyword arguments:
argument -- description
Return: return_description
"""
sum = 0
for i in range(1, 101, 2):
    sum += i
    print(i, end=' ')
    
print("1到100的整数之和为:", sum)

