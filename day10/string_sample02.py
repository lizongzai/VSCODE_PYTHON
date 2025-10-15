s = 'abc123456'

print("=== 正向索引 ===")
for i in range(len(s)):
    print(f"s[{i}] = '{s[i]}'")

print("\n=== 反向索引 ===")
for i in range(-1, -len(s)-1, -1):
    print(f"s[{i}] = '{s[i]}'")

print("\n=== 同时显示 ===")
print("字符: ", end="")
for char in s:
    print(f"  {char}  ", end="")
print()

print("正向: ", end="")
for i in range(len(s)):
    print(f"  {i}  ", end="")
print()

print("反向: ", end="")
for i in range(-1, -len(s)-1, -1):
    print(f" {i} ", end="")
print()