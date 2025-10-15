"""
Version: 1.0
Author: 李小婕
Date: 2024-06-17
Description: 输入一个大于1的正整数判断它是不是素数,并打印结果。

Keyword arguments:
argument -- description
Return: return_description
"""

num = int(input("请输入一个大于1的正整数: "))
if num <= 1:
    print("输入无效，请输入一个大于1的正整数。")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1): # 只需检查到sqrt(num), 比如36只需检查到6
        if num % i == 0: # 能被整除, 说明不是素数
            is_prime = False # 不是素数
            break # 跳出循环
    if is_prime:
        print(f"{num} 是素数。")
    else:
        print(f"{num} 不是素数。")
# 1.输入一个大于1的正整数
# 2.判断输入的数是否小于等于1，如果是，打印无效输入
# 3.初始化一个标志变量 is_prime = True
# 4.使用for循环从2到sqrt(num)遍历可能的因子
# 5.在循环中判断 num 是否能被 i 整除，如果能，设置 is_prime = False 并跳出循环
# 6.循环结束后，根据 is_prime 的值打印结果
# 使用break跳出循环的步骤
# 使用for循环遍历可能的因子
# 使用平方根优化素数判断