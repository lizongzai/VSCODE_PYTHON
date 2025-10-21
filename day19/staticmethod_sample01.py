import math

class Triangle:
    """
    三角形类
    """
    
    def __init__(self, side_a, side_b, side_c):
        """
        初始化三角形
        在构造对象前，应该先使用is_valid_triangle方法验证边长是否有效
        """
        if not Triangle.is_valid_triangle(side_a, side_b, side_c):
            raise ValueError(f"边长({side_a}, {side_b}, {side_c})无法构成三角形")
        
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    @staticmethod
    def is_valid_triangle(a, b, c):
        """
        静态方法：验证三条边长是否能构成三角形
        三角形条件：任意两边之和大于第三边，且所有边长为正数
        """
        # 检查边长是否为正数
        if a <= 0 or b <= 0 or c <= 0:
            return False
        
        # 检查三角形不等式
        if a + b <= c:
            return False
        if a + c <= b:
            return False
        if b + c <= a:
            return False
        
        return True
    
    def perimeter(self):
        """实例方法：计算三角形的周长"""
        return self.side_a + self.side_b + self.side_c
    
    def area(self):
        """实例方法：计算三角形的面积（使用海伦公式）"""
        p = self.perimeter() / 2  # 半周长
        area = math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))
        return area
    
    def __str__(self):
        return f"三角形(边长: {self.side_a}, {self.side_b}, {self.side_c})"


# 使用示例
if __name__ == "__main__":
    # 使用静态方法验证边长，不需要创建对象
    print("验证边长是否能构成三角形:")
    print(f"边长(3, 4, 5)是否有效: {Triangle.is_valid_triangle(3, 4, 5)}")  # True
    print(f"边长(1, 1, 3)是否有效: {Triangle.is_valid_triangle(1, 1, 3)}")  # False
    print(f"边长(0, 2, 2)是否有效: {Triangle.is_valid_triangle(0, 2, 2)}")  # False
    print()
    
    # 创建有效的三角形对象
    try:
        triangle1 = Triangle(3, 4, 5)
        print(f"创建成功: {triangle1}")
        print(f"周长: {triangle1.perimeter()}")
        print(f"面积: {triangle1.area()}")
        print()
    except ValueError as e:
        print(f"创建失败: {e}")
    
    # 尝试创建无效的三角形对象
    try:
        triangle2 = Triangle(1, 1, 3)
        print(f"创建成功: {triangle2}")
    except ValueError as e:
        print(f"创建失败: {e}")
    
    # 另一个有效的三角形
    try:
        triangle3 = Triangle(5, 5, 5)  # 等边三角形
        print(f"创建成功: {triangle3}")
        print(f"周长: {triangle3.perimeter()}")
        print(f"面积: {triangle3.area():.2f}")
    except ValueError as e:
        print(f"创建失败: {e}")