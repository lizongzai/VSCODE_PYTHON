import time
from functools import wraps

def timer(func):
    """计算函数执行时间的装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"函数 {func.__name__} 执行耗时: {execution_time:.4f} 秒")
        return result
    return wrapper

# 使用装饰器
@timer
def download(file_path):
    """模拟下载文件"""
    print(f"开始下载文件: {file_path}")
    time.sleep(2)  # 模拟下载耗时
    print("下载完成")
    return f"下载文件: {file_path}"

@timer
def upload(file_path):
    """模拟上传文件"""
    print(f"开始上传文件: {file_path}")
    time.sleep(1.5)  # 模拟上传耗时
    print("上传完成")
    return f"上传文件: {file_path}"

# 测试
if __name__ == "__main__":
    download("example.txt")
    upload("example.txt")