from collections import deque

dq = deque([1, 2, 3])
dq.append(4)       # 右边添加
dq.appendleft(0)   # 左边添加
dq.pop()           # 右边删除
dq.popleft()       # 左边删除

print(dq)  # deque([1, 2, 3])