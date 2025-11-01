"""
Version: 1.0
Author: ChatGPT
Description: 检查PDF是否已加密
Date: 2025-11-01
"""
from PyPDF2 import PdfReader

def check_pdf_encryption(file_path):
    """检查PDF文件是否已加密"""
    try:
        reader = PdfReader(file_path)
        if reader.is_encrypted:
            print(f"文件 {file_path} 已加密")
            return True
        else:
            print(f"文件 {file_path} 未加密")
            return False
    except Exception as e:
        print(f"检查文件时出错: {str(e)}")
        return False

# 使用示例
if __name__ == "__main__":
    check_pdf_encryption('test_protected.pdf')