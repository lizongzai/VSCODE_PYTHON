import math
import time

def is_prime(n):
    """
    判断给定的大于1的正整数是否为素数
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    max_divisor = math.isqrt(n)
    i = 5
    while i <= max_divisor:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def check_primes_in_range(start, end):
    """检查指定范围内的所有素数"""
    primes = []
    for num in range(max(2, start), end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def test_performance():
    """测试性能"""
    test_numbers = [2, 3, 17, 100, 101, 1009, 7919, 10007, 999983]
    
    print("性能测试:")
    start_time = time.time()
    
    for num in test_numbers:
        result = is_prime(num)
        status = "素数" if result else "合数"
        print(f"  {num}: {status}")
    
    end_time = time.time()
    print(f"总耗时: {end_time - start_time:.6f}秒")

# 使用示例
if __name__ == "__main__":
    # 测试单个数字
    numbers_to_test = [1, 2, 3, 4, 16, 17, 25, 97, 100, 101]
    
    print("=== 素数判断 ===")
    for num in numbers_to_test:
        result = is_prime(num)
        status = "素数" if result else "合数"
        print(f"{num} -> {status}")
    
    # 检查范围内的素数
    print("\n=== 1-100的素数 ===")
    primes = check_primes_in_range(1, 100)
    print(f"共找到 {len(primes)} 个素数:")
    print(primes)
    
    # 性能测试
    print("\n=== 性能测试 ===")
    test_performance()