import numpy as np

# 示例数据
data = [12, 18, 25, 30, 15]

# 计算统计量
mean_val = np.mean(data)           # 均值
median_val = np.median(data)       # 中位数
range_val = np.ptp(data)           # 极差（最大值-最小值）
var_val = np.var(data, ddof=1)     # 样本方差，ddof=1 表示除以 n-1
std_val = np.std(data, ddof=1)     # 样本标准差
cv_val = std_val / mean_val        # 变异系数

# 输出描述性统计信息
print(f'均值: {mean_val}')
print(f'中位数: {median_val}')
print(f'极差: {range_val}')
print(f'方差: {var_val}')
print(f'标准差: {std_val}')
print(f'变异系数: {cv_val:.2f}')
