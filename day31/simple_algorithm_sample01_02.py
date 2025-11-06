"""
Version: 1.0
Author: lixiaojie
Description: 简单排序法，降序排序. 在每次一轮排序完成之后，才开始进行位置交换。
Date: 2025-11-05

Keyword arguments:
argument -- description
Return: return_description
"""

def select_sort_verbose(items, comp=lambda x, y: x < y):
    """
    选择排序，带详细内层循环打印，显示 min_index 变化
    
    Args:
        items: 要排序的列表
        comp: 比较函数，默认是升序(x<y)，这里测试使用降序(x>y)
    
    Returns:
        排序后的新列表（原列表不被修改）
    """
    # 创建原列表的副本，避免修改原列表
    items = items[:]
    n = len(items)  # 获取列表长度
    
    # 外层循环：遍历每个位置，除了最后一个（因为最后一个会自动就位）
    for i in range(n - 1):
        # 假设当前位置的元素是最优的（最小或最大，取决于comp函数）
        min_index = i
        print(f"\n第{i+1}轮开始，假设当前位置 i={i} 最优元素 items[{i}]={items[i]}")
        
        # 内层循环：从当前位置的下一个元素开始，比较找到真正的最优元素
        for j in range(i + 1, n):
            # =======================================算法执行过程分析==========================================================
            # 以下注释展示了以 [3, 1, 4, 2] 降序排序为例的详细执行过程：
            #
            # 第一轮比较 (i=0):
            #   初始化：当 i=0, j=1, min_index=0 时，初始化排序[3, 1, 4, 2]
            #   第一次比较：j=1, min_index=0，比较 1>3=False → min_index=0
            #   第二次比较：j=2, min_index=0，比较 4>3=True → min_index=2
            #   第三次比较：j=3, min_index=2，比较 2>4=False → min_index=2
            #   交换 items[0]=4 和 items[2]=3
            #   第一轮排序输出的结果：[4, 1, 3, 2]
            #
            # 第二轮比较 (i=1):
            #   初始化：当 i=1, j=2, min_index=1 时
            #   第一次比较：j=2, min_index=1，比较 3>1=True → min_index=2
            #   第二次比较：j=3, min_index=2，比较 2>3=False → min_index=2
            #   交换 items[1]=3 和 items[2]=1
            #   第二轮排序输出的结果：[4, 3, 1, 2]
            #
            # 第三轮比较 (i=2):
            #   初始化：当 i=2, j=3, min_index=2 时
            #   第一次比较：j=3, min_index=2，比较 2>1=True → min_index=3
            #   交换 items[2]=2 和 items[3]=1
            #   第三轮排序输出的结果：[4, 3, 2, 1]
            # ==============================================================================================================
            
            # 使用比较函数判断当前元素是否比当前最优元素更优
            if comp(items[j], items[min_index]):
                # 如果更优，更新最优元素的索引
                min_index = j
                changed = True
            else:
                changed = False
            
            # 打印每一次比较的详细状态，便于理解算法执行过程
            print(f"  比较 items[{j}]={items[j]} 与 items[{min_index}]={items[min_index]} -> min_index={'更新' if changed else '不变'}")
        
        # 内层循环结束，此时min_index指向当前未排序部分的最优元素
        # 将最优元素交换到当前位置i
        # 示例：i=0, min_index=2 时，交换位置0和位置2的元素
        items[i], items[min_index] = items[min_index], items[i]
        print(f"  交换 items[{i}]={items[i]} 和 items[{min_index}]={items[min_index]} -> 列表现在: {items}")
    
    return items


if __name__ == "__main__":
    # 测试示例，使用降序排序（x > y）
    nums = [3, 1, 4, 2]
    print("原始列表:", nums)
    print("开始降序排序...")
    
    # 调用选择排序函数，comp=lambda x, y: x > y 表示降序排序
    sorted_nums = select_sort_verbose(nums, comp=lambda x, y: x > y)
    print("\n最终排序结果:", sorted_nums)
    
    # 补充说明：如果要改为升序排序，使用 comp=lambda x, y: x < y
    print("\n" + "="*50)
    print("补充说明：")
    print("升序排序使用: comp=lambda x, y: x < y")
    print("降序排序使用: comp=lambda x, y: x > y")