lst = [{}] * 3
lst[0]['a'] = 1
print(lst)
# 输出：[{'a': 1}, {'a': 1}, {'a': 1}]


lst = [[1,2], [3,4], [5,6]]
for sublist in lst:
    sublist.append(0)
print(lst)
# 输出：[[1,2,0], [3,4,0], [5,6,0]]  ✅

for sublist in lst:
    lst.remove(sublist)
print(lst)
# 输出：部分删除，结果不可预测


lst = [[0]*3 for _ in range(3)]  # 每行独立
lst2 = [[0]*3]*3  # 每行共享引用


lst = [[1,2],[3,4]]
lst_slice = lst[:]
lst_slice[0][0] = 99
print(lst)
# 输出：[[99, 2], [3, 4]]  ← 内层列表仍然共享

