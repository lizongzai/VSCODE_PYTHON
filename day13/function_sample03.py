import math

def calculate_combination(m, n):
    """使用math.factorial计算组合数"""
    print(f"计算 C({m}, {n}) = {m}! / ({n}! × ({m}-{n})!)")
    print("=" * 40)
    
    # 直接使用math.factorial
    fac_m = math.factorial(m)
    fac_n = math.factorial(n)
    fac_m_n = math.factorial(m - n)
    
    print(f"{m}! = {fac_m}")
    print(f"{n}! = {fac_n}")
    print(f"({m}-{n})! = {fac_m_n}")
    
    combination = fac_m // (fac_n * fac_m_n)
    print(f"C({m}, {n}) = {fac_m} // ({fac_n} × {fac_m_n}) = {combination}")
    return combination

# 使用示例
m = int(input('m = '))
n = int(input('n = '))
result = calculate_combination(m, n)