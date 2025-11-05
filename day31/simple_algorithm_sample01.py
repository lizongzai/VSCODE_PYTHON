"""
Version: 1.0
Author: lixiaojie
Description: 默认升序排序（不传 comp）
Date: 2025-11-05
"""
def select_sort(items, comp=lambda x, y: x < y):
    """
    简单选择排序（Selection Sort）

    Args:
        items: 待排序的列表
        comp: 比较函数，默认升序排序，返回 True 表示前者优先于后者
              例如:
                - comp=lambda x, y: x < y  -> 升序
                - comp=lambda x, y: x > y  -> 降序

    Returns:
        排序后的新列表（原列表不修改）
    """
    # 拷贝列表，避免修改原列表
    items = items[:]
    
    # 外层循环：依次确定每个位置的元素
    for i in range(len(items) - 1):
        # 假设当前位置 i 的元素是当前最小值
        min_index = i
        
        # 内层循环：在剩余未排序的元素中寻找更小（或更优先）的元素
        for j in range(i + 1, len(items)):
            # 如果 items[j] 更符合排序规则（更小或更优先），更新 min_index
            if comp(items[j], items[min_index]):
                min_index = j
        
        # 交换当前位置 i 的元素与找到的最小元素
        items[i], items[min_index] = items[min_index], items[i]
        
        # 打印每轮排序后的列表状态，便于观察排序过程
        print(f'第{i+1}轮排序结果: {items}')
    
    # 返回排序后的新列表
    return items


# 测试示例
nums = [-3, 1, -4, 2]
sorted_nums = select_sort(nums, comp=lambda x, y: abs(x) < abs(y))  # 按绝对值升序排序
print(sorted_nums)  # 输出最终排序结果
