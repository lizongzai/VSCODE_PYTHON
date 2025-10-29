"""
Version: 1.0
Author: ChatGPT
Descrtiption: 将数据写入CSV文件.
Date: 2025-10-29

Keyword arguments:
argument -- description
Return: return_description
"""

import csv
import random

with open('scores.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file) # 创建写入对象
    writer.writerow(['姓名', '语文', '数学', '英语']) # 写入表头
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    for name in names:
        scores = [random.randrange(50, 101) for _ in range(3)]
        print(name, scores)
        scores.insert(0, name)
        writer.writerow(scores)