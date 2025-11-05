from collections import deque  # 从 collections 模块导入 deque，用于创建双端队列

# 创建一个 deque 对象，初始化元素为 [1, 2, 3]
dq = deque([1, 2, 3])

# 在右边（尾部）添加元素 4
dq.append(4)       # deque 变为 deque([1, 2, 3, 4])

# 在左边（头部）添加元素 0
dq.appendleft(0)   # deque 变为 deque([0, 1, 2, 3, 4])

# 从右边（尾部）删除元素
dq.pop()           # 删除 4，deque 变为 deque([0, 1, 2, 3])

# 从左边（头部）删除元素
dq.popleft()       # 删除 0，deque 变为 deque([1, 2, 3])

# 打印当前 deque 的内容
print(dq)  # 输出 deque([1, 2, 3])