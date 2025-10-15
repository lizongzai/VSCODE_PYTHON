# 数学: 5 ≠ 3
# Python:
print(5 != 3)  # True

# 数学: x ≠ y  
# Python:
x = 10
y = 20
if x != y:
    print(f"{x} 不等于 {y}")
# 输出: x不等于y
elif x == y:
    print(f"{x} 等于 {y}")
# 输出: x等于y
elif x > y:
    print(f"{x} 大于 {y}")
# 输出: x大于y
elif x < y:
    print(f"{x} 小于 {y}")
# 输出: x小于y
elif x >= y:
    print(f"{x} 大于等于 {y}")
# 输出: x大于等于y
elif x <= y:
    print(f"{x} 小于等于 {y}")
else:
    print("无法比较")