"""
Version: 1.0
Author: Lixiaojie
Description: 将json写入文本文件
Date: 2025-10-27

Keyword arguments:
argument -- description
Return: return_description
"""
import json
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'skills': ['Python', 'Machine Learning', 'Data Analysis']
}

with open('data.json', 'w') as json_file:
    json.dump(data, json_file)
print("JSON数据已写入data.json文件")
