# 在条件语句中直接使用
allowed_domains = {"gmail.com", "yahoo.com", "hotmail.com"}
user_email = "user@gmail.com"

domain = user_email.split('@')[-1]
if domain in allowed_domains:
    print("邮箱域名有效")
else:
    print("请使用支持的邮箱域名")

# 在循环中过滤
data = [("apple", 1.2), ("banana", 0.8), ("orange", 1.5), ("grape", 2.0)]
available_fruits = {"apple", "orange", "mango"}

# 只处理可用的水果
for fruit, price in data:
    if fruit in available_fruits:
        print(f"{fruit}: ${price}")