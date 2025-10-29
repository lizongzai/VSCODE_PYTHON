import ujson

# 你的JSON数据
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

# 序列化为JSON字符串
json_str = ujson.dumps(data, ensure_ascii=False, indent=2)
print("JSON字符串:")
print(json_str)

# 反序列化
parsed_data = ujson.loads(json_str)
print("\n解析后的数据:")
print(f"姓名: {parsed_data['name']}")
print(f"第一辆车: {parsed_data['cars'][0]['brand']}")
print(f"第二辆车: {parsed_data['cars'][1]['brand']}")
print(f"第三辆车: {parsed_data['cars'][2]['brand']}")
