"""
Version: 1.0
Author: 李小婕
Date: 2025-10-19
Decription: 类装饰器

Keyword arguments:
argument -- description
Return: return_description
"""

import time
from functools import wraps

class Timer:
    """计时器类装饰器"""
    
    def __init__(self, func):
        self.func = func
        wraps(func)(self)
    
    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        
        print(f"⏰ 函数 {self.func.__name__} 执行耗时: {execution_time:.4f} 秒")
        return result

# 使用类装饰器
@Timer
def download(file_path):
    print(f"开始下载文件: {file_path}")
    time.sleep(2)
    print("下载完成")
    return f"下载文件: {file_path}"

@Timer
def upload(file_path):
    print(f"开始上传文件: {file_path}")
    time.sleep(1.5)
    print("上传完成")
    return f"上传文件: {file_path}"


# 测试
if __name__ == "__main__":
    download("example.txt")
    upload("example.txt")