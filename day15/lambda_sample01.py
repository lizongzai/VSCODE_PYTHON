# 在 sorted 中使用
numbers = [('a', 3), ('b', 1), ('c', 2)]
sorted_numbers = sorted(numbers, key=lambda number: number[1])
print(sorted_numbers)  # 输出: [('b', 1), ('c', 2), ('a', 3)]

# 在 map 中使用
numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda number: number ** 2, numbers))
print(squared_numbers)  # 输出: [1, 4, 9, 16]

# 在 filter 中使用
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print(even_numbers)  # 输出: [2, 4, 6]