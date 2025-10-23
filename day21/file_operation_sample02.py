"""
Version: 1.0
Author: 李小婕
Description: 传统方式读取整个文件和使用with上下文管理器读取文件的方法
Date: 2025-10-23
"""


# 第一种方式：传统方式读取整个文件
file = open('致橡树.txt', 'r', encoding='utf-8')
print(file.read())
file.close() # 如果这里发生异常，文件不会关闭！可能执行不到这里

# 第二种方式：使用 with 语句（推荐）读取整个文件,文件已自动关闭
with open('致橡树.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# 逐行读取
with open('致橡树.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())  # strip() 移除换行符

# 读取所有行到列表
with open('致橡树.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(lines)
