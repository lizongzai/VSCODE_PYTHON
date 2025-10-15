"""
Version: 1.0
Author: 李小婕
Description: 常用数据结构示例，将一颗色子掷6000次，统计各个点数出现的次数。

Keyword arguments:
argument -- description
Return: return_description
"""
import random
# 初始化一个字典来存储点数出现的次数
dice_counts = {i: 0 for i in range(1, 7)} # 创建一个包含1到6点数的字典，初始值为0,举例：{1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
# 掷色子6000次
for _ in range(6):
    roll = random.randint(1, 6)  # 生成1到6之间的随机整数,举例子如: 3
    dice_counts[roll] += 1  # 对应点数的计数加1，举例子如: {1: 998, 2: 1005, 3: 1003, 4: 1002, 5: 995, 6: 997}
    print(roll, end=' ')  # 打印当前掷出的点数
    print(dice_counts)  # 打印当前所有点数的计数
    print()  # 换行
# 打印结果
for number, count in dice_counts.items():
    print(f"点数 {number} 出现的次数: {count}")
# 1.导入random模块
# 2.初始化字典 dice_counts = {i: 0 for i in range(1, 7)}
# 3.循环 for _ in range(6000)
# 4.生成随机数 roll = random.randint(1, 6)
# 5.更新字典 dice_counts[roll] += 1
# 6.循环结束后，打印结果 for number, count in dice_counts.items(): print(f"点数 {number} 出现的次数: {count}")
# 使用字典存储点数出现次数的步骤
# 使用random.randint生成随机数
# 使用字典的键值对存储和更新点数出现次数
# 使用for循环遍历字典并打印结果
# 使用字典推导式初始化字典
# 使用f字符串格式化输出
# 以上步骤展示了如何使用常用数据结构（字典）来统计和存储数据
# 以及如何使用循环和条件语句来处理数据。
# 这些都是Python编程中非常重要的基础知识
# 通过这个示例，读者可以更好地理解和掌握Python中的数据结构和控制流
# 以及如何将它们应用到实际问题中
# 这将有助于提高编程技能和解决问题的能力
# 希望读者能够通过这个示例，进一步探索和学习Python编程的更多内容
# 并将所学知识应用到自己的项目和工作中
# 祝大家编程愉快！