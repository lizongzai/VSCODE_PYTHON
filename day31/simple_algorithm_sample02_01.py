"""
Version: 1.0
Author: lixiaojie
Description: 简单排序法，升序排序. 在每次一轮排序完成之后，才开始进行位置交换。
Date: 2025-11-05

Keyword arguments:
argument -- description
Return: return_description
"""

def select_sort_verbose(items, comp=lambda x, y: x < y):
    """
    选择排序，带详细内层循环打印，显示 min_index 变化
    """
    items = items[:]
    n = len(items) # n = 4, i = 0, item[0,1,2,3] =[3, 1, 4, 2]
    
    for i in range(n - 1):
        min_index = i
        print(f"\n第{i+1}轮开始，假设当前位置 i={i} 最优元素 items[{i}]={items[i]}")
        
        for j in range(i + 1, n):
            # =======================================第一轮比较=========================================================================
            # 初始化：当 i = 0, j =1， min_index=0 时，初始化排序[3, 1, 4, 2], 如下开始排序：
            # 第一次比较x < y： j =1 , min_index=0， items[j] =items[1] = 1， items[min_index]=items[0] = 3 ---> min_index =1
            # 结果： 1 < 3 ---> true, j =2, min_index=1

            # 第二次比较x < y： j =2 , min_index=1， items[j] =items[2] = 4， items[min_index]=items[1] = 1 ---> min_index =1
            # 结果： 4 < 1 ---> false, j =3, min_index=1
            
            # 第三次比较x < y： j =3 , min_index=1， items[j] =items[3] = 2， items[min_index]=items[1] = 1 ---> min_index =1
            # 结果： 2 < 1 ---> false, j = 4, min_index=1, i = 0,
            # 交换 items[0]=3 和 items[1]=1
            # 第一轮排序输出的结果：[1，3，4，2]
            
            # =======================================第二轮比较=========================================================================
            # 初始化：当 i = 1, j =2， min_index=1时，如下开始排序：
            # 第一次比较x < y： j =2 , min_index=1， items[j] =items[2] = 4， items[min_index]=items[1] = 3 ---> min_index =1
            # 结果： 4 < 3 ---> false, j =3, min_index=1
            # 第二次比较x < y： j =3 , min_index=1， items[j] =items[3] = 2， items[min_index]=items[1] = 3 ---> min_index =3
            # 结果： 2 < 3 ---> true, j =4, min_index=3
            # 交换 items[1]=3 和 items[3]=2
            # 第二轮排序输出的结果：[1，2，4，3]
           
            # =======================================第三轮比较=========================================================================
            # 初始化：当 i = 2, j =3， min_index=2时，如下开始排序：
            # 第一次比较x < y： j =3 , min_index=2， items[j] =items[3] = 3， items[min_index]=items[2] = 4 ---> min_index =3
            # 结果： 3 < 4 ---> true, j =4, min_index=3
            # 交换 items[2]=4 和 items[3]=3
            # 第三轮排序输出的结果：[1，2，3，4]
            
            
            if comp(items[j], items[min_index]):
                min_index = j
                changed = True
            else:
                changed = False
            # 打印每一次比较的状态
            print(f"  比较 items[{j}]={items[j]} 与 items[{min_index}]={items[min_index]} -> min_index={'更新' if changed else '不变'}")
        
        # 内层循环结束，交换位置 i 和 min_index
        # i = 0, min_index=1
        items[i], items[min_index] = items[min_index], items[i]
        print(f"  交换 items[{i}]={items[i]} 和 items[{min_index}]={items[min_index]} -> 列表现在: {items}")
    
    return items


if __name__ == "__main__":
    # 测试示例，使用升序排序（x < y）
    nums = [3, 1, 4, 2]
    print("原始列表:", nums)
    sorted_nums = select_sort_verbose(nums, comp=lambda x, y: x < y)
    print("\n最终排序结果:", sorted_nums)


# 只交换两个位置：
# 位置 0 和位置 1 的元素互换
# 交换过程：
# text
# 交换前: [3, 1, 4, 2]
#          ↑  ↑
#          0  1   (要交换的两个位置)

# 交换后: [1, 3, 4, 2]
#          ↑  ↑
#          0  1   (这两个位置的值互换了)


#初始: [3, 1, 4, 2]
#第1轮: 找到最小值1 → [1, 3, 4, 2]
#第2轮: 找到次小值2 → [1, 2, 4, 3]  
#第3轮: 找到第三小值3 → [1, 2, 3, 4]

# 详细交换过程说明：
# 第1轮交换：位置0(3) ↔ 位置1(1) → [1, 3, 4, 2]
# 第2轮交换：位置1(3) ↔ 位置3(2) → [1, 2, 4, 3]  
# 第3轮交换：位置2(4) ↔ 位置3(3) → [1, 2, 3, 4]