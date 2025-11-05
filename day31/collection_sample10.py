from collections import namedtuple

# 定义命名元组
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)

print(p.x)  # 10
print(p.y)  # 20
print(p)    # Point(x=10, y=20)