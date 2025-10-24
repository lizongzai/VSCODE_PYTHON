class CustomError(Exception):
    """自定义异常类"""
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

# 使用示例
def validate_age(age):
    """验证年龄"""
    if not isinstance(age, int):
        raise CustomError("年龄必须是整数", "INVALID_TYPE", {"input": age, "expected": "int"})
    if age < 0:
        raise CustomError("年龄不能为负数", "NEGATIVE_AGE", {"input": age})
    if age > 150:
        raise CustomError("年龄超出合理范围", "AGE_TOO_HIGH", {"input": age, "max_allowed": 150})
    return age

def process_user_data(user_data):
    """处理用户数据"""
    try:
        name = user_data.get('name', '未知')
        age = user_data.get('age')
        
        print(f"处理用户: {name}")
        validated_age = validate_age(age)
        print(f"年龄验证通过: {validated_age}")
        
    except CustomError as e:
        print(f"捕获自定义错误: {e}")
        print(f"错误详情: {e.get_details()}")
        # 可以根据错误代码进行不同的处理
        if e.error_code == "INVALID_TYPE":
            print("请检查输入数据类型")
        elif e.error_code == "NEGATIVE_AGE":
            print("年龄应该大于等于0")
        elif e.error_code == "AGE_TOO_HIGH":
            print("请输入合理的年龄")
    except Exception as e:
        print(f"捕获其他错误: {e}")

# 测试不同的场景
test_cases = [
    {'name': '张三', 'age': 25},      # 正常情况
    {'name': '李四', 'age': -5},      # 负数年龄
    {'name': '王五', 'age': 200},     # 年龄过大
    {'name': '赵六', 'age': "二十"},  # 错误类型
    {'name': '张飞', 'age': 25.1},      # 浮点数类型
    {'name': '钱七'},                 # 缺少年龄
]

print("=== 开始测试自定义异常 ===")
for i, user_data in enumerate(test_cases, 1):
    print(f"\n--- 测试案例 {i} ---")
    try:
        process_user_data(user_data)
    except Exception as e:
        print(f"处理过程中发生错误: {e}")

# 直接使用自定义异常
print("\n=== 直接使用自定义异常 ===")
try:
    raise CustomError("这是一个自定义错误", "CUSTOM_001", {"timestamp": "2024-01-01", "module": "test"})
except CustomError as e:
    print(f"错误信息: {e}")
    print(f"错误代码: {e.error_code}")
    print(f"错误详情: {e.get_details()}")

# 继承自定义异常创建更具体的异常
class DatabaseError(CustomError):
    """数据库相关异常"""
    def __init__(self, message, query=None, db_type="MySQL"):
        super().__init__(message, "DB_ERROR", {"query": query, "database": db_type})

class NetworkError(CustomError):
    """网络相关异常"""
    def __init__(self, message, url=None, status_code=None):
        super().__init__(message, "NETWORK_ERROR", {"url": url, "status_code": status_code})

print("\n=== 使用继承的自定义异常 ===")
try:
    raise DatabaseError("数据库连接失败", "SELECT * FROM users", "PostgreSQL")
except DatabaseError as e:
    print(f"数据库错误: {e}")
    print(f"详情: {e.get_details()}")

try:
    raise NetworkError("请求超时", "https://api.example.com", 408)
except NetworkError as e:
    print(f"网络错误: {e}")
    print(f"详情: {e.get_details()}")