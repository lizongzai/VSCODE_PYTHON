"""
Version: 1.0
Author: 李小婕
Description: 写入文件的两种方法：覆盖写入和追加内容写入
Date: 2025-10-23
"""

# 写入文件（覆盖）
with open('example.txt', 'w', encoding='utf-8') as file:
    file.write('Hello, World!\n')
    file.write('This is a new line.\n')

# 追加内容
with open('example.txt', 'a', encoding='utf-8') as file:
    file.write('This line is appended.\n')