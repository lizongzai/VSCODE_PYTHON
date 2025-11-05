"""
迭代工具模块示例
"""
import itertools

# 产生 'ABCD' 的全排列 (长度为4的所有排列)
perm = itertools.permutations('ABCD')
print("全排列:")
print(list(perm))  # 转成列表显示结果

# 产生 'ABCDE' 的五选三组合
comb = itertools.combinations('ABCDE', 3)
print("\n三元素组合:")
print(list(comb))

# 产生 'ABCD' 和 '123' 的笛卡尔积
prod = itertools.product('ABCD', '123')
print("\n笛卡尔积:")
print(list(prod))

# 产生 'ABC' 的无限循环序列 (这里只取前10个示例)
cycle_iter = itertools.cycle(('A', 'B', 'C', 'D'))
print("\n循环序列前10个元素:")
for i, val in enumerate(cycle_iter):
    if i >= 10:  # 防止无限循环
        break
    print(val, end=' ')


# 筛选工具（Filtering Tools）
data = ['A', 'B', 'C', 'D']
selectors = [1, 0, 1, 0]  # 1 表示保留，0 表示舍弃

result = list(itertools.compress(data, selectors))
print("\n条件筛选:")
print(result)


# 组合工具
result = list(itertools.chain('AB', '12', ['X','Y'])) # 把多个迭代器串联起来，相当于顺序连接
print("\n组合工具:")
print(result)


# 类似切片 islice(iterable, start, stop, step)
nums = range(10)
# 类似切片，但可以对迭代器使用，不占用额外内存
result = list(itertools.islice(nums, 2, 8, 2))  # 从索引2到7，步长2
print("\n类似切片:")
print(result)

# 对每个元素解包作为参数调用函数 starmap(function, iterable)
pairs = [(2,3), (3,2), (4,1)]
result = list(itertools.starmap(pow, pairs))  # 等同于 [2**3, 3**2, 4**1]
print("\n对每个元素解包:")
print(result)

# 打包
# 像 zip 一样打包，但长度不一致时用 fillvalue 填充
result = list(itertools.zip_longest('AB', '123', fillvalue='*'))
print("\n打包填充:")
print(result)
