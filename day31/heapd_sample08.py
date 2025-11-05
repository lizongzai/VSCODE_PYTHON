"""
从列表中找出最大的或最小的 N 个元素
使用堆结构（大根堆/小根堆）
"""
import heapq  # 导入 heapq 模块，用于堆操作

# 一个整数列表，用于演示最大/最小 N 个元素
list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]

# 一个字典列表，每个字典表示一只股票的信息
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# 找出 list1 中最大的 3 个元素
print(heapq.nlargest(3, list1))  
# 输出: [99, 92, 88]

# 找出 list1 中最小的 3 个元素
print(heapq.nsmallest(3, list1))  
# 输出: [12, 25, 34]

# 找出 list2 中价格最高的 2 支股票
# key 参数指定排序依据为字典中的 'price' 字段
print(heapq.nlargest(2, list2, key=lambda x: x['price']))
# 输出: [{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}]

# 找出 list2 中持股数最多的 2 支股票
# key 参数指定排序依据为字典中的 'shares' 字段
print(heapq.nlargest(2, list2, key=lambda x: x['shares']))
# 输出: [{'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'IBM', 'shares': 100, 'price': 91.1}]
