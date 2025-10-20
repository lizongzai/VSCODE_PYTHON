class DigitalClock:
    """数字时钟类"""
    
    def __init__(self, hour=0, minute=0, second=0):
        """
        初始化时钟
        :param hour: 小时 (0-23)
        :param minute: 分钟 (0-59)
        :param second: 秒 (0-59)
        """
        self._hour = hour
        self._minute = minute
        self._second = second
        self._validate_time()
    
    def _validate_time(self):
        """验证时间是否合法"""
        if not (0 <= self._hour <= 23 and 0 <= self._minute <= 59 and 0 <= self._second <= 59):
            raise ValueError("时间参数不合法")
    
    def run(self):
        """时钟走字 - 秒数增加1"""
        self._second += 1
        
        # 处理进位
        if self._second == 60:
            self._second = 0
            self._minute += 1
            
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                
                if self._hour == 24:
                    self._hour = 0
    
    def display(self):
        """显示当前时间"""
        return f"{self._format_number(self._hour)}:{self._format_number(self._minute)}:{self._format_number(self._second)}"
    
    def _format_number(self, num):
        """格式化数字，确保两位数显示"""
        return str(num).zfill(2) # 在字符串左侧填充零，确保总长度为2
    
    def set_time(self, hour, minute, second):
        """设置时间"""
        self._hour = hour
        self._minute = minute
        self._second = second
        self._validate_time()
    
    def get_time(self):
        """获取时间元组"""
        return (self._hour, self._minute, self._second)

# 使用示例
if __name__ == "__main__":
    # 创建一个时钟，初始时间为 23:59:58
    clock = DigitalClock(23, 59, 58)
    
    print("初始时间:", clock.display())
    
    # 模拟时钟走字
    for i in range(10):
        clock.run()
        print(f"第{i+1}秒后: {clock.display()}")
    
    print("\n" + "="*30)
    
    # 测试设置时间功能
    clock2 = DigitalClock()
    clock2.set_time(12, 30, 45)
    print("新时钟时间:", clock2.display())
    
    # # 获取时间元组
    print("时间元组:", clock2.get_time())