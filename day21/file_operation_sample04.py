class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """进入上下文时调用，返回要管理的资源"""
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        """退出上下文时调用，处理异常和清理资源"""
        if self.file: # 确保文件已打开
            self.file.close()
        
        # 如果返回 True，异常会被抑制；返回 False 或 None，异常会继续传播
        return False

# 使用自定义上下文管理器
with FileManager('example.txt', 'a') as f:
    f.write('Hello, World!')