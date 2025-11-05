from collections import defaultdict  # 从 collections 模块导入 defaultdict，用于创建带默认值的字典

# 创建一个 defaultdict，默认值类型为 int（即默认值为 0）
dd = defaultdict(int)  # 如果访问不存在的键，会自动生成一个默认值 0

# 给键 'apple' 增加 1（如果键不存在，会先用默认值 0 初始化）
dd['apple'] += 1  # 'apple' 原本不存在，先变为 0，然后加 1 => 1

# 给键 'banana' 增加 2
dd['banana'] += 2  # 'banana' 原本不存在，先变为 0，然后加 2 => 2

# 打印键 'apple' 的值
print(dd['apple'])   # 输出 1

# 打印键 'orange' 的值
# 'orange' 不存在，会自动创建并赋值为默认值 0
print(dd['orange'])  # 输出 0