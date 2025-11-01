"""
Version: 1.0
Author: ChatGPT
Description: 从PDF中提取文本
Date: 2025-11-01

Keyword arguments:
argument -- description
Return: return_description
"""

# 使用PyPDF2
import PyPDF2

with(open('test.pdf', 'rb')) as file:
    reader = PyPDF2.PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    print("=" * 60)
    print(text)

# 或使用pdfplumber（更准确）
import pdfplumber
with pdfplumber.open('test.pdf') as pdf:
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    print("=" * 60)
    print(text)        