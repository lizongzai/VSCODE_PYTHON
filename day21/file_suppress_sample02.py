"""
Version: 1.0
Author: 李小婕
Description:使用suppress来抑制数据处理中的特定异常
1.通过列表处理数据转换异常
2.通过字典操作抑制键错误异常

Keyword arguments:
argument -- description
Return: return_description
"""

from contextlib import suppress
import os

def data_processing_suppress():
    """数据处理中的异常抑制"""
    
    print("=== 数据处理抑制 ===")
    
    data_list = ['123', '456', 'abc', '789', 'def']
    
    # 1. 转换数据，忽略转换错误
    numbers = []
    for item in data_list:
        with suppress(ValueError):
            num = int(item) # 尝试将字符串转换为整数
            numbers.append(num) # 只有转换成功的才添加到列表中
            print(f"成功转换: {item} -> {num}")
    
    print(f"最终数字列表: {numbers}")
    
    # 2. 字典操作抑制
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    
    with suppress(KeyError):
        value = my_dict['d']  # 尝试访问不存在的键
        print(f"获取的值: {value}")
    print("键不存在时继续执行")
    
    print("数据处理完成\n")

# 运行数据处理示例
data_processing_suppress()


my_dict = {'a': 1, 'b': 2, 'c': 3}

# 这行代码的意思是：从字典中获取键 'd' 对应的值，并赋值给变量 value
# value = my_dict['d']  # 主要目的是获取值，不是检查存在性