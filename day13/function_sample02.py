def fac(num):
    """求阶乘"""
    result = 1
    print(f"计算 {num}! 的过程：")
    for i in range(1, num + 1):
        old_result = result  # 保存之前的结果
        result *= i
        print(f"i = {i}: result = {old_result} * {i} = {result}")
    print(f"{num}! = {result}\n")
    return result

m = int(input('m = '))  # m = 4
n = int(input('n = '))  # n = 3

print(f"计算 C({m}, {n}) = {m}! // {n}! // ({m}-{n})!")
print("=" * 50)

# 计算组合数
fac_m = fac(m)
fac_n = fac(n)
fac_m_n = fac(m - n)

combination = fac_m // fac_n // fac_m_n
print("=" * 50)
print(f"最终结果：C({m}, {n}) = {fac_m} // {fac_n} // {fac_m_n} = {combination}")