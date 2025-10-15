# 生成1-10（官方表情符号）
for i in range(1, 11):
    if i == 10:
        print("🔟", end=" ")
    else:
        print(f"{i}\uFE0F\u20E3", end=" ")
print()

# 生成11-20（模拟组合）
for i in range(11, 21):
    if i < 20:
        print(f"{str(i)[0]} {str(i)[1]}\uFE0F\u20E3", end="  ")
    else:
        print(f"{str(i)[0]} {str(i)[1]}\uFE0F\u20E3", end="")