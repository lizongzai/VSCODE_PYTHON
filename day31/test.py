def select_sort_verbose(items, comp=lambda x, y: x < y):
    """
    选择排序，带详细内层循环打印，显示 min_index 变化
    """
    items = items[:]
    n = len(items) # n = 4, i = 0, item[0,1,2,3] =3, 1, 4, 2
    
    for i in range(n - 1):
        min_index = i
        print(f"\n第{i+1}轮开始，假设当前位置 i={i} 最优元素 items[{i}]={items[i]}")
        
        for j in range(i + 1, n):
            # 初始化： j =1， min_index=0
            # 第一轮比较x > y： j =1 , min_index=0， items[j] =items[1] = 1， items[min_index]=items[0] = 3 ---> min_index =0
            # 结果： 1 > 3 ---> false, j =2, min_index=0
            
            # 第二轮比较x > y： j =2 , min_index=0， items[j] =items[2] = 4， items[min_index]=items[0] = 3 ---> min_index =2
            # 结果： 4 > 3 ---> true, j =3, min_index=2,
            
            # 第三轮比较x > y： j =3 , min_index=2， items[j] =items[3] = 2， items[min_index]=items[2] = 4 ---> min_index =2
            # 结果： 2 > 4, j = 4, min_index=2, i = 0,
            
            if comp(items[j], items[min_index]):
                min_index = j
                changed = True
            else:
                changed = False
            # 打印每一次比较的状态
            print(f"  比较 items[{j}]={items[j]} 与 items[{min_index}]={items[min_index]} -> min_index={'更新' if changed else '不变'}")
        
        # 内层循环结束，交换位置 i 和 min_index
        # i = 0, min_index=2
        items[i], items[min_index] = items[min_index], items[i]
        print(f"  交换 items[{i}]={items[i]} 和 items[{min_index}]={items[min_index]} -> 列表现在: {items}")
    
    return items


# 测试示例，降序排序
nums = [3, 1, 4, 2]
sorted_nums = select_sort_verbose(nums, comp=lambda x, y: x > y)
print("\n最终排序结果:", sorted_nums)


# 只交换两个位置：

# 位置 0 和位置 2 的元素互换

# 位置 1 和位置 3 的元素保持不变

# 交换过程：

# text
# 交换前: [3, 1, 4, 2]
#          ↑     ↑
#          0     2   (要交换的两个位置)

# 交换后: [4, 1, 3, 2]
#          ↑     ↑
#          0     2   (这两个位置的值互换了)