"""
Version: 1.0
Author: 李小婕
Date: 2025-10-19
Decription: 可重用的计时器装饰器

Keyword arguments:
argument -- description
Return: return_description
"""

import time
from functools import wraps
from datetime import datetime

def advanced_timer(print_result=True, save_to_file=False):
    """高级计时装饰器，支持更多功能"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 开始计时
            start_time = time.time()
            start_datetime = datetime.now()
            
            # 执行原函数
            result = func(*args, **kwargs)
            
            # 结束计时
            end_time = time.time()
            execution_time = end_time - start_time
            
            # 输出结果
            time_info = f"""
╔══════════════════════════════════════╗
║            函数执行时间统计           ║
╠══════════════════════════════════════╣
║ 函数名称: {func.__name__:<25} ║
║ 开始时间: {start_datetime.strftime('%Y-%m-%d %H:%M:%S')} ║
║ 执行耗时: {execution_time:.6f} 秒        ║
║ 执行结果: {result if print_result else '***'} ║
╚══════════════════════════════════════╝
            """
            print(time_info)
            
            # 可选：保存到文件
            if save_to_file:
                with open('function_timing.log', 'a', encoding='utf-8') as f:
                    f.write(time_info + '\n')
            
            return result
        return wrapper
    return decorator

# 使用高级装饰器
@advanced_timer(print_result=True, save_to_file=False)
def download(file_path):
    print(f"开始下载文件: {file_path}")
    time.sleep(2)
    print("下载完成")
    return f"下载文件: {file_path}成功"

@advanced_timer(print_result=False)
def upload(file_path):
    print(f"开始上传文件: {file_path}")
    time.sleep(1.5)
    print("上传完成")
    return f"上传文件: {file_path}成功"

# 测试
if __name__ == "__main__":
    download("example.txt")
    upload("example.txt")