"""
Version: 1.0
Author: ChatGPT
Description: 
例如在当前文件夹下有一个名为“2022年股票数据.xlsx”的 Excel 文件，
如果想读取并显示该文件的内容，可以通过如下所示的代码来完成。
Date: 2025-10-29

Keyword arguments:
argument -- description
Return: return_description
"""
import openpyxl

workbook = openpyxl.load_workbook('2022年股票数据.xlsx')  # 打开Excel文件
sheet = workbook.active  # 获取活动的工作表
for row in sheet.iter_rows(values_only=True):  # 遍历每一行
    print(row)  # 打印每一行的数据 
workbook.close()  # 关闭Excel文件