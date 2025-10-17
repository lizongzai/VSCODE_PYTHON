# 判断奇偶
check_odd = lambda x: "奇数" if x % 2 == 1 else "偶数"
print(check_odd(5))  # 输出: "奇数"
print(check_odd(4))  # 输出: "偶数"

# 绝对值
abs_value = lambda x: x if x >= 0 else -x
print(abs_value(-5))  # 输出: 5