"""
Version: 1.0
Author: ChatGPT
Description: 对PDF文件进行加密处理
Date: 2025-11-01
"""

from PyPDF2 import PdfReader, PdfWriter

def encrypt_pdf(input_path, output_path, password):
    
    """使用密码加密PDF文件"""
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    # 复制所有页面
    for page in reader.pages:
        writer.add_page(page)
    
    # 加密PDF
    writer.encrypt(user_password=password, owner_password=None)
    
    # 保存加密后的文件
    with open(output_path, 'wb') as f:
        writer.write(f)

# 使用示例
if __name__ == "__main__":
    encrypt_pdf('test.pdf', 'test_encrypted.pdf', 'mypassword123')