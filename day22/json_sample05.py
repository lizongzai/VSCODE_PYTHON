"""
Version: 1.0
Author: Lixiaojie
Description: 从文件读取JSON数据,并序列化为Python对象，反序列化为JSON字符串
Date: 2025-10-27

Keyword arguments:
argument -- description
Return: return_description
"""
import ujson
data = {
    "name": "骆昊",
    "age": 40,
    "friends": ["王大锤", "白元芳"],
    "cars": [
        {"brand": "BMW", "max_speed": 240},
        {"brand": "Benz", "max_speed": 280},
        {"brand": "Audi", "max_speed": 280}
    ]
}

# 序列化为JSON字符串并写入文件
with open('data_ujson.json', 'w') as json_file:
    ujson.dump(data,json_file,ensure_ascii=False, indent=2)
print("JSON数据已写入data_ujson.json文件")  

# 从文件读取JSON数据并反序列化为Python对象
with open('data_ujson.json', 'r') as json_file:
    paresed_data = ujson.load(json_file)
print("\n解析后的数据:")
print(f"姓名: {paresed_data['name']}")
print(f"第一辆车: {paresed_data['cars'][0]['brand']}")
print(f"第二辆车: {paresed_data['cars'][1]['brand']}")
print(f"第三辆车: {paresed_data['cars'][2]['brand']}")

