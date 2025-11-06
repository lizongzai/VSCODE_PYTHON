"""
Version: 1.0
Author: lixiaojie
Description: 冒泡排序算法--> 降序排序
Date: 2025-11-06

Keyword arguments:
argument -- description
Return: return_description
"""

def bubble_sort(items, comp=lambda x, y: x > y):
    """
    冒泡排序算法
    
    Args:
        items: 要排序的列表
        comp: 比较函数，默认是降序(x>y)，返回True时需要交换
    
    Returns:
        排序后的新列表（原列表不被修改）
    """
    items = items[:]  # 创建列表副本，不修改原列表 [3, 1, 4, 2]
    n = len(items) # n = 4
    for i in range(n - 1):
        swapped = False  # 标记本轮是否发生交换
        print(f'\n--- 第{i+1}轮冒泡排序 ---')
        
        for j in range(n - 1 - i): 
            # 第一轮的时候：range(3) → j = 0, 1, 2
            # 第二轮的时候：range(2) → j = 0, 1
            # 第三轮的时候：range(1) → j = 0
            
            # =======================================算法执行过程分析==========================================================
            # 以下注释展示了以 [3, 1, 4, 2] 降序排序为例的详细执行过程：
            #
            # 第一轮比较 (i=0): 在[3, 1, 4, 2]中从前往后比较相邻元素
            #   第一次比较：j=0，比较 itmems[j]=items[0]=3 和 itmems[j+1]=items[1]=1，3>1=True → 交换 → [1, 3, 4, 2]
            #   第二次比较：j=1，比较 itmems[j]=items[1]=3 和 itmems[j+1]=items[2]=4，3>4=False → 不交换 → [1, 3, 4, 2]
            #   第三次比较：j=2，比较 itmems[j]=items[2]=4 和 itmems[j+1]=items[3]=2，4>2=True → 交换 → [1, 3, 2, 4]
            #   第一轮排序结果: [1, 3, 2, 4]
            #
            # 第二轮比较 (i=1): 在[1, 3, 2]中比较相邻元素
            #   第一次比较：j=0，比较 itmems[j]=items[0]=1 和 itmems[j+1]=items[1]=3，1>3=False → 不交换 → [1, 3, 2, 4]
            #   第二次比较：j=1，比较 itmems[j]=items[1]=3 和 itmems[j+1]=items[2]=2，3>2=True → 交换 → [1, 2, 3, 4]
            #   第二轮排序结果: [1, 2, 3, 4]
            #
            # 第三轮比较 (i=2): 在[1, 2]中比较相邻元素
            #   第一次比较：j=0，比较 itmems[j]=items[0]=1 和 itmems[j+1]=items[1]=2，1>2=False → 不交换 → [1, 2, 3, 4]
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
    print('开始降序排序 (comp=lambda x, y: x > y)...')
    
    sorted_nums = bubble_sort(nums, comp=lambda x, y: x > y)
    print(f'\n最终排序结果: {sorted_nums}')
    
    # print('\n' + '='*60)
    
    # # 测试升序排序
    # print('开始升序排序 (comp=lambda x, y: x < y)...')
    # nums2 = [3, 1, 4, 2]
    # sorted_nums2 = bubble_sort(nums2, comp=lambda x, y: x < y)
    # print(f'\n最终排序结果: {sorted_nums2}')
    
    # print('\n' + '='*60)
    
    # # 测试按绝对值升序排序
    # print('开始按绝对值升序排序 (comp=lambda x, y: abs(x) < abs(y))...')
    # nums3 = [-3, 1, -4, 2]
    # sorted_nums3 = bubble_sort(nums3, comp=lambda x, y: abs(x) < abs(y))
    # print(f'\n最终排序结果: {sorted_nums3}')


# 冒泡排序特点说明：
# 1. 每轮将最大的元素"冒泡"到末尾（对于降序是最小的元素沉底）
# 2. 相邻元素比较，满足条件就交换
# 3. 优化：如果某轮没有发生交换，说明已经有序，提前结束
# 4. 比较函数 comp 返回 True 时交换元素

# 详细交换过程（降序排序 [3, 1, 4, 2]）：
# 初始: [3, 1, 4, 2]
# 第1轮: 3>1交换 → [1, 3, 4, 2], 3>4不交换, 4>2交换 → [1, 3, 2, 4]
# 第2轮: 1>3不交换, 3>2交换 → [1, 2, 3, 4]  
# 第3轮: 1>2不交换 → 提前结束