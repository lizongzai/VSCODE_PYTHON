"""
Version: 1.0
Author: Lixiaojie
Description: 读取json文件并将打印输出内容
Date: 2025-10-27

Keyword arguments:
argument -- description
Return: return_description
"""
import json
with open('data.json', 'r') as json_file:
    data = json.load(json_file)
print(data)
