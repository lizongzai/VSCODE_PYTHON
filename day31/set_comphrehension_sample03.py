prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

# 只存股票名（Key）
stocks_over_100 = {key for key, value in prices.items() if value > 100}
print(stocks_over_100)

# 只存价格（Value）
prices_over_100 = {value for value in prices.values() if value > 100}
print(prices_over_100)

# 存键值对元组（Key, Value）
items_over_100 = {(key, value) for key, value in prices.items() if value > 100}
print(items_over_100)