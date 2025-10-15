items1 = [35, 12, 99, 68, 55, 87]
items2 = [45, 8, 29]

# 列表的拼接
print("--------列表的拼接---------")
print(items1 + items2)  # [35, 12, 99, 68, 55, 87, 45, 8, 29]
print(items1 * 3)       # [35, 12, 99, 68, 55, 87, 35, 12, 99, 68, 55, 87, 35, 12, 99, 68, 55, 87]
print("--------列表的拼接---------\n")

# 列表的比较
print("--------列表的比较---------")
print(items1 > items2)   # True
print(items1 < items2)   # False
print(items1 == items2)  # False
print(items1 != items2)  # True
print("--------列表的比较---------\n")

# 列表的成员资格
print("--------列表的成员资格---------")
print(35 in items1)    # True 
print(100 in items1)   # False
print(100 not in items1) # True
print("--------列表的成员资格---------\n")

# 列表的遍历
print("--------列表的遍历---------")
for item in items1:
    print(item, end=' ')
print("\n--------列表的遍历---------\n")

# 列表的长度
print("--------列表的长度---------")
print(len(items1))  # 6
print("--------列表的长度---------\n")

# 列表的最大值和最小值
print("--------列表的最大值和最小值---------")
print(max(items1))  # 99
print(min(items1))  # 12
print("--------列表的最大值和最小值---------\n")

# 列表的求和
print("--------列表的求和---------")
print(sum(items1))  # 356
print("--------列表的求和---------\n")

# 列表的排序
print("--------列表的排序---------")
print(sorted(items1))  # [12, 35, 55, 68, 87, 99]
print(sorted(items1, reverse=True))  # [99, 87, 68, 55, 35, 12]
print("--------列表的排序---------\n")

# 列表的切片
print("--------列表的切片---------")
# items1 = [35, 12, 99, 68, 55, 87]
print(items1[1:4])  # [12, 99, 68] # 取出索引1到4的元素
print(items1[:3])   # [35, 12, 99] # 取出索引0到3的元素
print(items1[3:])   # [68, 55, 87] # 取出索引3到最后的元素
print(items1[-3:])  # [68, 55, 87] # 取出最后3个元素
print(items1[:-3])  # [35, 12, 99] # 取出所有元素，直到倒数第3个元素
print(items1[::2])  # [35, 99, 55] # 取出所有偶数索引的元素
print(items1[::-1]) # [87, 55, 68, 99, 12, 35] # 取出所有元素，倒序
print("--------列表的切片---------\n")

# 列表的复制
print("--------列表的复制---------")
list_copy = items1[:]  # 列表的切片复制
print(list_copy)  # [35, 12, 99, 68, 55, 87]
list_copy2 = items1.copy()  # 列表的copy方法复制
print(list_copy2)  # [35, 12, 99, 68, 55, 87]
list_copy3 = list(items1)  # 列表的list函数复制
print(list_copy3)  # [35, 12, 99, 68, 55, 87]
print("--------列表的复制---------\n")

# 列表的嵌套
print("--------列表的嵌套---------")
nested_list = [items1, items2]
print(nested_list)  # [[35, 12, 99, 68, 55, 87], [45, 8, 29]]
print(nested_list[0])  # [35, 12, 99, 68, 55, 87]
print(nested_list[1])  # [45, 8, 29]
print(nested_list[0][2])  # 99
print("--------列表的嵌套---------\n")

# 列表的解包
print("--------列表的解包---------")
a, b, c, d, e, f = items1
print(a, b, c, d, e, f)  # 35 12 99 68 55 87
print("--------列表的解包---------\n")
# 列表的增删改查
print("--------列表的增删改查---------")
items = [1, 2, 3]
items.append(4)  # 增加元素
print(items)  # [1, 2, 3, 4]
items.insert(1, 1.5)  # 插入元素
print(items)  # [1, 1.5, 2, 3, 4]
items.remove(1.5)  # 删除元素
print(items)  # [1, 2, 3, 4]
items[2] = 99  # 修改元素
print(items)  # [1, 2, 99, 4]
print(items.index(99))  # 查找元素索引，输出2
print(items.count(2))  # 统计元素出现次数，输出1
items.sort()  # 列表排序
print(items)  # [1, 2, 4, 99]
items.reverse()  # 列表反转
print(items)  # [99, 4, 2, 1]
print("--------列表的增删改查---------\n")
# 列表的清空
print("--------列表的清空---------")
items.clear()  # 清空列表
print(items)  # []
print("--------列表的清空---------\n")
# 列表的复制
print("--------列表的复制---------")
# 列表的合并
print("--------列表的合并---------")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)  # 合并列表
print(list1)  # [1, 2, 3, 4, 5, 6]
print