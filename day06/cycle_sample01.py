"""
Version: 1.0
Author: 李小婕
Description: 每间隔1秒钟打印输出 hello world!，持续一个小时共打印5次
Date: 2025-10-13

Keyword arguments:
argument -- description
Return: return_description
"""
print("--------循环打印---------")
import time # 导入时间模块
count = 0   # 计数器初始化
while count < 5: # 循环5次
    print("hello world!") # 打印输出
    count += 1 # 计数器加1
    time.sleep(2) # 每次循环后暂停1秒钟
print("--------循环打印---------\n")