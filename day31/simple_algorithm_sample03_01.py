"""
Version: 1.0
Author: lixiaojie
Description: 自定义比较函数，比如按绝对值升序
Date: 2025-11-05
"""

def select_sort(items, comp=lambda x, y: x < y):
    """
    选择排序算法，支持自定义比较函数
    
    Args:
        items: 要排序的列表
        comp: 比较函数，默认是标准升序(x<y)
    
    Returns:
        排序后的新列表（原列表不被修改）
    """
    items = items[:]  # 创建列表副本，不修改原列表
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            # 使用自定义比较函数判断元素顺序
            if comp(items[j], items[min_index]):
                min_index = j
        # 交换当前位置和最小位置的值
        items[i], items[min_index] = items[min_index], items[i]
        print(f'第{i+1}轮排序结果: {items}')  # 打印每轮排序后的列表
    return items


if __name__ == "__main__":
    # 测试按绝对值升序排序
    nums = [-3, 1, -4, 2]
    print(f'原始列表: {nums}')
    print('开始按绝对值升序排序...')

    sorted_nums = select_sort(nums, comp=lambda x, y: abs(x) < abs(y))
    print(f'最终排序结果: {sorted_nums}')

    print('\n' + '='*50)
    print('排序过程说明:')
    print('按绝对值大小排序: |-4|(4) > |-3|(3) > |2|(2) > |1|(1)')
    print('所以排序结果为: [1, 2, -3, -4]')