from collections import OrderedDict  # 从 collections 模块导入 OrderedDict 类

# 创建一个空的有序字典
od = OrderedDict()

# 向有序字典中添加键值对
od['a'] = 1  # 插入键 'a'，值为 1
od['b'] = 2  # 插入键 'b'，值为 2
od['c'] = 3  # 插入键 'c'，值为 3

# 将键 'b' 移动到字典的末尾
od.move_to_end('b')  # 原本顺序为 a->b->c，移动后变为 a->c->b

# 打印字典中所有的键，以列表形式显示顺序
print(list(od.keys()))  # 输出 ['a', 'c', 'b']