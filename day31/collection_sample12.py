from collections import Counter  # 从 collections 模块导入 Counter 类，用于统计元素出现次数

# 定义一个列表，包含一些水果名称
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# 使用 Counter 对列表中的元素进行计数
c = Counter(words)  
# c 变成一个 Counter 对象，本质上是字典 {'apple': 3, 'banana': 2, 'orange': 1}

# 打印 Counter 对象
print(c)  
# 输出：Counter({'apple': 3, 'banana': 2, 'orange': 1})
# 表示 'apple' 出现了 3 次，'banana' 出现了 2 次，'orange' 出现了 1 次

# 打印出现次数最多的前 2 个元素
print(c.most_common(2))  
# 输出：[('apple', 3), ('banana', 2)]
# most_common(n) 方法返回出现次数最多的 n 个元素及其计数，按次数降序排列