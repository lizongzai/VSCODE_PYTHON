"""
Version: 1.0
Author: ChatGPT
Description: 对PDF文件进行加密,设置不同权限的加密
Date: 2025-11-01
"""

from PyPDF2 import PdfReader, PdfWriter

def encrypt_with_permissions(input_path, output_path, password):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    for page in reader.pages:
        writer.add_page(page)
    
    # 设置加密和权限
    writer.encrypt(
        user_password=password,           # 用户密码（打开文件需要）
        owner_password="owner123",        # 所有者密码
        use_128bit=True,                  # 使用128位加密
        permissions_flag=0b11110000       # 权限标志
    )
    
    with open(output_path, 'wb') as f:
        writer.write(f)

# 使用示例
encrypt_with_permissions('test.pdf', 'test_protected.pdf', 'userpass')