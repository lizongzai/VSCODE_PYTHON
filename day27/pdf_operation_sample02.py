"""
Version: 1.0
Author: ChatGPT
Description: 旋转和叠加页面
Date: 2025-11-01
"""

from PyPDF2 import PdfReader, PdfWriter

def manipulate_pdf(input_path, output_path):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    # 操作示例：对奇数页和偶数页进行不同处理
    for i, page in enumerate(reader.pages):
        if i % 2 == 0:  # 偶数页顺时针旋转
            page.rotate(90)
        else:  # 奇数页逆时针旋转
            page.rotate(-90)
        
        writer.add_page(page)
    
    # 在文档末尾添加空白页
    writer.add_blank_page()  # 使用默认尺寸
    
    # 保存文件
    with open(output_path, 'wb') as f:
        writer.write(f)

# 使用函数
if __name__ == "__main__":
    manipulate_pdf('test.pdf', 'test_output.pdf')