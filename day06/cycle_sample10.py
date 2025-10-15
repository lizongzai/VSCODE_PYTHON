"""
Version: 1.0
Author: 李小婕
Description: 从1到100的偶数求和,并且使用break跳出循环
Date: 2025-10-13

Keyword arguments:
argument -- description
Return: return_description
"""
sum = 0
i = 2
while True: # 使用while True创建一个无限循环
    sum += i # 累加当前的偶数
    i += 2 # 每次增加2
    print(i - 2, end=' ') # 打印当前的偶数
    if i > 100: # 使用break跳出循环
        break # 跳出循环
print("1到100的偶数之和为:", sum)

# 1.初始化变量 i = 2, sum = 0
# 2.条件 i <= 100
# 3.循环体 sum += i, i += 2, if i > 100: break
# 4.重复2-3步
# 5.结束循环，打印结果 print("1到100的偶数之和为:", sum)
# 使用break跳出循环的步骤