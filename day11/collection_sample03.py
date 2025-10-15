# 添加元素
fruits = {"apple", "banana"}
fruits.add("orange")
fruits.update(["grape", "kiwi"])  # 添加多个
print(fruits)  # {'apple', 'banana', 'orange', 'grape', 'kiwi'}

# 删除元素
fruits.remove("banana")  # 如果不存在会报错
fruits.discard("mango")  # 如果不存在不会报错
popped = fruits.pop()    # 随机删除一个元素
print(f"删除了: {popped}, 剩余: {fruits}")

# 清空集合
fruits.clear()
