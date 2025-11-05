from collections import ChainMap  # 从 collections 模块导入 ChainMap，用于将多个字典组合成一个视图

# 定义两个普通字典
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# 创建一个 ChainMap，将 dict1 和 dict2 组合成一个视图
cm = ChainMap(dict1, dict2)
# 查找键时，按顺序在各个字典中查找，找到第一个就返回

# 访问键 'a'
print(cm['a'])

# 访问键 'b'
# 'b' 在 dict1 和 dict2 中都存在，但 ChainMap 会先查 dict1
# ChainMap 的查找规则是按顺序从左到右查找字典，找到第一个匹配的键就返回对应的值，而不会继续查找后面的字典。
print(cm['b'])  # 输出 2

# 访问键 'c'
# 'c' 不在 dict1 中，在 dict2 中存在
print(cm['c'])  # 输出 4