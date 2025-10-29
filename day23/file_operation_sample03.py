"""
Version: 1.0
Author: ChatGPT
Description: 从CSV文件读取数据并打印每个学生的姓名和对应的分数。
Date: 2025-10-29

Keyword arguments:
argument -- description
Return: return_description
"""
import csv
with open('scores.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='|', quoting=csv.QUOTE_ALL)  # 创建读取对象
    header = next(reader)  # 读取表头
    print(f"{header[0]:<10} {header[1]:<6} {header[2]:<6} {header[3]:<6}")  # 打印表头
    
    for row in reader:
        if not row or len(row) < 4:  # 检查行是否为空或列数是否少于4
            continue  # 跳过空行
        name = row[0]
        scores = list(map(int, row[1:]))
        print(f"{name:<10} {scores[0]:<6} {scores[1]:<6} {scores[2]:<6}")  # 打印每个学生的姓名和分数
        print(f"总分: {sum(scores):<6} 平均分: {sum(scores)/len(scores):<6.2f}")
        