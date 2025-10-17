# Lambda函数

在使用高阶函数的时候，如果作为参数或者返回值的函数本身非常简单，一行代码就能够完成，也不需要考虑对函数的复用，那么我们可以使用 lambda 函数。Python 中的 lambda 函数是没有的名字函数，所以很多人也把它叫做**匿名函数**，lambda 函数只能有一行代码，代码中的表达式产生的运算结果就是这个匿名函数的返回值。之前的代码中，我们写的`is_even`和`square`函数都只有一行代码，我们可以考虑用 lambda 函数来替换掉它们，代码如下所示。

```python
old_nums = [35, 12, 8, 99, 60, 52]
new_nums = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, old_nums)))
print(new_nums)  # [144, 64, 3600, 2704]
```



通过上面的代码可以看出，定义 lambda 函数的关键字是`lambda`，后面跟函数的参数，如果有多个参数用逗号进行分隔；冒号后面的部分就是函数的执行体，通常是一个表达式，表达式的运算结果就是 lambda 函数的返回值，不需要写`return` 关键字。

前面我们说过，Python 中的函数是“一等函数”，函数是可以直接赋值给变量的。在学习了 lambda 函数之后，前面我们写过的一些函数就可以用一行代码来实现它们了，大家可以看看能否理解下面的求阶乘和判断素数的函数。





~~~python
import functools
import operator

# 用一行代码实现计算阶乘的函数
fac = lambda n: functools.reduce(operator.mul, range(2, n + 1), 1)

# 用一行代码实现判断素数的函数
is_prime = lambda x: all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))

# 调用Lambda函数
print(fac(6))        # 720
print(is_prime(37))  # True
~~~

> **提示1**：上面使用的`reduce`函数是 Python 标准库`functools`模块中的函数，它可以实现对一组数据的归约操作，类似于我们之前定义的`calc`函数，第一个参数是代表运算的函数，第二个参数是运算的数据，第三个参数是运算的初始值。很显然，`reduce`函数也是高阶函数，它和`filter`函数、`map`函数一起构成了处理数据中非常关键的三个动作：**过滤**、**映射**和**归约**。
>
> **提示2**：上面判断素数的 lambda 函数通过`range`函数构造了从 2 到 x 的范围，检查这个范围有没有`x`的因子。`all`函数也是 Python 内置函数，如果传入的序列中所有的布尔值都是`True`，`all`函数返回`True`，否则`all`函数返回`False`。







###### 1️⃣  常见使用场景

**场景1：作为函数参数（最常用）**

```python
# 在 sorted 中使用
numbers = [('a', 3), ('b', 1), ('c', 2)]
sorted_numbers = sorted(numbers, key=lambda x: x[1])
print(sorted_numbers)  # 输出: [('b', 1), ('c', 2), ('a', 3)]

# 在 map 中使用
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # 输出: [1, 4, 9, 16]

# 在 filter 中使用
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # 输出: [2, 4, 6]
```



**场景2：简单的条件判断**

```python
# 判断奇偶
check_odd = lambda x: "奇数" if x % 2 == 1 else "偶数"
print(check_odd(5))  # 输出: "奇数"
print(check_odd(4))  # 输出: "偶数"

# 绝对值
abs_value = lambda x: x if x >= 0 else -x
print(abs_value(-5))  # 输出: 5
```



**场景3：在字典排序中使用**

```python
students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78}
]

# 按分数排序
sorted_students = sorted(students, key=lambda x: x['score'])
for student in sorted_students:
    print(f"{student['name']}: {student['score']}")
```



**场景4：复杂数据结构**

~~~python
employees = [
    {'name': 'Alice', 'department': 'HR', 'salary': 50000},
    {'name': 'Bob', 'department': 'IT', 'salary': 70000},
    {'name': 'Charlie', 'department': 'HR', 'salary': 55000}
]

# 按部门排序
sorted_dept = sorted(employees, key=lambda employee: employee['department'])

# 按薪资排序（降序）
sorted_salary = sorted(employees, key=lambda employee: employee['salary'], reverse=True)
~~~



**命名建议**

~~~python
# ✅ 清晰易懂
sorted_students = sorted(students, key=lambda student: student['score'])
sorted_products = sorted(products, key=lambda product: product['price'])
sorted_users = sorted(users, key=lambda user: user['age'])
~~~





**Lambda 参数名 `x`**

`x` 是 lambda 表达式的**参数名**，可以任意命名：

**使用有意义的名称：**

```python
# ✅ 使用 student 更清晰
sorted_students = sorted(students, key=lambda student: student['score'])

# ✅ 使用 s 作为缩写
sorted_students = sorted(students, key=lambda s: s['score'])

# ✅ 使用 item
sorted_students = sorted(students, key=lambda item: item['score'])

# ✅ 甚至用任意名字
sorted_students = sorted(students, key=lambda abc: abc['score'])
```



