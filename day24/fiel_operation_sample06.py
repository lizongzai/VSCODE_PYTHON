"""
Version: 1.0
Author: ChatGPT
Description: 使用openpyxl的只写模式创建包含柱状图的Excel文件示例代码。
Date: 2025-10-30

Keyword arguments:
argument -- description
Return: return_description
"""

from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

# 创建一个只写的工作簿
workbook = Workbook(write_only=True)

# 创建一个表单
sheet = workbook.create_sheet()

# 准备数据
data = [
    ('类别', '销售A组', '销售B组'),
    ('手机', 40, 30),
    ('平板', 50, 60),
    ('笔记本', 80, 70),
    ('外围设备', 20, 10),
]

# 向表单中添加行
for row in data:
    sheet.append(row)

# 创建图表对象
chart = BarChart()

# 设置图表的样式
chart.type = 'col'
# 设置图表的样式
chart.style = 10
# 设置图表的标题
chart.title = '销售统计图'
# 设置图表纵轴的标题
chart.y_axis.title = '销量'
# 设置图表横轴的标题
chart.x_axis.title = '商品类别'
# 设置数据的范围
data = Reference(sheet, min_col=2, min_row=1, max_row=5, max_col=3)
# 设置分类的范围
cats = Reference(sheet, min_col=1, min_row=2, max_row=5)
# 给图表添加数据
chart.add_data(data, titles_from_data=True)
# 给图表设置分类
chart.set_categories(cats)
chart.shape = 4
# 将图表添加到表单指定的单元格中
sheet.add_chart(chart, 'A10')

# 保存工作簿
workbook.save('demo.xlsx')