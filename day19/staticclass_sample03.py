from abc import ABC, abstractmethod
import math

class Triangle(ABC):
    """三角形基类"""
    
    def __init__(self, sides):
        self.sides = sides
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    @classmethod
    def create_triangle(cls, a, b, c):
        """工厂方法：根据边长自动创建合适的三角形子类"""
        # 1. 基础验证
        if not cls._is_valid_triangle(a, b, c):
            raise ValueError(f"边长({a}, {b}, {c})无法构成三角形")
        
        # 2. 判断类型并创建相应的子类对象
        if a == b == c:
            return EquilateralTriangle(a, b, c)
        elif a == b or a == c or b == c:
            return IsoscelesTriangle(a, b, c)
        elif cls._is_right_triangle(a, b, c):
            return RightTriangle(a, b, c)
        else:
            return ScaleneTriangle(a, b, c)
    
    @staticmethod
    def _is_valid_triangle(a, b, c):
        return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)
    
    @staticmethod
    def _is_right_triangle(a, b, c):
        sides = sorted([a, b, c])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2, rel_tol=1e-9)

class EquilateralTriangle(Triangle):
    """等边三角形"""
    def __init__(self, a, b, c):
        super().__init__([a, b, c])
        self.side = a
    
    def area(self):
        return (math.sqrt(3) / 4) * self.side ** 2
    
    def perimeter(self):
        return 3 * self.side
    
    def __str__(self):
        return f"等边三角形(边长: {self.side})"

class IsoscelesTriangle(Triangle):
    """等腰三角形"""
    def __init__(self, a, b, c):
        super().__init__([a, b, c])
        # 找出相等的两条边和底边
        if a == b:
            self.equal_sides = a
            self.base = c
        elif a == c:
            self.equal_sides = a
            self.base = b
        else:
            self.equal_sides = b
            self.base = a
    
    def area(self):
        # 等腰三角形面积公式
        height = math.sqrt(self.equal_sides**2 - (self.base/2)**2)
        return (self.base * height) / 2
    
    def perimeter(self):
        return 2 * self.equal_sides + self.base
    
    def __str__(self):
        return f"等腰三角形(腰: {self.equal_sides}, 底: {self.base})"

class RightTriangle(Triangle):
    """直角三角形"""
    def __init__(self, a, b, c):
        super().__init__([a, b, c])
        sides = sorted([a, b, c])
        self.legs = sides[:2]  # 两条直角边
        self.hypotenuse = sides[2]  # 斜边
    
    def area(self):
        return (self.legs[0] * self.legs[1]) / 2
    
    def perimeter(self):
        return sum(self.sides)
    
    def __str__(self):
        return f"直角三角形(直角边: {self.legs[0]}, {self.legs[1]}, 斜边: {self.hypotenuse})"

class ScaleneTriangle(Triangle):
    """一般三角形"""
    def __init__(self, a, b, c):
        super().__init__([a, b, c])
    
    def area(self):
        # 使用海伦公式
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))
    
    def perimeter(self):
        return sum(self.sides)
    
    def __str__(self):
        return f"一般三角形(边长: {self.sides[0]}, {self.sides[1]}, {self.sides[2]})"


if __name__ == "__main__":
    
    # 使用示例
    print("=== 工厂模式 + 多态的真正价值 ===")
    # 创建不同类型的三角形，但使用统一的接口
    triangles_data = [
        (3, 4, 5),     # 直角三角形
        (5, 5, 5),     # 等边三角形
        (5, 5, 6),     # 等腰三角形
        (2, 3, 4),     # 一般三角形
        (6, 8, 10),    # 直角三角形
        (7, 7, 10),    # 等腰三角形
    ]

    triangles = []
    for sides in triangles_data:
        try:
            triangle = Triangle.create_triangle(*sides)  # 工厂方法创建具体类型的三角形
            triangles.append(triangle)
            print(f"创建成功: {triangle}")
        except ValueError as e:
            print(f"创建失败: {e}")

    print("\n=== 多态的优势 ===")
    # 统一处理不同类型的三角形
    for triangle in triangles:
        print(f"{triangle}: 周长={triangle.perimeter()}, 面积={triangle.area():.2f}")

    print("\n=== 类型统计 ===")
    from collections import Counter
    types_count = Counter(type(t).__name__ for t in triangles)
    for type_name, count in types_count.items():
        print(f"{type_name}: {count}个")