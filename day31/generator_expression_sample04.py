prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

# 取出生成器的元素
stocks_over_100_gen = (key for key, value in prices.items() if value > 100)
for stock in stocks_over_100_gen:
    print(stock)


# 只生成价格（Value）
prices_over_100_gen = (value for value in prices.values() if value > 100)
for price in prices_over_100_gen:
    print(price)
    
# 生成键值对元组（Key, Value）
items_over_100_gen = ((key, value) for key, value in prices.items() if value > 100)
for item in items_over_100_gen:
    print(item)
