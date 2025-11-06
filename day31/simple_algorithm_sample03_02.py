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
            # =======================================算法执行过程分析==========================================================
            # 以下注释展示了以 [-3, 1, -4, 2] 按绝对值升序排序为例的详细执行过程：
            #
            # 第一轮比较 (i=0): 在[-3, 1, -4, 2]中找绝对值最小的元素
            #   初始化：当 i=0, j=1, min_index=0 时，初始化排序[-3, 1, -4, 2]
            #   第一次比较：j=1, min_index=0，比较 abs(1)=1 < abs(-3)=3 → True → min_index=1
            #   第二次比较：j=2, min_index=1，比较 abs(-4)=4 < abs(1)=1 → False → min_index=1
            #   第三次比较：j=3, min_index=1，比较 abs(2)=2 < abs(1)=1 → False → min_index=1
            #   交换 items[0]=-3 和 items[1]=1
            #   第一轮排序结果: [1, -3, -4, 2]
            #
            # 第二轮比较 (i=1): 在[-3, -4, 2]中找绝对值最小的元素
            #   初始化：当 i=1, j=2, min_index=1 时
            #   第一次比较：j=2, min_index=1，比较 abs(-4)=4 < abs(-3)=3 → False → min_index=1
            #   第二次比较：j=3, min_index=1，比较 abs(2)=2 < abs(-3)=3 → True → min_index=3
            #   交换 items[1]=-3 和 items[3]=2
            #   第二轮排序结果: [1, 2, -4, -3]
            #
            # 第三轮比较 (i=2): 在[-4, -3]中找绝对值最小的元素
            #   初始化：当 i=2, j=3, min_index=2 时
            #   第一次比较：j=3, min_index=2，比较 abs(-3)=3 < abs(-4)=4 → True → min_index=3
            #   交换 items[2]=-4 和 items[3]=-3
            #   第三轮排序结果: [1, 2, -3, -4]
            # ==============================================================================================================
            
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
    
    print('\n' + '='*50)
    print('详细交换过程:')
    print('第1轮交换: 位置0(-3) ↔ 位置1(1) → [1, -3, -4, 2]')
    print('第2轮交换: 位置1(-3) ↔ 位置3(2) → [1, 2, -4, -3]')
    print('第3轮交换: 位置2(-4) ↔ 位置3(-3) → [1, 2, -3, -4]')