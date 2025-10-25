"""
Version: 1.0
Author: 李小婕
Description: 
1.基础文件操作抑制
2.使用 contextlib.suppress 来抑制文件操作中的特定异常
3.删除文件时抑制文件未找到异常
4.创建目录时抑制目录已存在异常
5.抑制多个异常类型的示例

Keyword arguments:
argument -- description
Return: return_description
"""

from contextlib import suppress
import os

def basic_suppress_examples():
    """基础抑制示例"""
    
    print("=== 基础文件操作抑制 ===")
    
    # 1. 删除文件（如果文件不存在也不报错）
    with suppress(FileNotFoundError):
        os.remove('temp_file.txt')
        print("文件已删除")
    print("继续执行...")
    
    # 2. 创建目录（如果目录已存在也不报错）
    with suppress(FileExistsError):
        os.makedirs('my_directory')
        print("目录已创建")
    
    # 3. 抑制多个异常类型
    with suppress(FileNotFoundError, PermissionError):
        os.remove('protected_file.txt')
        print("文件删除尝试完成")
    
    print("所有操作完成\n")

# 运行基础示例
basic_suppress_examples()