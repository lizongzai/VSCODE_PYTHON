from functools import partial

def power(base, exponent):
    print(f"计算: {base} 的 {exponent} 次方 = {base ** exponent}")
    return base ** exponent

# 创建偏函数
square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print("调用 square(5):")
result1 = square(5)
print(f"结果: {result1}\n")

print("调用 cube(3):")
result2 = cube(3)
print(f"结果: {result2}")