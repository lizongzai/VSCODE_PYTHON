# 创建集合
set1 = {1, 2, 3, 4, 5}
set2 = set([3, 4, 5, 6, 7])  # 从列表创建
set3 = set()  # 空集合（不能用 {}，那是字典）

print(set1)  # {1, 2, 3, 4, 5}
print(set2)  # {3, 4, 5, 6, 7}


my_set = {3, 1, 4, 1, 4, 5, 9, 2}
print(my_set)  # 输出顺序可能不同：{1, 2, 3, 4, 5, 9}



numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3, 4}