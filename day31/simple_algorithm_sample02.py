"""
Version: 1.0
Author: lixiaojie
Description: 降序排序（传 comp=lambda x, y: x > y）
Date: 2025-11-05
"""

def select_sort(items, comp=lambda x, y: x < y):
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
        print(f'第{i+1}轮排序结果: {items}')  # 打印每轮排序后的列表
    return items


nums = [3, 1, 4, 2]
sorted_nums = select_sort(nums, comp=lambda x, y: x > y)
print(sorted_nums)
