import os
import requests
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

def download_fonts_and_create_pdf():
    # 创建resources文件夹
    os.makedirs('resources/fonts', exist_ok=True)
    
    # 免费字体URL（示例）
    font_urls = {
        'Vera.ttf': 'https://github.com/opensourcedesign/fonts/raw/master/gnu-freefont_freepoc/FreeMono.ttf',
        '青呱石头体.ttf': ''  # 需要找到合适的中文字体URL
    }
    
    # 下载字体（这里只是示例，实际需要可用的字体URL）
    print("请手动下载字体文件到 resources/fonts/ 目录")
    print("推荐下载免费字体如：")
    print("- 文泉驿微米黑")
    print("- 思源黑体")
    print("- 方正免费字体")
    
    # 使用默认字体创建PDF
    create_pdf_with_default_fonts()

def create_pdf_with_default_fonts():
    pdf_canvas = canvas.Canvas('default_font_demo.pdf', pagesize=A4)
    width, height = A4
    
    # 使用ReportLab内置字体
    available_fonts = ['Helvetica', 'Helvetica-Bold', 'Times-Roman', 'Courier']
    
    for i, font_name in enumerate(available_fonts):
        pdf_canvas.setFont(font_name, 20)
        pdf_canvas.setFillColorRGB(i*0.2, 0.5, 0.3)
        pdf_canvas.drawString(50, height - 100 - i*30, f'This is {font_name} font')
    
    pdf_canvas.showPage()
    
    # 第二页：图形和旋转
    pdf_canvas.setFont('Helvetica-Bold', 36)
    pdf_canvas.setFillColorRGB(0.8, 0.2, 0.2)
    pdf_canvas.drawString(width//2-100, height//2, 'PDF Creation')
    pdf_canvas.setFillColorRGB(0.2, 0.2, 0.8)
    pdf_canvas.drawString(width//2-80, height//2-50, 'Successful!')
    
    pdf_canvas.save()
    print("使用默认字体创建PDF完成: default_font_demo.pdf")

# 执行
create_pdf_with_default_fonts()