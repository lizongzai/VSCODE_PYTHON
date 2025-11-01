"""
Version: 1.0
Author: ChatGPT
Description: 使用pypdf对PDF文件进行加密
Date: 2025-11-01
"""

# 首先安装：pip install pypdf
from pypdf import PdfReader, PdfWriter

def encrypt_with_pypdf(input_path, output_path, password):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    # 添加所有页面
    for page in reader.pages:
        writer.add_page(page)
    
    # 添加一些元数据
    writer.add_metadata(reader.metadata)
    
    # 加密
    writer.encrypt(
        user_password=password,
        owner_password=None,
        use_128bit=True
    )
    
    with open(output_path, 'wb') as f:
        writer.write(f)
        
if __name__ == "__main__":
    encrypt_with_pypdf('test.pdf', 'test_pypdf.pdf', 'user123')        