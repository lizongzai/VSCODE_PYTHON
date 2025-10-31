"""
Version: 1.0
Author: ChatGPT
Description: 对于一个已经存在的 Word 文件，我们可以通过下面的代码去遍历它所有的段落并获取对应的内容。
Date: 2025-10-31

Keyword arguments:
argument -- description
Return: return_description
"""
from docx import Document
from docx.document import Document as Doc

document = Document('resources/离职证明.docx')
for no, p in enumerate(document.paragraphs):
    print(no, p.text)