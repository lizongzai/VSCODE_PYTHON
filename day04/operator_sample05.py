"""
比较运算符和逻辑运算符的使用

Version: 1.0
Author: 骆昊
"""
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag0
print("--------比较运算符和逻辑运算符的使用---------")
print('flag0 =', flag0)     # flag0 = True
print('flag1 =', flag1)     # flag1 = True
print('flag2 =', flag2)     # flag2 = False
print('flag3 =', flag3)     # flag3 = False
print('flag4 =', flag4)     # flag4 = True
print('flag5 =', flag5)     # flag5 = False
print(flag1 and not flag2)  # True
print(1 > 2 or 2 == 3)      # False
print(3.14 > 3 and 1 < 2)  # True
print(1 in [1, 2, 3])      # True
print(4 not in [1, 2, 3])  # True
print('a' in 'abc')        # True
print('d' not in 'abc')    # True
print(2 + 3 * 4 > 20 or 2 ** 3 < 5 and 4 % 2 == 0)  # False
print((2 + 3) * 4 > 20 or 2 ** 3 < 5 and 4 % 2 == 0)  # True
print(2 + 3 * 4 > 20 or (2 ** 3 < 5 and 4 % 2 == 0))  # True
print("--------比较运算符和逻辑运算符的使用---------\n")
