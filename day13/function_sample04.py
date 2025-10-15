from random import randint

def roll_dice(n=2):
    """摇色子返回总的点数"""
    total = 0
    print(f"开始摇{n}个色子：")
    for i in range(n):
        point = randint(1, 6)
        total += point
        print(f"  第{i+1}次摇色子点数: {point}，当前总分: {total}")
    print(f"摇色子总点数: {total}\n")
    return total

# 测试
print("=== 第一次摇色子 ===")
result1 = roll_dice() # 设置默认值为 n = 2
print(f"返回值: {result1}\n")

print("=== 第二次摇色子 ===")
result2 = roll_dice(3)
print(f"返回值: {result2}")