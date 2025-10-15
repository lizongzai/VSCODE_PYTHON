A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {4, 5}

# 检查是否所有元素都在另一个集合中
print(all(x in B for x in A))  # True
print(all(x in B for x in C))  # True

# 使用内置方法（更高效）
print(A.issubset(B))  # True
print(C.issubset(B))  # True
