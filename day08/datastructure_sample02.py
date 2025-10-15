"""
Version: 1.0
Author: 李小婕
Description: 同时一次掷出 ≤ 6 个骰子
Date: 2025-10-14

Keyword arguments:
argument -- description
Return: return_description
"""
import random
num_dice = int(input("请输入要掷出的骰子数量 (1-6): "))
if 1 <= num_dice <= 6:
    rolls = [random.randint(1, 6) for _ in range(num_dice)]
    print(f"你掷出的 {num_dice} 个骰子的点数分别是: {', '.join(map(str, rolls))}")
    print(f"总和为: {sum(rolls)}")
else:
    print("请输入一个介于 1 到 6 之间的数字。")

# 运行示例:
# 请输入要掷出的骰子数量 (1-6): 4
# 你掷出的 4 个骰子的点数分别是: 3, 5, 2, 6
# 总和为: 16
# 1.导入random模块
# 2.提示用户输入要掷出的骰子数量 (1-6)
# 3.检查输入的数量是否在1到6之间
# 4.使用列表生成式和random.randint生成指定数量的随机骰子点数
# 5.打印每个骰子的点数和总和
# 6.如果输入无效，提示用户输入正确的数字
# 使用列表生成式生成多个随机数
# 使用join和map打印列表内容
# 使用sum计算列表元素的和
# 输入验证
# 使用f字符串格式化输出
# 代码简洁高效
# 适当的用户提示
# 良好的代码注释
# 清晰的逻辑结构
# 易于扩展和修改
# 良好的变量命名
# 适当的错误处理
# 遵循Python编码规范
# 代码可读性强
