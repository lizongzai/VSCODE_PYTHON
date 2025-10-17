def apply_twice(func, x):
    return func(func(x))

def add_three(n):
    return n + 3

result = apply_twice(add_three, 7)
print(result)  # 输出 13，因为 (7+3)+3=13
