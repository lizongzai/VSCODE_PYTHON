"""
Version: 1.0
Author: 李小婕
Description: 输入两个正整数求它们的最大公约数,最小公倍数，并输出从1到100的所有素数。
Date: 2025-10-13

Keyword arguments:
argument -- description
Return: return_description
"""
def gcd(a, b): # 欧几里得算法
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b): # 最小公倍数
    return a * b // gcd(a, b)
print("最大公约数:", gcd(48, 18))
print("最小公倍数:", lcm(48, 18))

print("1到100的素数有:")
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
print()
