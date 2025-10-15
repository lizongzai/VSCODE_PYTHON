# s = 'a,b,c,d,e,f'

# print(s.split(','))      # ['a', 'b', 'c', 'd', 'e', 'f'] - 全部分割
# print(s.split(',', 2))   # ['a', 'b', 'c,d,e,f'] - 分割2次
# print(s.split(',', 0))   # ['a,b,c,d,e,f'] - 不分割
# print(s.split(',', 1))   # ['a', 'b,c,d,e,f'] - 分割1次



# 处理CSV数据
csv_data = "John,25,Engineer,New York"
name, age, job, city = csv_data.split(',', 3)
print(f"姓名: {name}, 年龄: {age}, 职业: {job}, 城市: {city}")

# 解析URL路径
url = "https://example.com/blog/python-tutorial"
protocol, rest = url.split('://', 1)
domain, path = rest.split('/', 1)
print(f"协议: {protocol}, 域名: {domain}, 路径: {path}")

# 处理日志文件
log_line = "ERROR 2023-10-01 10:30:15 Database connection failed"
level, date, time, message = log_line.split(' ', 3)
print(f"级别: {level}, 日期: {date}, 时间: {time}, 信息: {message}")