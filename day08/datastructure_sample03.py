"""
Version: 1.0
Author: 李小婕
Description: 掷多个骰子（n ≤ 6）并统计各点数出现的次数
Date: 2025-10-14

Keyword arguments:
argument -- description
Return: return_description
"""

import random
dice_counts = {i: 0 for i in range(1, 7)}
# 假设一次掷出 n 个骰子（n ≤ 6）
n = 4
rolls = [random.randint(1, 6) for _ in range(n)]  # 一次生成 n 个随机点数
print("这次掷出的点数是:", rolls) # 举例子如: [3, 5, 2, 6]

for roll in rolls:
    dice_counts[roll] += 1 
    # 更新对应点数的计数, 举例子: [3, 5, 2, 6] 中的 3 计数加 1，那么dice_counts变为 {1: 0, 2: 1, 3: 1, 4: 0, 5: 1, 6: 1}
    # dice_counts[0] += 1 # KeyError: 0
print("统计结果:", dice_counts)
