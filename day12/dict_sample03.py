# 字典中的值又是一个字典(嵌套的字典)
students = {
    1001: {'name': '狄仁杰', 'sex': True, 'age': 22, 'place': '山西大同'},
    1002: {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'},
    1003: {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}
}

# 使用get方法通过键获取对应的值，如果取不到不会引发KeyError异常而是返回None或设定的默认值
print(students.get(1002))    # {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'}
print(students.get(1005))    # None
print(students.get(1005, {'name': '无名氏'}))    # {'name': '无名氏'}

# 获取字典中所有的键
print(students.keys())      # dict_keys([1001, 1002, 1003])
# 获取字典中所有的值
print(students.values())    # dict_values([{...}, {...}, {...}])
# 获取字典中所有的键值对
print(students.items())     # dict_items([(1001, {...}), (1002, {....}), (1003, {...})])
# 对字典中所有的键值对进行循环遍历
for key, value in students.items():
    print(key, '--->', value)

# 使用pop方法通过键删除对应的键值对并返回该值
stu1 = students.pop(1002)
print(stu1)             # {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'}
print(len(students))    # 2
# stu2 = students.pop(1005)    # KeyError: 1005
stu2 = students.pop(1005, {})
print(stu2)             # {}

# 使用popitem方法删除字典中最后一组键值对并返回对应的二元组
# 如果字典中没有元素，调用该方法将引发KeyError异常
key, value = students.popitem()
print(key, value)    # 1003 {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}

# 如果这个键在字典中存在，setdefault返回原来与这个键对应的值
# 如果这个键在字典中不存在，向字典中添加键值对，返回第二个参数的值，默认为None
result = students.setdefault(1005, {'name': '方启鹤', 'sex': True})
print(result)        # {'name': '方启鹤', 'sex': True}
print(students)      # {1001: {...}, 1005: {...}}

# 使用update更新字典元素，相同的键会用新值覆盖掉旧值，不同的键会添加到字典中
others = {
    1005: {'name': '乔峰', 'sex': True, 'age': 32, 'place': '北京大兴'},
    1010: {'name': '王语嫣', 'sex': False, 'age': 19},
    1008: {'name': '钟灵', 'sex': False}
}
students.update(others)
print(students)      # {1001: {...}, 1005: {...}, 1010: {...}, 1008: {...}}