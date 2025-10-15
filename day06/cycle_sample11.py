"""
Version: 1.0
Author: 李小婕
Description: 从1到100的偶数求和,并且使用continue语句跳过奇数
Date: 2025-10-13
Keyword arguments:
argument -- description
Return: return_description
"""
sum = 0
for i in range(1, 101):
    if i % 2 != 0:  # 奇数,比如1,3,5,7,9
        continue
    sum += i
    print(i, end=' ')
print("1到100的偶数之和为:", sum)
# 1.初始化变量 sum = 0
# 2.循环 for i in range(1, 101)
# 3.条件 if i % 2 != 0
# 4.跳过 continue
# 5.循环体 sum += i, print(i, end=' ')
# 6.重复2-5步
# 7.结束循环，打印结果 print("1到100的偶数之和为:", sum)
# 使用continue跳过奇数的步骤