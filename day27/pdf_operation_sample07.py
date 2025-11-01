"""
Version: 1.0
Author: ChatGPT
Description: 对PDF文件进行批量加密处理
Date: 2025-11-01
"""

import os
from PyPDF2 import PdfReader, PdfWriter

def batch_encrypt_pdfs(input_folder, output_folder, password):
    """批量加密文件夹中的所有PDF文件"""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.pdf'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"encrypted_{filename}")
            
            try:
                reader = PdfReader(input_path)
                writer = PdfWriter()
                
                for page in reader.pages:
                    writer.add_page(page)
                
                writer.encrypt(user_password=password)
                
                with open(output_path, 'wb') as f:
                    writer.write(f)
                
                print(f"成功加密: {filename}")
                
            except Exception as e:
                print(f"加密失败 {filename}: {str(e)}")

# 使用示例
batch_encrypt_pdfs('./pdfs', './encrypted_pdfs', 'securepassword')