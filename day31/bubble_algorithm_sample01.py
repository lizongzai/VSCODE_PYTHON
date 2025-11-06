"""
Version: 1.1
Author: lixiaojie
Description: 冒泡排序算法--> 降序排序
Date: 2025-11-06

Keyword arguments:
argument -- description
Return: return_description
"""

def bubble_sort_descending(items, comp=lambda x, y: x < y):
    """
    冒泡排序算法 - 降序排序
    
    Args:
        items: 要排序的列表
        comp: 比较函数，默认是降序(x<y)，返回True时需要交换
    
    Returns:
        排序后的新列表（原列表不被修改）
    """
    items = items[:]  # 创建列表副本，不修改原列表
    n = len(items)
    for i in range(n - 1):
        swapped = False  # 标记本轮是否发生交换
        print(f'\n--- 第{i+1}轮冒泡排序 ---')
        
        for j in range(n - 1 - i): 
            # =======================================算法执行过程分析==========================================================
            # 以下注释展示了以 [3, 1, 4, 2] 降序排序为例的详细执行过程：
            #
            # 第一轮比较 (i=0): 在[3, 1, 4, 2]中从前往后比较相邻元素
            #   第一次比较：j=0，比较 items[0]=3 和 items[1]=1，3<1? False → 不交换 → [3, 1, 4, 2]
            #   第二次比较：j=1，比较 items[1]=1 和 items[2]=4，1<4? True → 交换 → [3, 4, 1, 2]
            #   第三次比较：j=2，比较 items[2]=1 和 items[3]=2，1<2? True → 交换 → [3, 4, 2, 1]
            #   第一轮排序结果: [3, 4, 2, 1]
            #
            # 第二轮比较 (i=1): 在[3, 4, 2]中比较相邻元素（最后1个元素已确定）
            #   第一次比较：j=0，比较 items[0]=3 和 items[1]=4，3<4? True → 交换 → [4, 3, 2, 1]
            #   第二次比较：j=1，比较 items[1]=3 和 items[2]=2，3<2? False → 不交换 → [4, 3, 2, 1]
            #   第二轮排序结果: [4, 3, 2, 1]
            #
            # 第三轮比较 (i=2): 在[4, 3]中比较相邻元素（最后2个元素已确定）
            #   第一次比较：j=0，比较 items[0]=4 和 items[1]=3，4<3? False → 不交换 → [4, 3, 2, 1]
            #   由于没有发生交换，提前结束排序
            # ==============================================================================================================
            
            # 打印比较前的状态
            print(f'  比较 items[{j}]={items[j]} 和 items[{j+1}]={items[j+1]}', end='')
            
            # 使用比较函数判断是否需要交换
            if comp(items[j], items[j + 1]):
                # 交换相邻元素
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
                print(f' → 需要交换 → 交换后: {items}')
            else:
                print(f' → 不需要交换')
        
        print(f'第{i+1}轮排序结果: {items}')
        
        # 如果本轮没有发生交换，说明已经有序，提前结束
        if not swapped:
            print('没有发生交换，排序完成！')
            break
    
    return items


if __name__ == "__main__":
    # 测试降序排序
    nums = [3, 1, 4, 2]
    print(f'原始列表: {nums}')
    print('开始降序排序 (comp=lambda x, y: x < y)...')
    print('=' * 60)
    
    sorted_nums = bubble_sort_descending(nums, comp=lambda x, y: x < y)
    print('=' * 60)
    print(f'\n最终排序结果: {sorted_nums}')
    
    # print('\n' + '='*60)
    
    # # 测试升序排序
    # print('开始升序排序 (comp=lambda x, y: x > y)...')
    # nums2 = [3, 1, 4, 2]
    # sorted_nums2 = bubble_sort_descending(nums2, comp=lambda x, y: x > y)
    # print(f'\n最终排序结果: {sorted_nums2}')
    
    # print('\n' + '='*60)
    
    # # 测试按绝对值降序排序
    # print('开始按绝对值降序排序 (comp=lambda x, y: abs(x) < abs(y))...')
    # nums3 = [-3, 1, -4, 2]
    # sorted_nums3 = bubble_sort_descending(nums3, comp=lambda x, y: abs(x) < abs(y))
    # print(f'\n最终排序结果: {sorted_nums3}')


# 冒泡排序算法分析：
# ============================================================================
# 1. 算法原理：
#    冒泡排序通过重复遍历要排序的列表，比较相邻元素并根据比较结果交换它们的位置。
#    对于降序排序，每次遍历将最小的元素"沉"到列表末尾。
#
# 2. 时间复杂度：
#    - 最好情况：O(n) - 当列表已经有序时
#    - 最坏情况：O(n²) - 当列表完全逆序时
#    - 平均情况：O(n²)
#
# 3. 空间复杂度：
#    - O(1) - 原地排序，只使用了常数级别的额外空间
#
# 4. 稳定性：
#    - 稳定排序算法 - 相等元素的相对位置不会改变
#
# 5. 优化策略：
#    - 使用 swapped 标志位，当某轮没有发生交换时提前终止
#
# 6. 降序排序逻辑分析：
#    - 比较函数：comp=lambda x, y: x < y
#    - 当 x < y 时交换，即当前元素小于后一个元素时交换
#    - 这样会将较小的元素向后移动，最终形成降序排列
#
# 7. 详细交换过程（降序排序 [3, 1, 4, 2]）：
#    初始: [3, 1, 4, 2]
#    第1轮: 3<1? False → 不交换, 1<4? True → 交换 → [3, 4, 1, 2], 1<2? True → 交换 → [3, 4, 2, 1]
#    第2轮: 3<4? True → 交换 → [4, 3, 2, 1], 3<2? False → 不交换
#    第3轮: 4<3? False → 不交换 → 提前结束
#    结果: [4, 3, 2, 1]
# ============================================================================