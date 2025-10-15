def sum_of_numbers_with_step(start, end, step):
    total = 0
    for i in range(start, end, step):
        total += i
        print(i, end=' ')
    return total
print("1到100的数字之和为:", sum_of_numbers_with_step(1, 100, 1))
print("1到100的偶数之和为:", sum_of_numbers_with_step(2, 100, 2))
print("1到100的奇数之和为:", sum_of_numbers_with_step(1, 100, 2))