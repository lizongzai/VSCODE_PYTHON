"""
Version: 1.0
Author: 李小婕
Date: 2025-10-13
Description: 打印乘法口诀表

Keyword arguments:
argument -- description
Return: return_description
"""
for i in range(1, 10): # 外层循环控制行数, 比如1-9行
    for j in range(1, i + 1): # 内层循环控制每行的列数，比如1-9列 
        print(f"{j}*{i}={i*j}", end='\t') # 打印乘法表达式，使用制表符对齐
    print() # 每打印完一行，换行
