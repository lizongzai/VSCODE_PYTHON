import math

class Point:
    """描述平面上的点"""
    
    def __init__(self, x=0, y=0):
        """
        初始化点
        :param x: x坐标
        :param y: y坐标
        """
        self.x = x
        self.y = y
    
    def distance_to(self, other_point):
        """
        计算到另一个点的距离
        :param other_point: 另一个Point对象
        :return: 两点之间的距离
        """
        if not isinstance(other_point, Point):
            raise TypeError("参数必须是Point对象")
        
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx**2 + dy**2)
    
    def distance_from_origin(self):
        """计算到原点(0,0)的距离"""
        return math.sqrt(self.x**2 + self.y**2)
    
    def __str__(self):
        """返回点的字符串表示"""
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        """返回点的正式字符串表示"""
        return f"Point({self.x}, {self.y})"
    
    def move(self, dx, dy):
        """
        移动点
        :param dx: x方向移动距离
        :param dy: y方向移动距离
        """
        self.x += dx
        self.y += dy
        return self  # 支持链式调用
    
    def copy(self):
        """创建点的副本"""
        return Point(self.x, self.y)
    
    @classmethod
    def from_tuple(cls, coord_tuple):
        """
        从元组创建点
        :param coord_tuple: (x, y)元组
        """
        return cls(coord_tuple[0], coord_tuple[1])

# 使用示例
if __name__ == "__main__":
    # 创建点对象
    point1 = Point(3, 4)
    point2 = Point(0, 0)
    point3 = Point(6, 8)
    
    print(f"点1: {point1}")
    print(f"点2: {point2}")
    print(f"点3: {point3}")
    
    print("\n" + "="*40)
    
    # 计算点之间的距离
    distance1 = point1.distance_to(point2)
    distance2 = point1.distance_to(point3)
    
    print(f"点1到点2的距离: {distance1:.2f}")
    print(f"点1到点3的距离: {distance2:.2f}")
    
    # 计算到原点的距离
    origin_distance = point1.distance_from_origin()
    print(f"点1到原点的距离: {origin_distance:.2f}")
    
    print("\n" + "="*40)
    
    # 测试移动功能
    print("移动点2:")
    point2.move(1, 1)
    print(f"移动后的点2: {point2}")
    
    # 测试复制功能
    point4 = point1.copy()
    print(f"点1的副本: {point4}")
    
    # 测试从元组创建
    point5 = Point.from_tuple((10, 20))
    print(f"从元组创建的点: {point5}")
    
    print("\n" + "="*40)
    
    # 验证点1、点3和原点是否构成直角三角形
    d1 = point1.distance_from_origin()  # 点1到原点
    d2 = point3.distance_from_origin()  # 点3到原点  
    d3 = point1.distance_to(point3)     # 点1到点3
    
    print(f"验证直角三角形:")
    print(f"边1: {d1:.2f}, 边2: {d2:.2f}, 边3: {d3:.2f}")
    print(f"是否满足勾股定理: {abs(d1**2 + d2**2 - d3**2) < 0.0001}")