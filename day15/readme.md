

#### 2.5.3 函数使用进阶

我们继续探索定义和使用函数的相关知识。通过前面的学习，我们知道了函数有自变量（参数）和因变量（返回值），自变量可以是任意的数据类型，因变量也可以是任意的数据类型，那么这里就有一个小问题，我们能不能用函数作为函数的参数，用函数作为函数的返回值？这里我们先说结论：**Python 中的函数是“一等函数”**，所谓“一等函数”指的就是函数可以赋值给变量，函数可以作为函数的参数，函数也可以作为函数的返回值。把一个函数作为其他函数的参数或返回值的用法，我们通常称之为“高阶函数”。

##### 2.5.3.1 高阶函数

“高阶函数”（Higher-Order Function）是函数式编程中一个非常核心的概念，它指的是**满足以下至少一个条件的函数**：

1. **接收一个或多个函数作为参数**
2. **返回一个函数作为结果**



~~~python
def calc(*args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = 0
    for item in items:
        if type(item) in (int, float):
            result += item
    return result
~~~





**例子：**

```python
def apply_twice(func, x):
    return func(func(x))

def add_three(n):
    return n + 3

result = apply_twice(add_three, 7)
print(result)  # 输出 13，因为 (7+3)+3=13
```



**逐步执行过程**

*第1步：函数调用*

```python
result = apply_twice(add_three, 7)
```



*第2步：进入 apply_twice 函数*

python

```python
def apply_twice(func, x):  # func = add_three, x = 7
    return func(func(x))   # 先计算 func(x)，再用 func() 处理结果
```



*第3步：第一次调用 func(x)*

```python
func(x) = add_three(7)    # 调用 add_three(7)
def add_three(n):         # n = 7
    return n + 3          # 返回 7 + 3 = 10
```

> ```
> # 第一步：执行最内层的 func(x)
> inner_result = func(x)        # add_three(7) = 10
> 
> # 第二步：用第一步的结果执行外层的 func()
> final_result = func(inner_result)  # add_three(10) = 13
> 
> # 第三步：返回最终结果
> return final_result  # 返回 13
> 
> ```
>
> 



*第4步：第二次调用 func()*

```python
func(10) = add_three(10)  # 用第一次的结果再次调用 add_three
def add_three(n):         # n = 10  
    return n + 3          # 返回 10 + 3 = 13
```



*第5步：返回最终结果*

```python
return 13  # apply_twice 返回 13
```



*可视化执行流程*

```
apply_twice(add_three, 7)
    ↓
add_three(add_three(7))
    ↓
add_three(7 + 3) = add_three(10)
    ↓  
10 + 3 = 13
```





































