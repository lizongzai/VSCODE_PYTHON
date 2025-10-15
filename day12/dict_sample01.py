person = {'name': '王大锤', 'age': 55, 'weight': 60, 'office': '科华北路62号'}

print("=== 方法1: 通过key获取value ===")
for key in person:
    print(person[key])

print("\n=== 方法2: 直接遍历values ===")
for value in person.values():
    print(value)

print("\n=== 方法3: 同时显示键值对 ===")
for key, value in person.items():
    print(f"{key}: {value}")

print("\n=== 方法4: 一次性获取所有值 ===")
print(list(person.values()))