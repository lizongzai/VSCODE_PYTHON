from collections import namedtuple  # 从 collections 模块导入 namedtuple，用于创建命名元组

# 定义一个名为 Point 的命名元组，包含两个字段 'x' 和 'y'
Point = namedtuple('Point', ['x', 'y'])

# 创建一个 Point 实例，x=10, y=20
p = Point(10, 20)

# 通过字段名访问元组的值
print(p.x)  # 输出 10，访问 x 字段
print(p.y)  # 输出 20，访问 y 字段

# 打印整个命名元组对象，会显示字段名和对应值
print(p)    # 输出 Point(x=10, y=20)