"""
Version: 1.0
Author: ChatGPT
Description: 该脚本演示了如何使用contextlib.redirect_stdout来重定向标准输出流。
1. 将输出重定向到文件。
2. 将输出重定向到字符串缓冲区。
3. 临时重定向输出流。
4. 适用于需要捕获或重定向输出的场景，如日志记录、测试等。
Keyword arguments:
argument -- description
Return: return_description
"""

import sys
from contextlib import redirect_stdout
import io

def main():
    
    # 设置正确的编码,否则文字出现乱码
    if sys.stdout.encoding.lower() != 'utf-8': # 确保控制台输出为utf-8编码
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    # 原始输出
    print("1. 这是正常的控制台输出")
    
    # 重定向到文件
    print("\n2. 重定向到文件:")
    with open('output.txt', 'w', encoding='utf-8') as f:
        with redirect_stdout(f):
            print("这条消息会被写入到output.txt文件中")
            print("而不是显示在控制台上")
    
    # 读取文件内容并显示
    with open('output.txt', 'r', encoding='utf-8') as f:
        file_content = f.read()
    print(f"文件内容: {file_content}")
    
    # 重定向到字符串缓冲区
    print("\n3. 重定向到字符串缓冲区:")
    f = io.StringIO()
    with redirect_stdout(f):
        print("这条消息被重定向到字符串缓冲区")
        print("可以稍后获取并处理")
    
    # 获取缓冲区内容
    captured_output = f.getvalue()
    print(f"捕获的输出: {captured_output}")
    
    # 临时重定向示例
    print("\n4. 临时重定向示例:")
    original_stdout = sys.stdout
    try:
        sys.stdout = io.StringIO()
        print("这条消息被临时重定向")
        print("可以继续处理...")
        temp_output = sys.stdout.getvalue()
    finally:
        sys.stdout = original_stdout
    
    print(f"临时重定向期间捕获的内容: {temp_output}")

if __name__ == "__main__":
    main()