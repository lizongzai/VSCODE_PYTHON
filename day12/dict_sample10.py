stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 与zip结合使用
names = ['Apple', 'Google', 'IBM', 'Oracle', 'Accenture', 'Facebook', 'Symantec']
codes = ['AAPL', 'GOOG', 'IBM', 'ORCL', 'ACN', 'FB', 'SYMC']

# 创建名称到价格的映射
name_to_price = {name: stocks[code] for name, code in zip(names, codes)}
print(name_to_price)