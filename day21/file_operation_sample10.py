class RobustFileManager:
    def __init__(self, filename, mode): # 这里mode表示文件打开模式，有哪些模式可以参考Python的open函数
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            return self.file
        except FileNotFoundError:
            print(f"文件 {self.filename} 不存在")
            # 可以返回一个默认值或重新抛出异常
            raise
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        
        # 处理特定异常
        if exc_type is IOError:
            print("发生了IO错误")
            return True  # 抑制异常
        
        return False  # 不抑制其他异常

# 使用
try:
    with RobustFileManager('nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("文件未找到，已处理")