import math
import time

# 基础版本
def is_prime_basic(n):
    """判断一个大于1的正整数是否为素数（基础版本）"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # 检查从3到n-1的所有奇数
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

# 优化版本1
def is_prime_optimized(n):
    """判断素数（优化版本）- 检查到√n即可"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # 只需要检查到√n
    max_divisor = math.isqrt(n)
    
    for i in range(3, max_divisor + 1, 2):  # 只检查奇数
        if n % i == 0:
            return False
    return True

# 最终版本
def is_prime(n):
    """
    判断给定的大于1的正整数是否为素数（最终版本）
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # 使用6k±1规则进行优化检查
    max_divisor = math.isqrt(n)
    
    i = 5
    while i <= max_divisor:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

# 性能测试函数
def test_performance():
    """测试不同实现的性能"""
    test_numbers = [2, 3, 17, 100, 101, 1009, 7919, 10007, 999983]
    
    functions = [
        ("基础版本", is_prime_basic),
        ("优化版本", is_prime_optimized), 
        ("最终版本", is_prime)  # 这里使用已经定义的 is_prime 函数
    ]
    
    for name, func in functions:
        print(f"\n{name}性能测试:")
        start_time = time.time()
        
        results = []
        for num in test_numbers:
            result = func(num)
            results.append((num, result))
        
        end_time = time.time()
        
        for num, is_prime_result in results:
            status = "素数" if is_prime_result else "合数"
            print(f"  {num}: {status}")
        
        print(f"  总耗时: {end_time - start_time:.6f}秒")

# 范围检查函数
def check_primes_in_range(start, end):
    """检查指定范围内的所有素数"""
    primes = []
    for num in range(max(2, start), end + 1):
        if is_prime(num):  # 使用最终版本的 is_prime 函数
            primes.append(num)
    return primes

# 主程序
if __name__ == "__main__":
    # 单个数字测试
    test_numbers = [1, 2, 3, 4, 17, 25, 97, 100, 101, 1009]
    
    print("=== 素数判断测试 ===")
    for num in test_numbers:
        result = is_prime(num)
        status = "素数" if result else "合数"
        print(f"{num:4d} -> {status}")
    
    # 范围检查
    print("\n=== 查找1-50的素数 ===")
    primes_50 = check_primes_in_range(1, 50)
    print(f"1-50之间的素数: {primes_50}")
    
    # 性能测试
    print("\n=== 性能测试 ===")
    test_performance()