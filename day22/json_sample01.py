"""
Version: 1.0
Author: ChatGPT
Description: python json模块示例，将字典转换为JSON字符串并打印输出
Date: 2024-06-15
Keyword arguments:
argument -- description
Return: return_description
"""
import json

my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
print(json.dumps(my_dict))