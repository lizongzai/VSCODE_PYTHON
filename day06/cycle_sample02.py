"""
每隔1秒输出一次“hello, world”，持续1小时

Author: 骆昊
Version: 1.0
"""
import time

for i in range(3600):
    print('hello, world')
    time.sleep(1)