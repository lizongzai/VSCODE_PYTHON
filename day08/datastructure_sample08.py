import sys
import timeit

a = list(range(100000))
b = tuple(range(100000))

print(sys.getsizeof(a), sys.getsizeof(b))

print(timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]'))
print(timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)'))


# 比较创建时间
list_time = timeit.timeit('list(range(10000))', number=1000)
tuple_time = timeit.timeit('tuple(range(10000))', number=1000)
print(f"列表创建时间: {list_time}")
print(f"元组创建时间: {tuple_time}")