prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

# (方法一)推导式部分：
# 用股票价格大于100元的股票构造一个新的字典
prices2 = {key: value for key, value in prices.items() if value > 100}
print(prices2)


# (方法二)等价于传统写法：
prices3 = {}
for key, value in prices.items():
    if value > 100:
        prices3[key] = value
print(prices3)