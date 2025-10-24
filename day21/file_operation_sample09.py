class CustomError(Exception):
    """基础自定义异常类"""
    def __init__(self, message, error_code=None, details=None):
        self.message = message
        self.error_code = error_code
        self.details = details
        super().__init__(self.message)
    
    def __str__(self):
        """自定义异常显示格式"""
        if self.error_code:
            return f"[Error {self.error_code}] {self.message}"
        return self.message
    
    def get_details(self):
        """获取错误详情"""
        return self.details or "无额外详情"

# 继承自定义异常创建更具体的异常
class DatabaseError(CustomError):
    """数据库相关异常"""
    def __init__(self, message, query=None, db_type="MySQL"):
        super().__init__(message, "DB_ERROR", {"query": query, "database": db_type})

class NetworkError(CustomError):
    """网络相关异常"""
    def __init__(self, message, url=None, status_code=None):
        super().__init__(message, "NETWORK_ERROR", {"url": url, "status_code": status_code})

class FileSystemError(CustomError):
    """文件系统相关异常"""
    def __init__(self, message, file_path=None, operation=None):
        super().__init__(message, "FILE_ERROR", {"file_path": file_path, "operation": operation})

# 使用继承异常的专业函数
def connect_to_database(connection_string): # connection_string 来自数据库连接字符串
    """模拟数据库连接"""
    if "mysql" not in connection_string:
        raise DatabaseError("不支持的数据库类型", f"CONNECT TO {connection_string}", "MySQL")
    print(f"成功连接到数据库: {connection_string}")

def make_http_request(url):
    """模拟HTTP请求"""
    if "timeout" in url:
        raise NetworkError("请求超时", url, 408)
    elif "404" in url:
        raise NetworkError("页面未找到", url, 404)
    print(f"成功请求: {url}")

def read_file(file_path):
    """模拟文件读取"""
    if not file_path.endswith('.txt'):
        raise FileSystemError("不支持的文件格式", file_path, "read")
    print(f"成功读取文件: {file_path}")

print("=== 第二部分：使用继承的自定义异常 ===")

print("\n--- 测试数据库异常 ---")
try:
    connect_to_database("postgresql://localhost:5432")
except DatabaseError as e:
    print(f"数据库错误: {e}")
    print(f"详情: {e.get_details()}")

print("\n--- 测试网络异常 ---")
try:
    make_http_request("https://api.example.com/timeout")
except NetworkError as e:
    print(f"网络错误: {e}")
    print(f"状态码: {e.details.get('status_code')}")
    print(f"请求URL: {e.details.get('url')}")

print("\n--- 测试文件系统异常 ---")
try:
    read_file("data.pdf")
except FileSystemError as e:
    print(f"文件系统错误: {e}")
    print(f"操作类型: {e.details.get('operation')}")
    print(f"文件路径: {e.details.get('file_path')}")

print("\n--- 成功案例 ---")
try:
    connect_to_database("mysql://localhost:3306")
    make_http_request("https://api.example.com/data")
    read_file("data.txt")
    print("所有操作成功完成！")
except (DatabaseError, NetworkError, FileSystemError) as e:
    print(f"操作失败: {e}")