import time
from functools import wraps

def timer(unit='seconds'):
    """带参数的装饰器，可以选择时间单位"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            
            # 根据单位转换时间
            if unit == 'milliseconds':
                execution_time *= 1000
                time_unit = "毫秒"
            elif unit == 'minutes':
                execution_time /= 60
                time_unit = "分钟"
            else:
                time_unit = "秒"
            
            print(f"函数 {func.__name__} 执行耗时: {execution_time:.4f} {time_unit}")
            return result
        return wrapper
    return decorator

# 使用带参数的装饰器
@timer(unit='milliseconds')
def download(file_path):
    print(f"开始下载文件: {file_path}")
    time.sleep(2)
    print("下载完成")
    return f"下载文件: {file_path}"

@timer(unit='seconds')
def upload(file_path):
    print(f"开始上传文件: {file_path}")
    time.sleep(1.5)
    print("上传完成")
    return f"上传文件: {file_path}"