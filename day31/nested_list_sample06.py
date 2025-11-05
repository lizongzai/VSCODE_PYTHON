# 坑：直接用 * 或赋值复制嵌套列表时，内层列表会共享引用，修改一个会影响其他。
# 错误示例
matrix = [[0]*3]*3
matrix[0][0] = 1
print(matrix)
# 输出：
# [[1, 0, 0],
#  [1, 0, 0],
#  [1, 0, 0]]  ← 所有行都被修改了

# 原因：[[0]*3]*3 创建了 3 个指向同一个内层列表的引用。


import copy
matrix2 = copy.deepcopy(matrix)


# ✅ 解决方法：
matrix = [[0]*3 for _ in range(3)]
matrix[0][0] = 1
print(matrix)
# 输出：
# [[1, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]



