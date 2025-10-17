# 学习Python 程序设计













## 1. 安装Python解释器

### 1.1 Python Download

https://www.python.org/downloads/macos/

![image-20251012115109342](C:\Users\86181\AppData\Roaming\Typora\typora-user-images\image-20251012115109342.png)





### 1.2 Visual Studio Code







## 2. 基础部分



### 2.1 变量类型

#### 2.1.1 使用type函数检查变量的类型

`variable_sample01.py`

```python
"""
使用type函数检查变量的类型

Version: 1.0
Author: zongzai.li
"""
a = 100
b = 123.45
c = 'hello, world'
d = True

print(f"变量a的值: {a}, 类型: {type(a)}")  # <class 'int'>
print(f"变量b的值: {b}, 类型: {type(b)}")  # <class 'float'>
print(f"变量c的值: {c}, 类型: {type(c)}")  # <class 'str'>
print(f"变量d的值: {d}, 类型: {type(d)}")  # <class 'bool'>
```



#### 2.1.2 变量的类型转换操作

`variable_sample02.py`

```python
"""
Version: 1.0
Author: Lizongzai
Description: 变量的类型转换操作
"""

# 字符串转整数
num_str = "123"
num_int = int(num_str)
print(type(num_int))  # <class 'int'>

# 整数转字符串
num = 456
num_str = str(num)
print(type(num_str))  # <class 'str'>


# variable_sample02.py 的可能内容
x = 100
y = "hello"

print(type(x))
print(type(y))
```



`variable_sample03.py`

```python
"""
Version: 1.0
Author: Lizongzai
Description: 变量的类型转换操作
"""

a = 100
b = 123.45
c = '123'
d = '100'
e = '123.45'
f = 'hello, world'
g = True
print(float(a))         # int类型的100转成float，输出100.0
print(int(b))           # float类型的123.45转成int，输出123
print(int(c))           # str类型的'123'转成int，输出123
print(int(c, base=16))  # str类型的'123'按十六进制转成int，输出291
print(int(d, base=2))   # str类型的'100'按二进制转成int，输出4
print(float(e))         # str类型的'123.45'转成float，输出123.45
print(bool(f))          # str类型的'hello, world'转成bool，输出True
print(int(g))           # bool类型的True转成int，输出1
print(chr(a))           # int类型的100转成str，输出'd'
print(ord('d'))         # str类型的'd'转成int，输出100
```



`variable_sample04.py`

```python
"""
Version: 1.0
Author: Lizongzai
Description: 变量的类型转换操作
"""
a = 100
b = 123.45 
c = '123'
d = '100'
e = '123.45'
f = 'hello, world'
g = True

print(float(a))         # int类型的100转成float，输出100.0
print(int(b))           # float类型的123.45转成int，输出123
print(int(c))           # str类型的'123'转成int，输出123
print(int(c, base=16))  # str类型的'123'按十六进制转成int，输出291
print(int(d, base=2))   # str类型的'100'按二进制转成int，输出4
print(float(e))         # str类型的'123.45'转成float，输出
print(bool(f))          # str类型的'hello, world'转成bool，输出True
print(int(g))           # bool类型的True转成int，输出1
print(chr(a))           # int类型的100转成str，输出'd'
print(ord('d'))         # str类型的'd'转成int，输出100

print(type(ord('a')))  # <class 'int'> --- IGNORE ---
```



####  2.1.3 元组和列表

```python
"""
Version: 1.0
Author: Lizongzai
Description: 变量的类型检查和元组、列表的使用
"""


# 元组不可变，列表可变
tuple1 = (1, 2, 3)
print(type(tuple1))  # <class 'tuple'>
print(tuple1[0])  # 访问元组的第一个元素
print(tuple1[-1])  # 访问元组的最后一个元素
print(tuple1[1:3])  # 访问元组的第二个和第三个元素
print(len(tuple1))  # 元组的长度
# tuple1[0] = 10  # 这行会报错！元组不可修改

# 列表
list1 = [1, 2, 3]
list1[0] = 10  # 列表可以修改
print(list1)  # [10, 2, 3]
print(type(list1))  # <class 'list'>
print(list1[0])  # 访问列表的第一个元素
print(list1[-1])  # 访问列表的最后一个元素

# 元组的访问
fruits = ('apple', 'banana', 'cherry')
print(fruits[0])   # 'apple'
print(fruits[-1])  # 'cherry'
```





```python
"""
Version: 1.0
Author: Lizongzai
Description: 变量的类型检查和元组、列表的使用
"""


# 元组不可变，列表可变
tuple1 = (1, 2, 3)
print(type(tuple1))  # <class 'tuple'>
print(tuple1[0])  # 访问元组的第一个元素
print(tuple1[-1])  # 访问元组的最后一个元素
print(tuple1[1:3])  # 访问元组的第二个和第三个元素
print(len(tuple1))  # 元组的长度
# tuple1[0] = 10  # 这行会报错！元组不可修改

# 列表
list1 = [1, 2, 3]
list1[0] = 10  # 列表可以修改
print(list1)  # [10, 2, 3]
print(type(list1))  # <class 'list'>
print(list1[0])  # 访问列表的第一个元素
print(list1[-1])  # 访问列表的最后一个元素

# 元组的访问
fruits = ('apple', 'banana', 'cherry')
print(fruits[0])   # 'apple'
print(fruits[-1])  # 'cherry'
print(fruits[1:3]) # ('banana', 'cherry')
print(len(fruits))  # 3
print(type(fruits))  # <class 'tuple'>
print(isinstance(fruits, tuple))  # True
print(isinstance(fruits, list))   # False
print(isinstance(fruits, (list, tuple)))  # True
print(isinstance(fruits, (list, dict)))   # False
print(tuple1 + fruits)  # (1, 2, 3, 'apple', 'banana', 'cherry')
print(fruits * 2)      # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
print(2 in tuple1)     # True
print('banana' in fruits)  # True
print('orange' in fruits)  # False
print(tuple1.index(2))  # 1
print(fruits.count('apple'))  # 1
print(fruits.count('orange'))  # 0

```



#### 2.1.4 元组 vs 列表

| 特性     | 元组             | 列表               |
| :------- | :--------------- | :----------------- |
| 语法     | `()`             | `[]`               |
| 可变性   | ❌ 不可变         | ✅ 可变             |
| 性能     | 更快             | 稍慢               |
| 内存占用 | 更小             | 更大               |
| 用途     | 保护数据不被修改 | 需要动态修改的数据 |





### 2.2 算术符

#### 2.2.1 运算符优先级表（部分）

| 优先级 | 运算符              | 描述               | 结合性   |
| :----- | :------------------ | :----------------- | :------- |
| 1      | `**`                | 指数               | 从右向左 |
| 2      | `*`, `/`, `%`, `//` | 乘、除、取模、整除 | 从左向右 |
| 3      | `+`, `-`            | 加、减             | 从左向右 |



`operator_sample01.py`

~~~python
"""
算术运算符

Version: 1.0
Author: 骆昊
"""
print("--------算术运算符---------")
print(321 + 12)     # 加法运算，输出333
print(321 - 12)     # 减法运算，输出309
print(321 * 12)     # 乘法运算，输出3852
print(321 / 12)     # 除法运算，输出26.75
print(321 // 12)    # 整除运算，输出26
print(321 % 12)     # 求模运算，输出9
print(321 ** 12)    # 求幂运算，输出1196906950228928915420617322241
print(2 + 3 * 4)   # 运算符优先级，输出14
print((2 + 3) * 4) # 运算符优先级，输出20
print(2 ** 3 ** 2)   # 运算符优先级，输出512
print(2 ** (3 ** 2))   # 512 - 显式括号，结果相同
print((2 ** 3) ** 2)   # 64  - 如果从左向右计算的结果
print("--------算术运算符---------\n")


"""
算术运算的优先级

Version: 1.0
Author: 骆昊
"""
print("--------算术运算的优先级---------")
print(2 + 3 * 5)           # 17
print((2 + 3) * 5)         # 25
print((2 + 3) * 5 ** 2)    # 125
print(((2 + 3) * 5) ** 2)  # 625
print("--------算术运算的优先级---------\n")
~~~





#### 2.2.2 赋值运算符

赋值运算符应该是最为常见的运算符，它的作用是将右边的值赋给左边的变量。赋值运算符还可以跟上面的算术运算符放在一起，组合成复合赋值运算符，例如：`a += b`相当于`a = a + b`，`a *= a + 2`相当于`a = a * (a + 2)`。下面的例子演示了赋值运算符和复合赋值运算符的使用。

~~~python
"""
赋值运算符和复合赋值运算符

Version: 1.0
Author: 骆昊
"""
a = 10
b = 3
a += b        # 相当于：a = a + b
a *= a + 2    # 相当于：a = a * (a + 2)
print(a)      # 大家算一下这里会输出什么
~~~



赋值运算构成的表达式本身不产生任何值，也就是说，如果你把一个赋值表达式放到`print`函数中试图输出表达式的值，将会产生语法错误。为了解决这个问题，Python 3.8 中引入了一个新的赋值运算符`:=`，我们称之为海象运算符，大家可以猜一猜它为什么叫这个名字。海象运算符也是将运算符右侧的值赋值给左边的变量，与赋值运算符不同的是，运算符右侧的值也是整个表达式的值，看看下面的代码大家就明白了。

```python
"""
海象运算符

Version: 1.0
Author: 骆昊
"""
# SyntaxError: invalid syntax
# print((a = 10))
# 海象运算符
print((a := 10))  # 10
print(a)          # 10
```



> **提示**：上面第 8 行代码如果不注释掉，运行代码会看到`SyntaxError: invalid syntax`错误信息，注意，这行代码中我们给`a = 10`加上了圆括号，如果不小心写成了`print(a = 10)`，会看到`TypeError: 'a' is an invalid keyword argument for print()`错误信息，后面讲到函数的时候，大家就会明白这个错误提示是什么意思了。





#### 2.2.3 海象运算符

```python
# 在循环中使用海象运算符
print("--------在循环中使用海象运算符---------")
while (line := input("请输入内容，输入exit退出: ")) != "exit":
    print(f"你输入的内容是: {line}")
print("--------在循环中使用海象运算符---------\n")

# 注意：海象运算符不能取代所有的赋值语句
# 例如下面的代码就会报错
# if (n := len(input("请输入内容: "))) > 5 and n < 10:
#     print("你输入的内容长度在5到10之间")
# print(n)  # NameError: name 'n' is not defined

# 正确的写法应该是
n = len(input("请输入内容: "))
if n > 5 and n < 10:
    print("你输入的内容长度在5到10之间")
print(n)  # 这里的n是可以访问的
```



#### 2.2.4 位运算符

整数在计算机中以 **二进制** 存储。
 位运算就是**直接操作二进制位（bit）** 的运算。

举个例子：
 `5` 的二进制是 `0101`
 `3` 的二进制是 `0011`



##### 1️⃣ 位与赋值 `&=`

```
x = 5      # 二进制 0101
x &= 3     # 二进制 0011
```

运算过程：

```
0101
& 0011
= 0001
```

- `&` 表示“按位与”：
  - 1 & 1 → 1
  - 1 & 0 → 0
  - 0 & 1 → 0
  - 0 & 0 → 0

结果 `0001` → 十进制是 `1`
 👉 **输出：1**

------



##### 2️⃣ 位或赋值 `|=`

```
x = 5      # 0101
x |= 3     # 0011
```

运算过程：

```
0101
| 0011
= 0111
```

- `|` 表示“按位或”：
  - 只要有一个是 1，结果就是 1。

结果 `0111` → 十进制是 `7`
 👉 **输出：7**

------



##### 3️⃣ 位异或赋值 `^=`

```
x = 5      # 0101
x ^= 3     # 0011
```

运算过程：

```
0101
^ 0011
= 0110
```

- `^` 表示“按位异或”（相同为 0，不同为 1）

结果 `0110` → 十进制是 `6`
 👉 **输出：6**

------



##### 4️⃣ 左移赋值 `<<=`

```
x = 5      # 0101
x <<= 1    # 左移 1 位
```

运算过程：

```
0101 << 1 = 1010
```

- 左移相当于乘以 2。
  `1010` → 十进制是 `10`
  👉 **输出：10**

------



##### 5️⃣ 右移赋值 `>>=`

```
x = 5      # 0101
x >>= 1    # 右移 1 位
```

运算过程：

```
0101 >> 1 = 0010
```

- 右移相当于除以 2（向下取整）。
  `0010` → 十进制是 `2`
  👉 **输出：2**

------



##### ✅ 总结对比表：

| 运算符      | 含义         | 示例（二进制）      | 结果 | 十进制 |
| ----------- | ------------ | ------------------- | ---- | ------ |
| `&=`        | 按位与赋值   | 0101 & 0011 = 0001  | 0001 | 1      |
| `      | =` | 按位或赋值   | 0101 \| 0011 = 0111 | 0111 |        |
| `^=`        | 按位异或赋值 | 0101 ^ 0011 = 0110  | 0110 | 6      |
| `<<=`       | 左移赋值     | 0101 << 1 = 1010    | 1010 | 10     |
| `>>=`       | 右移赋值     | 0101 >> 1 = 0010    | 0010 | 2      |





#### 2.2.5 二进制(补充内容)

##### 1️⃣举例：什么是“二进制”

二进制的每一位只能是 **0 或 1**，
 每一位的“权重”是 **2 的幂**：

| 位数   | 权重（从右往左） | 说明   |
| ------ | ---------------- | ------ |
| 最右边 | 2⁰ = 1           | 个位   |
| 第二位 | 2¹ = 2           | “二位” |
| 第三位 | 2² = 4           | “四位” |
| 第四位 | 2³ = 8           | “八位” |

举个例子：
 二进制 `101`
 = (1 × 2²) + (0 × 2¹) + (1 × 2⁰)
 = 4 + 0 + 1 = **5（十进制）**

------



##### 2️⃣ 怎么从十进制得到二进制？

我们要做的，就是把十进制的数**拆成若干个 2 的幂**。

> “除 2 取余法” 就是找出这些 0/1 位的方法。



##### 3️⃣ 示例：把 5 转成二进制

| 步骤  | 运算  | 商   | 余数（当前最低位） |
| ----- | ----- | ---- | ------------------ |
| 第1步 | 5 ÷ 2 | 2    | **1**              |
| 第2步 | 2 ÷ 2 | 1    | **0**              |
| 第3步 | 1 ÷ 2 | 0    | **1**（结束）      |

👉 然后从**下往上读余数**：
 `101`

------



为什么要倒着读？
 因为第一次取的余数是“最低位（2⁰ 位）”，
 第二次取的余数是“次低位（2¹ 位）”，
 依次类推。

------



##### 4️⃣ 再看 3 的例子：

| 步骤  | 运算  | 商   | 余数  |
| ----- | ----- | ---- | ----- |
| 第1步 | 3 ÷ 2 | 1    | **1** |
| 第2步 | 1 ÷ 2 | 0    | **1** |

👉 倒着读余数：`11`

也就是：

```
3 (十进制) = 11 (二进制)
```







#### 2.2.6 比较运算符

比较运算符也称为关系运算符，包括`==`、`!=`、`<`、`>`、`<=`、`>=`，我相信大家一看就能懂。需要提醒的是比较相等用的是`==`，请注意这里是两个等号，因为`=`是赋值运算符，我们在上面刚刚讲到过。比较不相等用的是`!=`，跟数学课本中使用的$\small{\neq}$或≠并不相同，Python 2 中曾经使用过`<>`来表示不等于，在 Python 3 中使用`<>`会引发`SyntaxError`（语法错误）。比较运算符会产生布尔值，要么是`True`，要么是`False`。



**数学符号与编程符号对照表**

| 数学符号 | 编程符号 | 含义     |
| :------- | :------- | :------- |
| `=`      | `==`     | 等于     |
| `≠`      | `!=`     | 不等于   |
| `>`      | `>`      | 大于     |
| `<`      | `<`      | 小于     |
| `≥`      | `>=`     | 大于等于 |
| `≤`      | `<=`     | 小于等于 |



`operator_sample04.py`

~~~python
# 数学: 5 ≠ 3
# Python:
print(5 != 3)  # True

# 数学: x ≠ y  
# Python:
x = 10
y = 20
if x != y:
    print(f"{x} 不等于 {y}")
# 输出: x不等于y
elif x == y:
    print(f"{x} 等于 {y}")
# 输出: x等于y
elif x > y:
    print(f"{x} 大于 {y}")
# 输出: x大于y
elif x < y:
    print(f"{x} 小于 {y}")
# 输出: x小于y
elif x >= y:
    print(f"{x} 大于等于 {y}")
# 输出: x大于等于y
elif x <= y:
    print(f"{x} 小于等于 {y}")
else:
    print("无法比较")
~~~



`operator_sample05.py`

```python
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
```

> **说明**：比较运算符的优先级高于赋值运算符，所以上面的`flag0 = 1 == 1`先做`1 == 1`产生布尔值`True`，再将这个值赋值给变量`flag0`。`print`函数可以输出多个值，多个值之间可以用`,`进行分隔，输出的内容默认以空格分开。





#### 2.2.7 逻辑运算符

逻辑运算符有三个，分别是`and`、`or`和`not`。`and`字面意思是“而且”，所以`and`运算符会连接两个布尔值或者产生布尔值的表达式，如果两边的布尔值都是`True`，那么运算的结果就是`True`；左右两边的布尔值有一个是`False`，最终的运算结果就是`False`。当然，如果`and`运算符左边的布尔值是`False`，不管右边的布尔值是什么，最终的结果都是`False`，这时运算符右边的布尔值会被跳过（专业的说法叫短路处理，如果`and`右边是一个表达式，那么这个表达式不会执行）。`or`字面意思是“或者”，所以`or`运算符也会连接两个布尔值或产生布尔值的表达式，如果两边的布尔值有任意一个是`True`，那么最终的结果就是`True`。当然，`or`运算符也是有短路功能的，当它左边的布尔值为`True`的情况下，右边的布尔值会被短路（如果`or`右边是一个表达式，那么这个表达式不会执行）。`not`运算符的后面可以跟一个布尔值，如果`not`后面的布尔值或表达式是`True`，那么运算的结果就是`False`；如果`not`后面的布尔值或表达式是`False`，那么运算的结果就是`True`。



##### 1️⃣ 什么是逻辑运算符？

逻辑运算符是用来**连接多个条件表达式**（True 或 False）并产生一个新的布尔结果的运算符。
通俗点说，就是让程序能做出**“同时满足”“至少一个满足”“不满足”**等判断。



##### 2️⃣ Python 中的三个逻辑运算符

| 运算符 | 含义           | 示例             | 结果    |
| ------ | -------------- | ---------------- | ------- |
| `and`  | 逻辑与（并且） | `True and False` | `False` |
| `or`   | 逻辑或（或者） | `True or False`  | `True`  |
| `not`  | 逻辑非（取反） | `not True`       | `False` |



##### 3️⃣ 逻辑真值表

| A     | B     | `A and B` | `A or B` | `not A` |
| ----- | ----- | --------- | -------- | ------- |
| True  | True  | True      | True     | False   |
| True  | False | False     | True     | False   |
| False | True  | False     | True     | True    |
| False | False | False     | False    | True    |



##### 4️⃣ 例子讲解

```python
a = True
b = False

print(a and b)  # False：必须都为 True
print(a or b)   # True：有一个 True 就行
print(not a)    # False：a 是 True，取反
```



##### 5️⃣ 结合条件判断使用

逻辑运算符常和比较符号一起使用：

```python
x = 8

# and：两个条件都成立
if x > 0 and x < 10:
    print("x 在 0 到 10 之间")

# or：只要一个条件成立
if x < 0 or x == 8:
    print("x 小于 0 或等于 8")

# not：取反
if not (x == 5):
    print("x 不是 5")
```

输出：

```
x 在 0 到 10 之间
x 小于 0 或等于 8
x 不是 5
```



##### 6️⃣ 逻辑“短路”机制（short-circuit）

Python 为了提高效率，有一个特性叫“**短路**”：

- `A and B`：如果 `A` 为 False，Python 不会再计算 `B`
- `A or B`：如果 `A` 为 True，Python 不会再计算 `B`

示例：

```python
def test():
    print("执行了 test()")
    return True

print(False and test())  # 不执行 test()
print(True or test())    # 不执行 test()
```



##### 7️⃣ 逻辑运算符 vs 位运算符

| 类型       | 运算符                           | 操作对象             | 示例                           | 结果    |
| ---------- | -------------------------------- | -------------------- | ------------------------------ | ------- |
| 逻辑运算符 | `and`, `or`, `not`               | 布尔值（True/False） | `True and False`               | `False` |
| 位运算符   | `&`, `             | `, `~`, `^` | 二进制位             | `5 & 3` → `0101 & 0011 = 0001` |         |

👉 **区别**：逻辑运算符处理真假，位运算符处理二进制位。





#### 2.2.8 运算符和表达式应用

##### 1️⃣  例子1：华氏温度转摄氏温度

> **要求**：输入华氏温度将其转换为摄氏温度，华氏温度到摄氏温度的转换公式为： C=(F−32)/1.8 。

~~~python
"""
将华氏温度转换为摄氏温度

Version: 1.0
Author: 骆昊
"""
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
~~~

> **说明**：上面代码中的`input`函数用于从键盘接收用户输入，由于输入的都是字符串，如果想处理成浮点小数来做后续的运算，可以用我们上一课讲解的类型转换的方法，用`float`函数将`str`类型处理成`float`类型。

上面的代码中，我们对`print`函数输出的内容进行了格式化处理，`print`输出的字符串中有两个`%.1f`占位符，这两个占位符会被`%`之后的`(f, c)`中的两个`float`类型的变量值给替换掉，浮点数小数点后保留1位有效数字。如果字符串中有`%d`占位符，那么我们会用`int`类型的值替换掉它，如果字符串中有`%s`占位符，那么它会被`str`类型的值替换掉。



除了上面格式化输出的方式外，Python 中还可以用下面的办法来格式化输出，我们给出一个带占位符的字符串，字符串前面的`f`表示这个字符串是需要格式化处理的，其中的`{f:.1f}`和`{c:.1f}`可以先看成是`{f}`和`{c}`，表示输出时会用变量`f`和变量`c`的值替换掉这两个占位符，后面的`:.1f`表示这是一个浮点数，小数点后保留1位有效数字。

```python
"""
将华氏温度转换为摄氏温度

Version: 1.1
Author: 骆昊
"""
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')
```



##### 2️⃣ 例子2：计算圆的周长和面积

> **要求**：输入一个圆的半径（$\small{r}$），计算出它的周长（ 2πr ）和面积（ πr2 ）。

~~~python
"""
输入半径计算圆的周长和面积

Version: 1.0
Author: 骆昊
"""
radius = float(input('请输入圆的半径: '))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
~~~



Python 中有一个名为`math` 的内置模块，该模块中定义了名为`pi`的变量，它的值就是圆周率。如果要使用 Python 内置的这个`pi`，我们可以对上面的代码稍作修改。

~~~python
"""
输入半径计算圆的周长和面积

Version: 1.1
Author: 骆昊
"""
import math

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'周长: {perimeter:.2f}')
print(f'面积: {area:.2f}')
~~~

> **说明**：上面代码中的`import math`表示导入`math`模块，导入该模块以后，才能用`math.pi`得到圆周率的值。



这里其实还有一种格式化输出的方式，是 Python 3.8 中增加的新特性，大家直接看下面的代码就明白了。

~~~python
"""
输入半径计算圆的周长和面积

Version: 1.2
Author: 骆昊
"""
import math

radius = float(input('请输入圆的半径: '))  # 输入: 5.5
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'{perimeter = :.2f}')  # 输出：perimeter = 34.56
print(f'{area = :.2f}')       # 输出：area = 95.03
~~~



~~~python
"""
Version: 1.0
Author: 李小婕
Keyword arguments:
    radius -- 输入的圆半径 (float)
    Return: 返回一个包含周长和面积的元组 (perimeter, area)
argument -- 输入半径计算圆的周长和面积
Return: 返回计算结果
"""

import math

def calculate_circle(radius):
    """
    计算圆的周长和面积
    Version: 1.0
    Author: 李小婕
    Keyword arguments:
    radius -- 输入半径，用于计算圆的周长和面积
    Return: 返回一个包含周长和面积的元组 (perimeter, area)
    """
    perimeter = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return perimeter, area


# 调用函数并打印结果
r = float(input("请输入圆的半径："))
perimeter, area = calculate_circle(r)

print(f"半径为 {r} 的圆：")
print(f"周长 = {perimeter:.2f}")
print(f"面积 = {area:.2f}")
~~~



`打印输出结果如下：`

```
请输入圆的半径：5.5
半径为 5.5 的圆：
周长 = 34.56
面积 = 95.03
```



> **说明**：假如变量半径`r`的值是`9.87`，那么字符串`f'{r = }'`的值是`a = 9.87`；而字符串`f'{r = :.1f}'`的值是`r = 9.9`。这种格式化输出的方式会同时输出变量名和变量值。



##### 3️⃣ 例子3：判断闰年

> 要求：输入一个 1582 年以后的年份，判断该年份是不是闰年。

```python
"""
输入年份，闰年输出True，平年输出False

Version: 1.0
Author: 骆昊
"""
year = int(input('请输入年份: '))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(f'{is_leap = }')
```

>**说明**：对于格里历（Gregorian calendar），即今天我们使用的公历，判断闰年的规则是：1. 公元年份非 4 的倍数是平年；2. 公元年份为 4 的倍数但非 100 的倍数是闰年；3. 公元年份为 400 的倍数是闰年。格里历是由教皇格里高利十三世在 1582 年 10 月引入的，作为对儒略历（Julian calendar）的修改和替代，我们在输入年份时要注意这一点。上面的代码通过`%`来判断`year`是不是`4`的倍数、`100`的倍数、`400`的倍数，然后用`and`和`or`运算符将三个条件组装在一起，前两个条件要同时满足，第三个条件跟前两个条件的组合只需满足其中之一。





```python
"""
Version:1.0
Author: 李小婕

Keyword arguments:
    year -- 输入年份
    argument -- 输入年份，闰年输出True，平年输出False
    Return: 返回一个布尔值，表示是否为闰年
Description: 判断是否为闰年
"""

def is_leap_year(year):
    """
    判断是否为闰年
    Version: 1.0
    Author: 李小婕
    Keyword arguments:
    year -- 输入年份
    Return: 返回一个布尔值，表示是否为闰年
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

    # 输入年份并调用函数
year = int(input("请输入年份: "))
if is_leap_year(year):
    print(f"{year} 是闰年")
else:
    print(f"{year} 不是闰年")
print("--------判断是否为闰年---------\n")
```



##### ✅ 总结

通过上面的讲解和例子，相信大家已经感受到了运算符和表达式的力量。实际编程中的很多问题，都需通过构造表达式来解决，所以变量、运算符、表达式对于任何一门编程语言都是极为重要的基础。如果本节课的内容有什么不理解的地方，一定不要着急进入下一课，先在评论区留言讨论，我会及时解答大家的问题。





### 2.3 分支结构

迄今为止，我们写的 Python 程序都是一条一条语句按顺序向下执行的，这种代码结构叫做顺序结构。然而仅有顺序结构并不能解决所有的问题，比如我们设计一个游戏，游戏第一关的过关条件是玩家获得 1000 分，那么在第一关完成后，我们要根据玩家得到的分数来决定是进入第二关，还是告诉玩家“Game Over”（游戏结束）。在这种场景下，我们的代码就会产生两个分支，而且只有一个会被执行。类似的场景还有很多，我们将这种结构称之为“分支结构”或“选择结构”。给大家一分钟的时间，你应该可以想到至少 5 个以上类似的例子，赶紧试一试吧！



#### 2.3.1 使用if和else构造分支结构

在 Python 中，构造分支结构最常用的是`if`、`elif`和`else`三个关键字。所谓**关键字**就是编程语言中有特殊含义的单词，很显然你不能够使用它作为变量名。当然，我们并不是每次构造分支结构都会把三个关键字全部用上，我们通过例子加以说明。例如我们要写一个身体质量指数（BMI）的计算器。身体质量质数也叫体质指数，是国际上常用的衡量人体胖瘦程度以及是否健康的一个指标，计算公式如下所示。通常认为 18.5≤BMI<24 是正常范围， BMI<18.5 说明体重过轻， BMI≥24 说明体重过重， BMI≥27 就属于肥胖的范畴了。



##### 1️⃣ BMI（身体质量指数）公式

BMI (Body Mass Index) 的计算公式如下：

$$
\text{BMI} = \frac{\text{体重 (kg)}}{\text{身高 (m)}^2}
$$
其中：

- **体重 (kg)** → 以千克（kg）为单位
- **身高 (m)** → 以米（m）为单位



##### 2️⃣ 举例说明

如果一个人的：

体重 = 70 kg  
身高 = 1.75 m  

则：

$$
\text{BMI} = \frac{70}{1.75^2} = \frac{70}{3.0625} \approx 22.86
$$




> **说明**：上面公式中的体重以千克（kg）为单位，身高以米（m）为单位。

~~~python
"""
BMI计算器

Version: 1.0
Author: 骆昊
"""
height = float(input('身高(cm)：'))
weight = float(input('体重(kg)：'))
bmi = weight / (height / 100) ** 2
print(f'{bmi = :.1f}')
if 18.5 <= bmi < 24:
    print('你的身材很棒！')
~~~

> **提示**：`if`语句的最后面有一个`:`，它是用英文输入法输入的冒号；程序中输入的`'`、`"`、`=`、`(`、`)`等特殊字符，都是在英文输入法状态下输入的，这一点之前已经提醒过大家了。很多初学者经常会忽略这一点，等到执行代码时，就会看到一大堆错误提示。当然，认真读一下错误提示还是很容易发现哪里出了问题，但是**强烈建议**大家在写代码的时候**切换到英文输入法**，这样可以避免很多不必要的麻烦。





接下来，我们对上面的代码稍作修改，在 BMI 不满足 18.5≤BMI<24 的情况下，也给出相信的提示信息。我们可以在`if`代码块的后面增加一个`else`代码块，它会在`if`语句给出的条件没有达成时执行，如下所示。很显然，`if`下面的`print('你的身材很棒！')`和`else`下面的`print('你的身材不够标准哟！')`只有一个会被执行到。

~~~python
"""
BMI计算器

Version: 1.1
Author: 骆昊
"""
height = float(input('身高(cm)：'))
weight = float(input('体重(kg)：'))
bmi = weight / (height / 100) ** 2
print(f'{bmi = :.1f}')
if 18.5 <= bmi < 24:
    print('你的身材很棒！')
else:
    print('你的身材不够标准哟！')
~~~







`branch_sample01.py`

~~~Python
"""
BMI 身体质量指数计算公式
Version: 1.0
Author: 李小婕
Description: 根据用户输入的身高（米）和体重（公斤）计算 BMI 指数并给出健康建议
"""
height = float(input("请输入您的身高（米）："))
weight = float(input("请输入您的体重（公斤）："))
bmi = weight / (height ** 2)
print(f"您的 BMI 指数为: {bmi:.2f}")
if bmi < 18.5:
    print("体重过轻，请注意营养均衡。")
elif 18.5 <= bmi < 24:
    print("体重正常，保持良好的生活习惯。")
elif 24 <= bmi < 28:
    print("体重过重，请注意饮食和锻炼。")
else:
    print("肥胖，请积极控制体重，注意健康。")
print("--------BMI 身体质量指数计算---------\n")
~~~



#### 2.3.2 使用match和case构造分支结构

Python 3.10 中增加了一种新的构造分支结构的方式，通过使用`match`和`case` 关键字，我们可以轻松的构造出多分支结构。Python 的官方文档在介绍这个新语法时，举了一个 HTTP 响应状态码识别的例子（根据 HTTP 响应状态输出对应的描述），非常有意思。如果不知道什么是 HTTP 响应状态吗，可以看看 MDN 上面的[文档](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status)。下面我们对官方文档上的示例稍作修改，为大家讲解这个语法，先看看下面用`if-else`结构实现的代码。



`branch_sample02.py`

~~~python
"""
Version: 1.0
Author: 李小婕
Description: 使用match和case构造分支结构
Date: 2025-10-12
"""
print("--------成绩等级评定---------")
score = int(input("请输入您的成绩（0-100）："))
match score:
    case s if 90 <= s <= 100:
        grade = 'A'
    case s if 80 <= s < 90:
        grade = 'B'
    case s if 70 <= s < 80:
        grade = 'C'
    case s if 60 <= s < 70:
        grade = 'D'
    case s if 0 <= s < 60:
        grade = 'F'
    case _:
        grade = None
if grade:
    print(f"您的成绩等级为: {grade}")
else:
    print("输入的成绩无效，请输入0到100之间的数字。")
print("--------成绩等级评定---------\n")
~~~



`打印输出结果：`

```
--------成绩等级评定---------
请输入您的成绩（0-100）：85
您的成绩等级为: B
--------成绩等级评定---------
```





> 下面是使用`match-case`语法实现的代码，虽然作用完全相同，但是代码显得更加简单优雅。

~~~python
status_code = int(input('响应状态码: '))
match status_code:
    case 400: description = 'Bad Request'
    case 401: description = 'Unauthorized'
    case 403: description = 'Forbidden'
    case 404: description = 'Not Found'
    case 405: description = 'Method Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('状态码描述:', description)
~~~



> **说明**：带有`_`的`case`语句在代码中起到通配符的作用，如果前面的分支都没有匹配上，代码就会来到`case _`。`case _`的是可选的，并非每种分支结构都要给出通配符选项。如果分支中出现了`case _`，它只能放在分支结构的最后面，如果它的后面还有其他的分支，那么这些分支将是不可达的。



当然，`match-case`语法还有很多高级玩法，其中有一个合并模式可以先教给大家。例如，我们要将响应状态码`401`、`403`和`404`归入一个分支，`400`和`405`归入到一个分支，其他保持不变，代码还可以这么写。



~~~python
status_code = int(input('响应状态码: '))
match status_code:
    case 400 | 405: description = 'Invalid Request'
    case 401 | 403 | 404: description = 'Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('状态码描述:', description)
~~~



#### 2.3.3 分支结构的应用

##### 1️⃣ 例子1：分段函数求值

 有如下所示的分段函数，要求输入`x`，计算出`y`。

函数 \(y\) 定义为：

$$
y = 
\begin{cases} 
3x - 5, & x > 1 \\[2mm]
x + 2, & -1 \le x \le 1 \\[1mm]
5x + 3, & x < -1
\end{cases}
$$

~~~python
"""
分段函数求值

Version: 1.0
Author: 骆昊
"""
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(f'{y = }')
~~~





有如下所示的分段函数，要求输入`x`，计算出函数 `f(x) `。

函数 \(f(x)\) 定义为：

$$
f(x) =
\begin{cases} 
2x - 1, & x > 1 \\[1mm]
x^2, & -1 \le x \le 1 \\[1mm]
2|x| + 1, & x < -1
\end{cases}
$$

~~~python
"""
分段函数，要求输入一个实数x，输出如下值：
If x>1, then f(x)=2x-1;
If -1<=x<=1, then f(x)=x^2;
If x<-1, then f(x)=2|x|+1.
Version: 1.0
Author: 李小婕
Keyword arguments:
x -- 输入的实数
Return: 返回分段函数的值
"""
print("--------分段函数计算---------")
def piecewise_function(x):
    match x:
        case _ if x > 1:
            return 2 * x - 1
        case _ if -1 <= x <= 1:
            return x ** 2
        case _ if x < -1:
            return 2 * abs(x) + 1
    return None

x = float(input("请输入一个实数x: "))
result = piecewise_function(x)
print(f"f({x}) = {result}")
print("--------分段函数计算---------\n")
~~~



```
--------分段函数计算---------
请输入一个实数x: -3
f(-3.0) = 7.0
--------分段函数计算---------

--------分段函数计算---------
请输入一个实数x: 0.2
f(0.2) = 0.04000000000000001
--------分段函数计算---------
```







##### 2️⃣ 例子2：百分制成绩转换成等级

要求：如果输入的成绩在90分以上（含90分），则输出`A`；输入的成绩在80分到90分之间（不含90分），则输出`B`；输入的成绩在70分到80分之间（不含80分），则输出`C`；输入的成绩在60分到70分之间（不含70分），则输出`D`；输入的成绩在60分以下，则输出`E`.



~~~python
"""
百分制成绩转换为等级制成绩

Version: 1.0
Author: 骆昊
"""
score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print(f'{grade = }')
~~~



```python
"""
如果输入的成绩在90分以上（含90分），则输出`A`；
输入的成绩在80分到90分之间（不含90分），则输出`B`；
输入的成绩在70分到80分之间（不含80分），则输出`C`；
入的成绩在60分到70分之间（不含70分），则输出`D`；
输入的成绩在60分以下，则输出`E`.

使用match和case构造分支结构实现上述功能。
Args:
    score -- 输入的成绩
Raises:
    ValueError -- 如果输入的成绩不在0到100之间，抛出异常

Version: 1.0
Author: 李小婕
Date: 2025-10-12

Keyword arguments:
score -- 输入的成绩
Return: 返回对应的等级
"""
print("--------成绩等级评定---------")
def get_grade(score):
    match score:
        case _ if score >= 90 and score <= 100:
            return "A"
        case _ if 80 <= score < 90:
            return "B"
        case _ if 70 <= score < 80:
            return "C"
        case _ if 60 <= score < 70:
            return "D"
        case _ if score >= 0 and score < 60:
            return "E"
        case _:
            raise ValueError("成绩不在0到100之间")

score = int(input("请输入您的成绩（0-100）："))
try:
    grade = get_grade(score)
    print(f"您的成绩等级为: {grade}")
    print(f"您的成绩分数为: {score}")
except ValueError as e:
    print(e)
print("--------成绩等级评定---------\n")
```











##### 3️⃣ 例子3：计算三角形的周长和面积。

> 要求：输入三条边的长度，如果能构成三角形就计算周长和面积；否则给出“不能构成三角形”的提示。

~~~python
"""
计算三角形的周长和面积

Version: 1.0
Author: 骆昊
"""
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    print(f'周长: {perimeter}')
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f'面积: {area}')
else:
    print('不能构成三角形')
~~~



**说明：** 上面的 `if` 条件表示任意两边之和大于第三边，这是构成三角形的必要条件。当这个条件成立时，我们要计算并输出周长和面积，所以 `if` 下方的五条语句都保持了相同的缩进，它们是一个整体，只要 `if` 条件成立，它们都会被执行，这就是我们之前提到的代码块的概念。

另外，上面计算三角形面积的公式叫做 **海伦公式**，假设有一个三角形，边长分别为 a、b、c，那么三角形的面积 AAA 可以由公式得到:

**三角形面积计算（海伦公式）**

给定三角形的三条边长分别为 \(a\)、\(b\)、\(c\)，首先计算半周长 \(s\)：

$$
s = \frac{a + b + c}{2}
$$

然后计算面积 \(A\)：

$$
A = \sqrt{s(s-a)(s-b)(s-c)}
$$

> 其中，\(s\) 表示三角形的半周长，\(A\) 表示三角形的面积。







##### 4️⃣ 例子4：课程成绩等级及网页显示。

~~~python
import webbrowser

# 输入成绩
score = int(input("请输入成绩（0-100）："))

# 计算成绩等级
def get_grade(score):
    if score < 0 or score > 100:
        return "成绩不在0到100之间"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"

grade = get_grade(score)

# HTML 内容（使用本地 Logo，路径用正斜杠）
html_content = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>Python程序设计 - 成绩等级评定</title>
<style>
body {{
    font-family: "Microsoft YaHei", Arial, sans-serif;
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #0099ff, #00cc99);
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}}
.card {{
    background-color: rgba(255,255,255,0.95);
    border-radius: 15px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    padding: 30px 50px;
    text-align: center;
    width: 400px;
}}
.card img {{
    width: 190px;
    height: 60px;
    margin-bottom: 20px;
}}
h2 {{
    color: #004080;
    margin-bottom: 15px;
}}
p {{
    font-size: 18px;
    margin: 8px 0;
    color: #333;
}}
</style>
</head>
<body>
<div class="card">
    <!-- 使用本地 Logo 文件 -->
    <img src="C:/Users/86181/Desktop/Vscode_python/day05/tut_logo.png" alt="天津理工大学 Logo">
    <h2>Python程序设计 - 成绩等级评定</h2>
    <p>您的成绩分数为：{score}</p>
    <p>您的成绩等级为：{grade}</p>
</div>
</body>
</html>
"""

# 保存 HTML 文件
html_file = "grade_result.html"
with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

# 自动在默认浏览器中打开
webbrowser.open(html_file)
~~~





```
请输入成绩（0-100）：100

```

![image-20251012171404145](C:\Users\86181\AppData\Roaming\Typora\typora-user-images\image-20251012171404145.png)













##### ✅ 总结

学会了 Python 中的分支结构，我们就可以解决很多实际的问题了。这一节课相信已经帮助大家掌握了构造分支结构的方法，下一节课我们为大家介绍循环结构，学完这两次课你一定会发现，你能写出很多很有意思的代码，继续加油吧！



#### 2.2.4 循环结构

我们在写程序的时候，极有可能遇到需要重复执行某条或某些指令的场景，例如我们需要每隔1秒钟在屏幕上输出一次“hello, world”并持续输出一个小时。如下所示的代码可以完成一次这样的操作，如果要持续输出一个小时，我们就需要把这段代码写3600遍，你愿意这么做吗？

~~~python
import time

print('hello, world')
time.sleep(1)
~~~



> **说明**：Python 内置`time`模块的`sleep`函数可以实现程序的休眠，参数`1`表示休眠的秒数，可以使用`int`或`float`类型，例如`0.05`表示`50`毫秒。关于函数和模块的知识，我们在后续的课程中会为大家讲解。





##### 1️⃣ for-in循环

为了应对上述场景中的问题，我们可以在 Python 程序中使用循环结构。所谓循环结构，就是程序中控制某条或某些指令重复执行的结构。有了这样的结构，刚才的代码就不需要写 3600 遍，而是写一遍然后放到循环结构中重复 3600 次。在 Python 语言中构造循环结构有两种做法，一种是`for-in`循环，另一种是`while`循环。

~~~python
"""
每隔1秒输出一次“hello, world”，持续1小时

Author: 骆昊
Version: 1.0
"""
import time

for i in range(3600):
    print('hello, world')
    time.sleep(1)
~~~

需要说明的是，上面代码中的`range(3600)`可以构造出一个从`0`到`3599`的范围，当我们把这样一个范围放到`for-in`循环中，就可以通过前面的循环变量`i`依次取出从`0`到`3599`的整数，这就会让`for-in`代码块中的语句重复 3600 次。当然，`range`的用法非常灵活，下面的清单给出了使用`range`函数的例子：

- `range(101)`：可以用来产生`0`到`100`范围的整数，需要注意的是取不到`101`。
- `range(1, 101)`：可以用来产生`1`到`100`范围的整数，相当于是左闭右开的设定，即`[1, 101)`。
- `range(1, 101, 2)`：可以用来产生`1`到`100`的奇数，其中`2`是步长（跨度），即每次递增的值，`101`取不到。
- `range(100, 0, -2)`：可以用来产生`100`到`1`的偶数，其中`-2`是步长（跨度），即每次递减的值，`0`取不到。





大家可能已经注意到了，上面代码的输出操作和休眠操作都没有用到循环变量`i`，对于不需要用到循环变量的`for-in`循环结构，按照 Python 的编程惯例，我们通常把循环变量命名为`_`，修改后的代码如下所示。虽然结果没什么变化，但是这样写显得你更加专业，逼格瞬间拉满。

```python
"""
每隔1秒输出一次“hello, world”，持续1小时

Author: 骆昊
Version: 1.1
"""
import time

for _ in range(3600):
    print('hello, world')
    time.sleep(1)
```



上面的代码要执行一个小时，如果想提前结束程序，在 PyCharm 中可以点击运行窗口上的停止按钮，如下图所示。如果在命令提示符或终端中运行代码，可以使用组合键`ctrl+c`来终止程序。

![img](https://github.com/jackfrued/Python-100-Days/raw/master/Day01-20/res/day06/terminate_program.png)



下面，我们用`for-in`循环实现从 1 到 100 的整数求和，即 
$$
\sum_{n=1}^{100} n
$$


```python
"""
从1到100的整数求和

Version: 1.0
Author: 骆昊
"""
total = 0
for i in range(1, 101):
    total += i
print(total)
```



上面的代码中，变量`total`的作用是保存累加的结果。在循环的过程中，循环变量`i`的值会从 1 一直取到 100。对于变量`i`的每个取值，我们都执行了`total += i`，它相当于`total = total + i`，这条语句实现了累加操作。所以，当循环结束，我们输出变量`total` 的值，它的值就是从 1 累加到 100 的结果 5050。注意，`print(total)`这条语句前是没有缩进的，它不受`for-in`循环的控制，不会重复执行。





```python
"""
Version: 1.0
Author: 李小婕
Date: 2025-10-13
Description: 从1到100的整数求和

Keyword arguments:
argument -- description
Return: return_description
"""
sum = 0
for i in range(1, 101):
    sum += i
    print(i, end=' ')
    
print("1到100的整数之和为:", sum)

```





```python
"""
Version: 1.0
Author: 李小婕
Description: 每间隔1秒钟打印输出 hello world!，持续一个小时共打印5次
Date: 2025-10-13

Keyword arguments:
argument -- description
Return: return_description
"""
print("--------循环打印---------")
import time # 导入时间模块
count = 0   # 计数器初始化
while count < 5: # 循环5次
    print("hello world!") # 打印输出
    count += 1 # 计数器加1
    time.sleep(2) # 每次循环后暂停1秒钟
print("--------循环打印---------\n")
```





```python
"""
Version: 1.0
Author: 李小婕
Description: 我们再来写一个从1到100偶数求和的代码，并且在每次循环中打印当前的偶数。
Date: 2025-10-13

Keyword arguments:
argument -- description
Return: return_description
"""
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum += i
        print(i, end=' ')
print("1到100的偶数之和为:", sum)
```





我们再来写一个从1到100偶数求和的代码，如下所示。

```python
"""
Version: 1.0
Author: 李小婕
Description: 我们再来写一个从1到100偶数求和的代码，并且在每次循环中打印当前的偶数。
Date: 2025-10-13

Keyword arguments:
argument -- description
Return: return_description
"""
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum += i
        print(i, end=' ')
print("1到100的偶数之和为:", sum)

```

> **说明**：上面的`for-in`循环中我们使用了分支结构来判断循环变量`i`是不是偶数。



我们也可以修改`range`函数的参数，将起始值和跨度修改为`2`，用更为简单的代码实现从 1 到 100 的偶数求和。

~~~python
"""
Version: 1.0
Author: 李小婕
Date: 2025-10-13
Description: 从1到100的整数求和

Keyword arguments:
argument -- description
Return: return_description
"""
sum = 0
for i in range(1, 101, 2):
    sum += i
    print(i, end=' ')
    
print("1到100的整数之和为:", sum)
~~~

```
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99 1到100的整数之和为: 2500
```



当然， 更为简单的办法是使用 Python 内置的`sum`函数求和，这样我们连循环结构都省掉了。

```python
"""
Version: 1.1
Author: 李小婕
Date: 2025-10-13
Description: 从1到100的整数求和
"""
print(sum(range(2, 101, 2)))
```





##### 2️⃣ while循环

如果要构造循环结构但是又不能确定循环重复的次数，我们推荐使用`while`循环。`while`循环通过布尔值或能产生布尔值的表达式来控制循环，当布尔值或表达式的值为`True`时，循环体（`while`语句下方保持相同缩进的代码块）中的语句就会被重复执行，当表达式的值为`False`时，结束循环。

下面我们用`while`循环来实现从 1 到 100 的整数求和，代码如下所示。

```python
"""
Version: 1.0
Author: 李小婕
Description: 我们再来写一个从1到100求和的代码，并且在每次循环中打印当前数字。
Date: 2025-10-13
Keyword arguments:
argument -- description
Return: return_description
"""
sum = 0
i = 1
while i <= 100:
    sum += i
    print(i, end=' ')
    i += 1
print("1到100的数字之和为:", sum)

# 1.初始化变量 i = 1, sum = 0
# 2.条件 i <= 100
# 3.循环体 sum += i, print(i, end=' '), i += 1
# 4.重复2-3步
# 5.结束循环，打印结果 print("1到100的数字之和为:", sum)
# 6.优化代码 for i in range(1, 101)
# 7.优化代码 for i in range(2, 101, 2)
# 8.优化代码 while i <= 100, i += 2
# 9.优化代码 for i in range(2, 101, 2)
# 10.总结代码   从1到100的数字之和为: 5050
# 11.练习代码   如何将1到100的偶数之和的计算过程用函数封装起来？
def sum_of_even_numbers(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total
print("1到100的偶数之和为:", sum_of_even_numbers(100))

# 12.思考代码   如何将1到100的数字之和的计算过程用函数封装起来？
def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print("1到100的数字之和为:", sum_of_numbers(100))

# 13.扩展代码  将函数改为支持任意范围的数字之和计算
def sum_of_range(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total
print("1到100的数字之和为:", sum_of_range(1, 100))
print("50到150的数字之和为:", sum_of_range(50, 150))

# 14.应用代码   将函数改为支持计算偶数之和
def sum_of_even_numbers(start, end):
    total = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            total += i
    return total
print("1到100的偶数之和为:", sum_of_even_numbers(1, 100))

# 15.项目代码   将函数改为支持计算奇数之和
def sum_of_odd_numbers(start, end):
    total = 0
    for i in range(start, end + 1):
        if i % 2 != 0:
            total += i
    return total
print("1到100的奇数之和为:", sum_of_odd_numbers(1, 100))

# 16.实战代码·  将函数改为支持计算任意步长的数字之和
def sum_of_numbers_with_step(start, end, step):
    total = 0
    for i in range(start, end + 1, step):
        total += i
    return total
print("1到100的数字之和为:", sum_of_numbers_with_step(1, 100, 1))
print("1到100的偶数之和为:", sum_of_numbers_with_step(2, 100, 2))
print("1到100的奇数之和为:", sum_of_numbers_with_step(1, 100, 2))

# 17.案例代码   将函数改为支持计算任意范围和任意步长的数字之和
def sum_of_numbers_with_step(start, end, step):
    total = 0
    for i in range(start, end + 1, step):
        total += i
        print(i, end=' ')
    return total
print("1到100的数字之和为:", sum_of_numbers_with_step(1, 100, 1))
print("1到100的偶数之和为:", sum_of_numbers_with_step(2, 100, 2))
print("1到100的奇数之和为:", sum_of_numbers_with_step(1, 100, 2))

# 18.示例代码   将函数改为支持计算任意范围和任意步长的数字之和
def sum_of_numbers_with_step(start, end, step):
    total = 0
    for i in range(start, end + 1, step):
        total += i
        print(i, end=' ')
    return total
print("1到100的数字之和为:", sum_of_numbers_with_step(1, 100, 1))
print("1到100的偶数之和为:", sum_of_numbers_with_step(2, 100, 2))
print("1到100的奇数之和为:", sum_of_numbers_with_step(1, 100, 2))

# 19.样例代码   将函数改为支持计算任意范围和任意步长的数字之和
def sum_of_numbers_with_step(start, end, step):
    total = 0
    for i in range(start, end + 1, step):
        total += i
        print(i, end=' ')
    return total
print("1到100的数字之和为:", sum_of_numbers_with_step(1, 100, 1))
print("1到100的偶数之和为:", sum_of_numbers_with_step(2, 100, 2))
print("1到100的奇数之和为:", sum_of_numbers_with_step(1, 100, 2))

# 20.范例代码   将函数改为支持计算任意范围和任意步长的数字之和
def sum_of_numbers_with_step(start, end, step):
    total = 0
    for i in range(start, end + 1, step):
        total += i
        print(i, end=' ')
    return total
print("1到100的数字之和为:", sum_of_numbers_with_step(1, 100, 1))
print("1到100的偶数之和为:", sum_of_numbers_with_step(2, 100, 2))
print("1到100的奇数之和为:", sum_of_numbers_with_step(1, 100, 2))

# 21.模板代码   将函数改为支持计算任意范围和任意步长的数字之和
def sum_of_numbers_with_step(start, end, step):
    total = 0
    for i in range(start, end + 1, step):
        total += i
        print(i, end=' ')
    return total
print("1到100的数字之和为:", sum_of_numbers_with_step(1, 100, 1))
print("1到100的偶数之和为:", sum_of_numbers_with_step(2, 100, 2))
print("1到100的奇数之和为:", sum_of_numbers_with_step(1, 100, 2))

# 22.框架代码  将函数改为支持计算任意范围和任意步长的数字之和
def sum_of_numbers_with_step(start, end, step):
    total = 0
    for i in range(start, end + 1, step):
        total += i
        print(i, end=' ')
    return total
print("1到100的数字之和为:", sum_of_numbers_with_step(1, 100, 1))
print("1到100的偶数之和为:", sum_of_numbers_with_step(2, 100, 2))
print("1到100的奇数之和为:", sum_of_numbers_with_step(1, 100, 2))

# 23.结构代码 将函数改为支持计算任意范围和任意步长的数字之和
def sum_of_numbers_with_step(start, end, step):
    total = 0
    for i in range(start, end + 1, step):
        total += i
        print(i, end=' ')
    return total
print("1到100的数字之和为:", sum_of_numbers_with_step(1, 100, 1))
print("1到100的偶数之和为:", sum_of_numbers_with_step(2, 100, 2))
print("1到100的奇数之和为:", sum_of_numbers_with_step(1, 100, 2))

# 24.循环代码 将函数改为支持计算任意范围和任意步长的数字之和
def sum_of_numbers_with_step(start, end, step):
    total = 0
    for i in range(start, end + 1, step):
        total += i
        print(i, end=' ')
    return total    
print("1到100的数字之和为:", sum_of_numbers_with_step(1, 100, 1))
print("1到100的偶数之和为:", sum_of_numbers_with_step(2, 100, 2))
print("1到100的奇数之和为:", sum_of_numbers_with_step(1, 100, 2))
```

相较于`for-in`循环，上面的代码我们在循环开始前增加了一个变量`i`，我们使用这个变量来控制循环，所以`while`后面给出了`i <= 100`的条件。在`while`的循环体中，我们除了做累加，还需要让变量`i`的值递增，所以我们添加了`i += 1`这条语句，这样`i`的值就会依次取到1、2、3、……，直到 101。当`i`变成 101 时，`while`循环的条件不再成立，代码会离开`while`循环，此时我们输出变量`total`的值，它就是从 1 到 100 求和的结果 5050。



如果要实现从 1 到 100 的偶数求和，我们可以对上面的代码稍作修改。

~~~python	
"""
从1到100的偶数求和

Version: 1.3
Author: 骆昊
"""
total = 0
i = 2
while i <= 100:
    total += i
    i += 2
print(total)
~~~



##### 3️⃣ break和continue

如果把`while`循环的条件设置为`True`，即让条件恒成立会怎么样呢？我们看看下面的代码，还是使用`while`构造循环结构，计算 1 到 100 的偶数和。

~~~python
"""
Version: 1.0
Author: 李小婕
Description: 从1到100的偶数求和,并且使用break跳出循环
Date: 2025-10-13

Keyword arguments:
argument -- description
Return: return_description
"""
sum = 0
i = 2
while i <= 100:
    sum += i # 累加当前的偶数
    i += 2 # 每次增加2
    print(i - 2, end=' ') # 打印当前的偶数
    if i > 100: # 使用break跳出循环
        break # 跳出循环
print("1到100的偶数之和为:", sum)

# 1.初始化变量 i = 2, sum = 0
# 2.条件 i <= 100
# 3.循环体 sum += i, i += 2, if i > 100: break
# 4.重复2-3步
# 5.结束循环，打印结果 print("1到100的偶数之和为:", sum)
# 使用break跳出循环的步骤
~~~



```python
"""
Version: 1.0
Author: 李小婕
Description: 从1到100的偶数求和,并且使用break跳出循环
Date: 2025-10-13

Keyword arguments:
argument -- description
Return: return_description
"""
sum = 0
i = 2
while True: # 使用while True创建一个无限循环
    sum += i # 累加当前的偶数
    i += 2 # 每次增加2
    print(i - 2, end=' ') # 打印当前的偶数
    if i > 100: # 使用break跳出循环
        break # 跳出循环
print("1到100的偶数之和为:", sum)

# 1.初始化变量 i = 2, sum = 0
# 2.条件 i <= 100
# 3.循环体 sum += i, i += 2, if i > 100: break
# 4.重复2-3步
# 5.结束循环，打印结果 print("1到100的偶数之和为:", sum)
# 使用break跳出循环的步骤
```

上面的代码中使用`while True`构造了一个条件恒成立的循环，也就意味着如果不做特殊处理，循环是不会结束的，这就是我们常说的“死循环”。为了在`i`的值超过 100 后让循环停下来，我们使用了`break`关键字，它的作用是终止循环结构的执行。需要注意的是，`break`只能终止它所在的那个循环，这一点在使用嵌套循环结构时需要引起注意，后面我们会讲到什么是嵌套的循环结构。除了`break`之外，还有另一个在循环结构中可以使用的关键字`continue`，它可以用来放弃本次循环后续的代码直接让循环进入下一轮，代码如下所示。

~~~python
"""
Version: 1.0
Author: 李小婕
Description: 从1到100的偶数求和,并且使用continue语句跳过奇数
Date: 2025-10-13
Keyword arguments:
argument -- description
Return: return_description
"""
sum = 0
for i in range(1, 101):
    if i % 2 != 0:  # 奇数,比如1,3,5,7,9
        continue
    sum += i
    print(i, end=' ')
print("1到100的偶数之和为:", sum)
# 1.初始化变量 sum = 0
# 2.循环 for i in range(1, 101)
# 3.条件 if i % 2 != 0
# 4.跳过 continue
# 5.循环体 sum += i, print(i, end=' ')
# 6.重复2-5步
# 7.结束循环，打印结果 print("1到100的偶数之和为:", sum)
# 使用continue跳过奇数的步骤
~~~

> **说明**：上面的代码使用`continue`关键字跳过了`i`是奇数的情况，只有在`i`是偶数的前提下，才会执行到`sum += i`。



##### 4️⃣ 嵌套的循环结构

和分支结构一样，循环结构也是可以嵌套的，也就是说在循环结构中还可以构造循环结构。下面的例子演示了如何通过嵌套的循环来输出一个乘法口诀表（九九表）。

~~~python
"""
Version: 1.0
Author: 李小婕
Date: 2025-10-13
Description: 打印乘法口诀表

Keyword arguments:
argument -- description
Return: return_description
"""
for i in range(1, 10): # 外层循环控制行数, 比如1-9行
    for j in range(1, i + 1): # 内层循环控制每行的列数，比如1-9列 
        print(f"{j}*{i}={i*j}", end='\t') # 打印乘法表达式，使用制表符对齐
    print() # 每打印完一行，换行

~~~



上面的代码中，`for-in`循环的循环体中又用到了`for-in`循环，外面的循环用来控制产生`i`行的输出，而里面的循环则用来控制在一行中输出`j`列。显然，里面的`for-in`循环的输出就是乘法口诀表中的一整行。所以在里面的循环完成时，我们用了一个`print()`来实现换行的效果，让下面的输出重新另起一行，最后的输出如下所示。



```
1*1=1
1*2=2   2*2=4
1*3=3   2*3=6   3*3=9
1*4=4   2*4=8   3*4=12  4*4=16
1*5=5   2*5=10  3*5=15  4*5=20  5*5=25
1*6=6   2*6=12  3*6=18  4*6=24  5*6=30  6*6=36
1*7=7   2*7=14  3*7=21  4*7=28  5*7=35  6*7=42  7*7=49
1*8=8   2*8=16  3*8=24  4*8=32  5*8=40  6*8=48  7*8=56  8*8=64
1*9=9   2*9=18  3*9=27  4*9=36  5*9=45  6*9=54  7*9=63  8*9=72  9*9=81
```



- `\t` 表示**制表符（Tab 键）**，它会在输出内容之间插入一个**水平空格（大约 4～8 个空格的宽度）**。

  - 例如：

    ```
    for i in range(1, 6):
        print(i, end='\t')
    ```

  - 输出结果是：

    ```
    1	2	3	4	5
    ```

    

- 其他常见写法举例

  | 写法       | 效果                   | 示例输出 |
  | ---------- | ---------------------- | -------- |
  | `end='\n'` | 默认换行               | 1  2  3  |
  | `end=' '`  | 用空格分隔             | 1 2 3    |
  | `end='\t'` | 用制表符分隔           | 1 2 3    |
  | `end=''`   | 连续打印不换行不加空格 | 123      |



​		

##### 5️⃣ 循环结构的应用

###### 例子1：判断素数

要求：输入一个大于 1 的正整数，判断它是不是素数。

> **提示**：素数指的是只能被 1 和自身整除的大于 1 的整数。例如对于正整数 n，我们可以通过在 2 到 n−1 之间寻找有没有 n 的因子，来判断它到底是不是一个素数。当然，循环不用从 2 开始到 n−1 结束，因为对于大于 1 的正整数，因子应该都是成对出现的，所以循环到 n 就可以结束了。

~~~python
"""
输入一个大于1的正整数判断它是不是素数

Version: 1.0
Author: 骆昊
"""
num = int(input('请输入一个正整数: '))
end = int(num ** 0.5)
is_prime = True
for i in range(2, end + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')
~~~





~~~python
"""
Version: 1.0
Author: 李小婕
Date: 2024-06-17
Description: 输入一个大于1的正整数判断它是不是素数,并打印结果。

Keyword arguments:
argument -- description
Return: return_description
"""

num = int(input("请输入一个大于1的正整数: "))
if num <= 1:
    print("输入无效，请输入一个大于1的正整数。")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} 是素数。")
    else:
        print(f"{num} 不是素数。")
# 1.输入一个大于1的正整数
# 2.判断输入的数是否小于等于1，如果是，打印无效输入
# 3.初始化一个标志变量 is_prime = True
# 4.使用for循环从2到sqrt(num)遍历可能的因子
# 5.在循环中判断 num 是否能被 i 整除，如果能，设置 is_prime = False 并跳出循环
# 6.循环结束后，根据 is_prime 的值打印结果
# 使用break跳出循环的步骤
# 使用for循环遍历可能的因子
# 使用平方根优化素数判断
~~~



```
请输入一个大于1的正整数: 2
2 是素数。
请输入一个大于1的正整数: 1
输入无效，请输入一个大于1的正整数。
请输入一个大于1的正整数: 5
5 是素数。
```

**说明**：上面的代码中我们用了布尔型的变量`is_prime`，我们先将它赋值为`True`，假设`num`是一个素数；接下来，我们在 2 到`num ** 0.5`的范围寻找`num`的因子，如果找到了`num`的因子，那么它一定不是素数，此时我们将`is_prime`赋值为`False`，同时使用`break`关键字终止循环结构；最后，我们根据`is_prime`的值是`True`还是`False`来给出不同的输出。



###### 例子2：最大公约数和最小公倍数

要求：*输入两个正整数求它们的最大公约数和最小公倍数，并输出从1到100的所有素数。*

> **提示**：
>
> - 两个数的最大公约数是两个数的公共因子中最大的那个数。
>
> - 最小公倍数是能同时被两个或多个整数整除的最小正整数



```python
"""
Version: 1.0
Author: 李小婕
Description: 输入两个正整数求它们的最大公约数,最小公倍数，并输出从1到100的所有素数。
Date: 2025-10-13

Keyword arguments:
argument -- description
Return: return_description
"""
def gcd(a, b): # 
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
```



**简单代码示例（Python）**

~~~python
import math

a, b = 12, 18
gcd = math.gcd(a, b)
lcm = a * b // gcd

print("最大公约数:", gcd)
print("最小公倍数:", lcm)
~~~

输出：

```
最大公约数: 6
最小公倍数: 36
```



🧩 **一、公约数和公倍数基本概念**

✅ 1. 最大公约数（Greatest Common Divisor, GCD）

指的是能同时整除两个或多个整数的最大整数。

**例如：**

- 12 的约数有：1, 2, 3, 4, 6, 12  
- 18 的约数有：1, 2, 3, 6, 9, 18  
  → 公共约数是：1, 2, 3, 6  
  👉 **最大公约数 GCD = 6**

---

✅ 2. 最小公倍数（Least Common Multiple, LCM）

指的是能同时被两个或多个整数整除的最小正整数。

**例如：**

- 12 的倍数：12, 24, 36, 48, 60, ...  
- 18 的倍数：18, 36, 54, 72, ...  
  → 公共倍数是：36, 72, ...  
  👉 **最小公倍数 LCM = 36**

---



**⚙️ 二、计算方法与条件**

*方法 1：列举法（基础思路）*

适合小数：

- 列出所有约数 → 找出最大公约数  
- 列出所有倍数 → 找出最小公倍数  

但效率太低。

---



*方法 2：质因数分解法*

把每个数分解成质数的乘积，然后：

- **最大公约数**：取公共质因数的最小指数次幂  
- **最小公倍数**：取所有质因数的最大指数次幂  

**例如：**

→ **最大公约数 GCD = 2¹ × 3¹ = 6**  
→ **最小公倍数 LCM = 2² × 3² = 36**

---



*方法 3：利用数学关系式*

一个非常重要的公式：

$$
a × b = GCD(a,b) × LCM(a,b)
$$

也就是说：

$$
LCM(a,b) = \frac{a × b}{GCD(a,b)}
$$

---



**📘 三、特殊情况（条件总结）**

| 条件                 | 最大公约数   | 最小公倍数   | 说明                      |
| -------------------- | ------------ | ------------ | ------------------------- |
| 两数互质（GCD=1）    | 1            | a × b        | 没有公因数                |
| 两数相等             | 该数本身     | 该数本身     | 如 (8,8) → GCD=8, LCM=8   |
| 一个数是另一个的倍数 | 较小的那个数 | 较大的那个数 | 如 (6,12) → GCD=6, LCM=12 |







###### 例子3：猜数字游戏

要求：计算机出一个 1 到 100 之间的随机数，玩家输入自己猜的数字，计算机给出对应的提示信息“大一点”、“小一点”或“猜对了”，如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。

~~~python
"""
猜数字小游戏

Version: 1.0
Author: 骆昊
"""
import random

answer = random.randrange(1, 101)
counter = 0
while True:
    counter += 1
    num = int(input('请输入: '))
    if num < answer:
        print('大一点.')
    elif num > answer:
        print('小一点.')
    else:
        print('猜对了.')
        break
print(f'你一共猜了{counter}次.')
~~~

> **说明**：上面的代码使用`import random`导入了 Python 标准库的`random`模块，该模块的`randrange`函数帮助我们生成了 1 到 100 范围的随机数（不包括 100）。变量`counter`用来记录循环执行的次数，也就是用户一共猜了几次，每循环一次`counter`的值都会加 1。



```python
"""
彩数字小游戏
Version: 1.0
Author: 李小婕
Date: 2025-10-13
Description: 猜数字小游戏，用户有三次机会猜一个1到100之间的数字。
Keyword arguments:
argument -- description
Return: return_description
"""
import random
number_to_guess = random.randint(1, 100)
attempts = 3
print("欢迎来到猜数字小游戏！你有三次机会猜一个1到100之间的数字。")
for attempt in range(attempts):
    guess = int(input(f"第{attempt + 1}次猜测: "))
    if guess < number_to_guess:
        print("太小了！")
    elif guess > number_to_guess:
        print("太大了！")
    else:
        print("恭喜你，猜对了！")
        break
else:
    print(f"很遗憾，三次机会用完了。正确的数字是 {number_to_guess}。")
```







##### ✅ 总结

学会了 Python 中的分支结构和循环结构，我们就可以解决很多实际的问题了。通过这节课的学习，大家应该已经知道了可以用`for`和`while`关键字来构造循环结构。**如果事先知道循环结构重复的次数，我们通常使用**`for`**循环**；**如果循环结构的重复次数不能确定，可以用**`while`**循环**。此外，我们可以在循环结构中**使用**`break`**终止循环**，**也可以在循环结构中使用**`continue`**关键字让循环结构直接进入下一轮次**。





#### 2.2.5 步长 step

##### 1️⃣ 例子对比

🔹**步长 = 1**

```python
for i in range(1, 11, 1):
    print(i, end=' ')
```

输出：

```
1 2 3 4 5 6 7 8 9 10
```

- 每次加 1，**遍历所有整数**。



🔹**步长 = 2**

```python
for i in range(1, 11, 2):
    print(i, end=' ')
```

输出：

```
1 3 5 7 9
```

- 每次加 2，只遍历 **奇数**（因为起始是 1）。



🔹**步长 = 2（起始为 2）**

```python
for i in range(2, 11, 2):
    print(i, end=' ')
```

输出：

```
2 4 6 8 10
```

- 每次加 2，只遍历 **偶数**（因为起始是 2）。



##### 2️⃣ 总结步长的作用

- **步长决定遍历“间隔”**，可以跳过某些数字
- 可以用步长直接 **生成奇数、偶数或等差序列**，不必在循环里再加额外判断
- 在你的例子里：
  - `range(1, 101, 2)` → 奇数序列
  - `range(2, 101, 2)` → 偶数序列



💡 **小技巧**：
 如果想求 **1~100 的偶数和**，最优写法就是：

```python
sum = 0
for i in range(2, 101, 2):
    sum += i
print(sum)
```

- 不用 `if i % 2 == 0` 判断，步长已经帮你“筛选”了偶数。





### 2.4 数据结构

#### 2.4.1 常用数据结构之列表

在开始本节课的内容之前，我们先给大家一个编程任务，将一颗色子掷`6000`次，统计每个点数出现的次数。这个任务对大家来说应该是非常简单的，我们可以用`1`到`6`均匀分布的随机数来模拟掷色子，然后用`6`个变量分别记录每个点数出现的次数，相信大家都能写出下面的代码。

~~~python
import random

f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0
for _ in range(6000):
    face = random.randint(1, 6)
    if face == 1:
        f1 += 1
    elif face == 2:
        f2 += 1
    elif face == 3:
        f3 += 1
    elif face == 4:
        f4 += 1
    elif face == 5:
        f5 += 1
    else:
        f6 += 1
print(f'1点出现了{f1}次')
print(f'2点出现了{f2}次')
print(f'3点出现了{f3}次')
print(f'4点出现了{f4}次')
print(f'5点出现了{f5}次')
print(f'6点出现了{f6}次')
~~~

看看上面的代码，相信大家一定觉得它非常的“笨重”和“丑陋”，更可怕的是，如果要统计掷两颗或者更多的色子统计每个点数出现的次数，那就需要定义更多的变量，写更多的分支结构。讲到这里，相信大家一定想问：有没有办法用一个变量来保存多个数据，有没有办法用统一的代码对多个数据进行操作？答案是肯定的，在Python中我们可以通过容器类型的变量来保存和操作多个数据，我们首先为大家介绍列表（list）这种新的数据类型。



`datastructure_sample01.py`

~~~python
"""
Version: 1.0
Author: 李小婕
Description: 常用数据结构示例，将一颗色子掷6000次，统计各个点数出现的次数。

Keyword arguments:
argument -- description
Return: return_description
"""
import random
# 初始化一个字典来存储点数出现的次数
dice_counts = {i: 0 for i in range(1, 7)} # 创建一个包含1到6点数的字典，初始值为0,举例：{1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
# 掷色子6000次
for _ in range(6):
    roll = random.randint(1, 6)  # 生成1到6之间的随机整数,举例子如: 3
    dice_counts[roll] += 1  # 对应点数的计数加1，举例子如: {1: 998, 2: 1005, 3: 1003, 4: 1002, 5: 995, 6: 997}
    print(roll, end=' ')  # 打印当前掷出的点数
    print(dice_counts)  # 打印当前所有点数的计数
    print()  # 换行
# 打印结果
for number, count in dice_counts.items():
    print(f"点数 {number} 出现的次数: {count}")
    
# 1.导入random模块
# 2.初始化字典 dice_counts = {i: 0 for i in range(1, 7)}
# 3.循环 for _ in range(6000)
# 4.生成随机数 roll = random.randint(1, 6)
# 5.更新字典 dice_counts[roll] += 1
# 6.循环结束后，打印结果 for number, count in dice_counts.items(): print(f"点数 {number} 出现的次数: {count}")
# 使用字典存储点数出现次数的步骤
# 使用random.randint生成随机数
# 使用字典的键值对存储和更新点数出现次数
# 使用for循环遍历字典并打印结果
# 使用字典推导式初始化字典
# 使用f字符串格式化输出
# 以上步骤展示了如何使用常用数据结构（字典）来统计和存储数据
# 以及如何使用循环和条件语句来处理数据。
# 这些都是Python编程中非常重要的基础知识
# 通过这个示例，读者可以更好地理解和掌握Python中的数据结构和控制流
# 以及如何将它们应用到实际问题中
# 这将有助于提高编程技能和解决问题的能力
# 希望读者能够通过这个示例，进一步探索和学习Python编程的更多内容
# 并将所学知识应用到自己的项目和工作中
# 祝大家编程愉快！
~~~



~~~python
"""
Version: 1.0
Author: 李小婕
Description: 掷多个骰子（n ≤ 6）并统计各点数出现的次数
Date: 2025-10-14

Keyword arguments:
argument -- description
Return: return_description
"""

import random
dice_counts = {i: 0 for i in range(1, 7)}
# 假设一次掷出 n 个骰子（n ≤ 6）
n = 4
rolls = [random.randint(1, 6) for _ in range(n)]  # 一次生成 n 个随机点数
print("这次掷出的点数是:", rolls) # 举例子如: [3, 5, 2, 6]

for roll in rolls:
    dice_counts[roll] += 1 
    # 更新对应点数的计数, 举例子: [3, 5, 2, 6] 中的 3 计数加 1，那么dice_counts变为 {1: 0, 2: 1, 3: 1, 4: 0, 5: 1, 6: 1}
    # dice_counts[0] += 1 # KeyError: 0
print("统计结果:", dice_counts)
~~~



```
这次掷出的点数是: [2, 1, 4, 2]
统计结果: {1: 1, 2: 2, 3: 0, 4: 1, 5: 0, 6: 0}
这次掷出的点数是: [6, 3, 6, 1]
统计结果: {1: 1, 2: 0, 3: 1, 4: 0, 5: 0, 6: 2}
```







##### 2.4.1.1 对应点数的计数加1

`dice_counts[roll] += 1` 这行确实是很多初学者第一次看到时最难理解的部分之一。
 别急，我们一层层拆开讲 👇



###### 🧩 一、背景先回顾

在你的代码中，有这几行：

```
dice_counts = {i: 0 for i in range(1, 7)} # 举例：{1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
roll = random.randint(1, 6)
dice_counts[roll] += 1
```

这三行的作用是：

1. 创建一个字典 `dice_counts`，记录每个点数出现的次数；
2. 用 `roll` 代表这次掷出的点数；
3. 让对应的点数计数加 1。



###### 🧠 二、我们逐步拆解

**第一步：理解字典是什么**

假设字典现在是这样👇

```
dice_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
```

这表示：

| 点数 | 出现次数 |
| ---- | -------- |
| 1    | 0        |
| 2    | 0        |
| 3    | 0        |
| 4    | 0        |
| 5    | 0        |
| 6    | 0        |



**第二步：假设这次掷出的点数是 4**

```
roll = 4
```

那 `dice_counts[roll]` 就等于 `dice_counts[4]`
 也就是 **访问键为 4 的值**。
 当前它是：

```
dice_counts[4] = 0
```



**第三步：看 `+= 1` 这个操作**

这行：

```
dice_counts[roll] += 1
```

等价于：

```
dice_counts[roll] = dice_counts[roll] + 1
```

也就是说：

> 取出原来的值，加 1，再放回去。



**第四步：执行结果**

执行后：

```
dice_counts[4] = 0 + 1 = 1
```

于是字典变成：

```
{1: 0, 2: 0, 3: 0, 4: 1, 5: 0, 6: 0}
```

表示：
 🎲 4 点出现了一次！





###### ✅ 三、再举个例子（多次掷）

| 第几次掷 | roll值 | 执行语句            | 更新后字典                     |
| -------- | ------ | ------------------- | ------------------------------ |
| 第1次    | 4      | dice_counts[4] += 1 | {1:0, 2:0, 3:0, 4:1, 5:0, 6:0} |
| 第2次    | 2      | dice_counts[2] += 1 | {1:0, 2:1, 3:0, 4:1, 5:0, 6:0} |
| 第3次    | 4      | dice_counts[4] += 1 | {1:0, 2:1, 3:0, 4:2, 5:0, 6:0} |

可以看到，每次掷出哪个点数，就让它的计数加 1。





###### 💡 四、总结一句话

> `dice_counts[roll] += 1`
> 意思是：**找到字典中键为 roll 的值，让它在原基础上加 1**。
> 它是“更新计数”的常见写法。



##### 2.4.1.2 定义和使用列表

在Python中，**列表是由一系元素按特定顺序构成的数据序列**，这样就意味着定义一个列表类型的变量，**可以保存多个数据**，而且**允许有重复的数据**。跟上一课我们讲到的字符串类型一样，列表也是一种结构化的、非标量类型，操作一个列表类型的变量，除了可以使用运算符还可以使用它的方法。

在Python中，可以使用`[]`字面量语法来定义列表，列表中的多个元素用逗号进行分隔，代码如下所示。

```python
items1 = [35, 12, 99, 68, 55, 87]
items2 = ['Python', 'Java', 'Go', 'Kotlin']
```



除此以外，还可以通过Python内置的`list`函数将其他序列变成列表。准确的说，`list`并不是一个普通的函数，它是创建列表对象的构造器（后面会讲到对象和构造器这两个概念）。

~~~python
items1 = list(range(1, 10))
print(items1)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
items2 = list('hello')
print(items2)    # ['h', 'e', 'l', 'l', 'o']
~~~

需要说明的是，列表是一种可变数据类型，也就是说列表可以添加元素、删除元素、更新元素，这一点跟我们上一课讲到的字符串有着鲜明的差别。字符串是一种不可变数据类型，也就是说对字符串做拼接、重复、转换大小写、修剪空格等操作的时候会产生新的字符串，原来的字符串并没有发生任何改变。



##### 2.4.1.3 列表的运算符

和字符串类型一样，列表也支持拼接、重复、成员运算、索引和切片以及比较运算，对此我们不再进行赘述，请大家参考下面的代码。

```python
items1 = [35, 12, 99, 68, 55, 87]
items2 = [45, 8, 29]

# 列表的拼接
print("--------列表的拼接---------")
print(items1 + items2)  # [35, 12, 99, 68, 55, 87, 45, 8, 29]
print(items1 * 3)       # [35, 12, 99, 68, 55, 87, 35, 12, 99, 68, 55, 87, 35, 12, 99, 68, 55, 87]
print("--------列表的拼接---------\n")

# 列表的比较
print("--------列表的比较---------")
print(items1 > items2)   # True
print(items1 < items2)   # False
print(items1 == items2)  # False
print(items1 != items2)  # True
print("--------列表的比较---------\n")

# 列表的成员资格
print("--------列表的成员资格---------")
print(35 in items1)    # True 
print(100 in items1)   # False
print(100 not in items1) # True
print("--------列表的成员资格---------\n")

# 列表的遍历
print("--------列表的遍历---------")
for item in items1:
    print(item, end=' ')
print("\n--------列表的遍历---------\n")

# 列表的长度
print("--------列表的长度---------")
print(len(items1))  # 6
print("--------列表的长度---------\n")

# 列表的最大值和最小值
print("--------列表的最大值和最小值---------")
print(max(items1))  # 99
print(min(items1))  # 12
print("--------列表的最大值和最小值---------\n")

# 列表的求和
print("--------列表的求和---------")
print(sum(items1))  # 356
print("--------列表的求和---------\n")

# 列表的排序
print("--------列表的排序---------")
print(sorted(items1))  # [12, 35, 55, 68, 87, 99]
print(sorted(items1, reverse=True))  # [99, 87, 68, 55, 35, 12]
print("--------列表的排序---------\n")

# 列表的切片
print("--------列表的切片---------")
# items1 = [35, 12, 99, 68, 55, 87]
print(items1[1:4])  # [12, 99, 68] # 取出索引1到4的元素
print(items1[:3])   # [35, 12, 99] # 取出索引0到3的元素
print(items1[3:])   # [68, 55, 87] # 取出索引3到最后的元素
print(items1[-3:])  # [68, 55, 87] # 取出最后3个元素
print(items1[:-3])  # [35, 12, 99] # 取出所有元素，直到倒数第3个元素
print(items1[::2])  # [35, 99, 55] # 取出所有偶数索引的元素
print(items1[::-1]) # [87, 55, 68, 99, 12, 35] # 取出所有元素，倒序
print("--------列表的切片---------\n")

# 列表的复制
print("--------列表的复制---------")
list_copy = items1[:]  # 列表的切片复制
print(list_copy)  # [35, 12, 99, 68, 55, 87]
list_copy2 = items1.copy()  # 列表的copy方法复制
print(list_copy2)  # [35, 12, 99, 68, 55, 87]
list_copy3 = list(items1)  # 列表的list函数复制
print(list_copy3)  # [35, 12, 99, 68, 55, 87]
print("--------列表的复制---------\n")

# 列表的嵌套
print("--------列表的嵌套---------")
nested_list = [items1, items2]
print(nested_list)  # [[35, 12, 99, 68, 55, 87], [45, 8, 29]]
print(nested_list[0])  # [35, 12, 99, 68, 55, 87]
print(nested_list[1])  # [45, 8, 29]
print(nested_list[0][2])  # 99
print("--------列表的嵌套---------\n")

# 列表的解包
print("--------列表的解包---------")
a, b, c, d, e, f = items1
print(a, b, c, d, e, f)  # 35 12 99 68 55 87
print("--------列表的解包---------\n")
# 列表的增删改查
print("--------列表的增删改查---------")
items = [1, 2, 3]
items.append(4)  # 增加元素
print(items)  # [1, 2, 3, 4]
items.insert(1, 1.5)  # 插入元素
print(items)  # [1, 1.5, 2, 3, 4]
items.remove(1.5)  # 删除元素
print(items)  # [1, 2, 3, 4]
items[2] = 99  # 修改元素
print(items)  # [1, 2, 99, 4]
print(items.index(99))  # 查找元素索引，输出2
print(items.count(2))  # 统计元素出现次数，输出1
items.sort()  # 列表排序
print(items)  # [1, 2, 4, 99]
items.reverse()  # 列表反转
print(items)  # [99, 4, 2, 1]
print("--------列表的增删改查---------\n")
# 列表的清空
print("--------列表的清空---------")
items.clear()  # 清空列表
print(items)  # []
print("--------列表的清空---------\n")
# 列表的复制
print("--------列表的复制---------")
# 列表的合并
print("--------列表的合并---------")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)  # 合并列表
print(list1)  # [1, 2, 3, 4, 5, 6]
print
```

值得一提的是，由于列表是可变类型，所以通过索引操作既可以获取列表中的元素，也可以更新列表中的元素。对列表做索引操作一样要注意索引越界的问题，对于有`N`个元素的列表，正向索引的范围是`0`到`N-1`，负向索引的范围是`-1`到`-N`，如果超出这个范围，将引发`IndexError`异常，错误信息为：`list index out of range`。



##### 2.4.1.4 列表元素的遍历

如果想逐个取出列表中的元素，可以使用`for`循环的，有以下两种做法。

**方法一：**

~~~python
items = ['Python', 'Java', 'Go', 'Kotlin']

for index in range(len(items)):
    print(index, items[index])
~~~

输出结果：

```
0 Python
1 Java
2 Go
3 Kotlin
```



**方法二：**

~~~python
items = ['Python', 'Java', 'Go', 'Kotlin']

for item in items:
    print(item)
~~~

输出结果：

```
Python
Java
Go
Kotlin
```



##### 2.4.1.5 列表的方法

在Python中，列表还可以通过一种特殊的字面量语法来创建，这种语法叫做生成式。我们给出两段代码，大家可以做一个对比，看看哪一种方式更加简单优雅。

通过`for`循环为空列表添加元素。

~~~python
# 创建一个由1到9的数字构成的列表
items1 = []
for x in range(1, 10):
    items1.append(x)
print(items1)

# 创建一个由'hello world'中除空格和元音字母外的字符构成的列表
items2 = []
for x in 'hello world':
    if x not in ' aeiou':
        items2.append(x)
print(items2)

# 创建一个由个两个字符串中字符的笛卡尔积构成的列表
items3 = []
for x in 'ABC':
    for y in '12':
        items3.append(x + y)
print(items3)
~~~



通过生成式创建列表

```python
# 创建一个由1到9的数字构成的列表
items1 = [x for x in range(1, 10)]
print(items1)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 创建一个由'hello world'中除空格和元音字母外的字符构成的列表
items2 = [x for x in 'hello world' if x not in ' aeiou']
print(items2)    # ['h', 'l', 'l', 'w', 'r', 'l', 'd']

# 创建一个由个两个字符串中字符的笛卡尔积构成的列表
items3 = [x + y for x in 'ABC' for y in '12']
print(items3)    # ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
```



下面这种方式不仅代码简单优雅，而且性能也优于上面使用`for`循环和`append`方法向空列表中追加元素的方式。可以简单跟大家交待下为什么生成式拥有更好的性能，那是因为Python解释器的字节码指令中有专门针对生成式的指令（`LIST_APPEND`指令）；而`for`循环是通过方法调用（`LOAD_METHOD`和`CALL_METHOD`指令）的方式为列表添加元素，方法调用本身就是一个相对耗时的操作。对这一点不理解也没有关系，记住“**强烈建议用生成式语法来创建列表**”这个结论就可以了。



##### 2.4.1.6 嵌套的列表

Python语言没有限定列表中的元素必须是相同的数据类型，也就是说一个列表中的元素可以任意的数据类型，当然也包括列表。如果列表中的元素又是列表，那么我们可以称之为嵌套的列表。嵌套的列表可以用来表示表格或数学上的矩阵，例如：我们想保存5个学生3门课程的成绩，可以定义一个保存5个元素的列表保存5个学生的信息，而每个列表元素又是3个元素构成的列表，分别代表3门课程的成绩。但是，一定要注意下面的代码是有问题的。

```
scores = [[0] * 3] * 5
print(scores)    # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
```



看上去我们好像创建了一个`5 * 3`的嵌套列表，但实际上当我们录入第一个学生的第一门成绩后，你就会发现问题来了，我们看看下面代码的输出。

```
# 嵌套的列表需要多次索引操作才能获取元素
scores[0][0] = 95
print(scores)
# [[95, 0, 0], [95, 0, 0], [95, 0, 0], [95, 0, 0], [95, 0, 0]]
```



我们不去过多的解释为什么会出现这样的问题，如果想深入研究这个问题，可以通过[Python Tutor](http://www.pythontutor.com/visualize.html)网站的可视化代码执行功能，看看创建列表时计算机内存中发生了怎样的变化，下面的图就是在这个网站上生成的。建议大家不去纠结这个问题，现阶段只需要记住不能用`[[0] * 3] * 5]`这种方式来创建嵌套列表就行了。那么创建嵌套列表的正确做法是什么呢，下面的代码会给你答案。

```
scores = [[0] * 3 for _ in range(5)]
scores[0][0] = 95
print(scores)
# [[95, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
```



##### 2.4.1.7 简单的总结

Python中的列表底层是一个可以动态扩容的数组，列表元素在内存中也是连续存储的，所以可以实现随机访问（通过一个有效的索引获取到对应的元素且操作时间与列表元素个数无关）。我们暂时不去触碰这些底层存储细节以及列表每个方法的渐近时间复杂度（执行这个方法耗费的时间跟列表元素个数的关系），等需要的时候再告诉大家。现阶段，大家只需要知道**列表是容器**，可以**保存各种类型的数据**，**可以通过索引操作列表元素**，知道这些就足够了。



#### 2.4.2 常用数据结构之元组

上一节课为大家讲解了Python中的列表，它是一种容器型数据类型，我们可以通过定义列表类型的变量来保存和操作多个元素。当然，Python中容器型的数据类型肯定不止列表一种，接下来我们为大家讲解另一种重要的容器型数据类型，它的名字叫元组（tuple）。

##### 2.4.2.1 定义和使用元组

在Python中，元组也是多个元素按照一定的顺序构成的序列。`元组和列表的不同之处在于，元组是不可变类型`，这就意味着元组类型的变量一旦定义，其中的元素不能再添加或删除，而且元素的值也不能进行修改。定义元组通常使用`()`字面量语法，也建议大家使用这种方式来创建元组。元组类型支持的运算符跟列表是一样。下面的代码演示了元组的定义和运算

~~~python
# 定义一个三元组
t1 = (30, 10, 55)
# 定义一个四元组
t2 = ('骆昊', 40, True, '四川成都')

# 查看变量的类型
print(type(t1), type(t2))    # <class 'tuple'> <class 'tuple'>
# 查看元组中元素的数量
print(len(t1), len(t2))      # 3 4

# 通过索引运算获取元组中的元素
print(t1[0], t1[-3])         # 30 30
print(t2[3], t2[-1])         # 四川成都 四川成都

# 循环遍历元组中的元素
for member in t2:
    print(member)

# 成员运算
print(100 in t1)    # False
print(40 in t2)     # True

# 拼接
t3 = t1 + t2
print(t3)           # (30, 10, 55, '骆昊', 40, True, '四川成都')

# 切片
print(t3[::3])      # (30, '骆昊', '四川成都')

# 比较运算
print(t1 == t3)    # False
print(t1 >= t3)    # False
print(t1 < (30, 11, 55))    # True
~~~



一个元组中如果有两个元素，我们就称之为二元组；一个元组中如果五个元素，我们就称之为五元组。需要提醒大家注意的是，`()`表示空元组，但是如果元组中只有一个元素，需要加上一个逗号，否则`()`就不是代表元组的字面量语法，而是改变运算优先级的圆括号，所以`('hello', )`和`(100, )`才是一元组，而`('hello')`和`(100)`只是字符串和整数。我们可以通过下面的代码来加以验证。

```python
# 空元组
a = ()
print(type(a))    # <class 'tuple'>
# 不是元组
b = ('hello')
print(type(b))    # <class 'str'>, 单元素元组（必须加逗号）
c = (100)
print(type(c))    # <class 'int'>
# 一元组
d = ('hello', )
print(type(d))    # <class 'tuple'>
e = (100, )
print(type(e))    # <class 'tuple'>
```



**正确的单元素元组定义**

要创建只有一个元素的元组，必须在元素后面加一个**逗号**：

```python
# 错误的方式
b1 = ('hello')
print(type(b1))   # <class 'str'>

# 正确的方式
b2 = ('hello',)   # 注意这里的逗号！
print(type(b2))   # <class 'tuple'>
print(b2)         # ('hello',)
```



**各种情况的对比**

```python
# 空元组
empty_tuple = ()
print(type(empty_tuple))  # <class 'tuple'>

# 单元素元组（必须加逗号）
single_tuple = ('hello',)
print(type(single_tuple))  # <class 'tuple'>

# 多元素元组（逗号分隔）
multi_tuple = ('hello', 'world')
print(type(multi_tuple))   # <class 'tuple'>

# 没有逗号 - 就是普通字符串
not_tuple = ('hello')
print(type(not_tuple))     # <class 'str'>
```



**甚至可以省略括号**

```python
# 这些也都是元组
tuple1 = 'hello',
tuple2 = 1, 2, 3
tuple3 = 'a', 'b', 'c'

print(type(tuple1))  # <class 'tuple'>
print(type(tuple2))  # <class 'tuple'>
print(type(tuple3))  # <class 'tuple'>
```





##### 2.4.2.2 元组的应用场景

讲到这里，相信大家一定迫切的想知道元组有哪些应用场景，我们给大家举几个例子。

###### 1️⃣ 例子1：打包和解包操作。

当我们把多个用逗号分隔的值赋给一个变量时，多个值会打包成一个元组类型；当我们把一个元组赋值给多个变量时，元组会解包成多个值然后分别赋给对应的变量，如下面的代码所示。

```python
# 打包
a = 1, 10, 100
print(type(a), a)    # <class 'tuple'> (1, 10, 100)
# 解包
i, j, k = a
print(i, j, k)       # 1 10 100
```





在解包时，如果解包出来的元素个数和变量个数不对应，会引发`ValueError`异常，错误信息为：`too many values to unpack`（解包的值太多）或`not enough values to unpack`（解包的值不足）。

```python
a = 1, 10, 100, 1000
# i, j, k = a             # ValueError: too many values to unpack (expected 3)
# i, j, k, l, m, n = a    # ValueError: not enough values to unpack (expected 6, got 4)
```



有一种解决变量个数少于元素的个数方法，就是使用星号表达式，我们之前讲函数的可变参数时使用过星号表达式。有了星号表达式，我们就可以让一个变量接收多个值，代码如下所示。需要注意的是，用星号表达式修饰的变量会变成一个列表，列表中有0个或多个元素。还有在解包语法中，星号表达式只能出现一次。

```python
a = 1, 10, 100, 1000
i, j, *k = a
print(i, j, k)          # 1 10 [100, 1000]
i, *j, k = a
print(i, j, k)          # 1 [10, 100] 1000
*i, j, k = a
print(i, j, k)          # [1, 10] 100 1000
*i, j = a
print(i, j)             # [1, 10, 100] 1000
i, *j = a
print(i, j)             # 1 [10, 100, 1000]
i, j, k, *l = a
print(i, j, k, l)       # 1 10 100 [1000]
i, j, k, l, *m = a
print(i, j, k, l, m)    # 1 10 100 1000 []
```



需要说明一点，解包语法对所有的序列都成立，这就意味着对列表以及我们之前讲到的`range`函数返回的范围序列都可以使用解包语法。大家可以尝试运行下面的代码，看看会出现怎样的结果。

```python
a, b, *c = range(1, 10)
print(a, b, c)
a, b, c = [1, 10, 100]
print(a, b, c)
a, *b, c = 'hello'
print(a, b, c)
```





###### 2️⃣ 例子2：交换两个变量的值。

交换两个变量的值是编程语言中的一个经典案例，在很多编程语言中，交换两个变量的值都需要借助一个中间变量才能做到，如果不用中间变量就需要使用比较晦涩的位运算来实现。在Python中，交换两个变量`a`和`b`的值只需要使用如下所示的代码。

```
a, b = b, a
```



同理，如果要将三个变量`a`、`b`、`c`的值互换，即`b`赋给`a`，`c`赋给`b`，`a`赋给`c`，也可以如法炮制。

```
a, b, c = b, c, a
```

需要说明的是，上面并没有用到打包和解包语法，Python的字节码指令中有`ROT_TWO`和`ROT_THREE`这样的指令可以实现这个操作，效率是非常高的。但是如果有多于三个变量的值要依次互换，这个时候没有直接可用的字节码指令，执行的原理就是我们上面讲解的打包和解包操作。



###### 3️⃣ 例子3：实际应用

```python
# 在函数返回多个值时
def get_user():
    return 'Alice', 25  # 自动打包成元组

name, age = get_user()  # 元组解包

# 在需要不可变数据时
CONFIG = ('localhost', 8080,)  # 明确的单元素元组
```



##### 2.4.2.3 元组和列表的比较

1. 元组是不可变类型，**不可变类型更适合多线程环境**，因为它降低了并发访问变量的同步化开销。关于这一点，我们会在后面讲解多线程的时候为大家详细论述。

2. 元组是不可变类型，通常**不可变类型在创建时间和占用空间上面都优于对应的可变类型**。我们可以使用`sys`模块的`getsizeof`函数来检查保存相同元素的元组和列表各自占用了多少内存空间。我们也可以使用`timeit`模块的`timeit`函数来看看创建保存相同元素的元组和列表各自花费的时间，代码如下所示。

   ```python
   # 通常元组比列表更节省内存
   a = list(range(100000))
   b = tuple(range(100000))
   
   print(f"列表占用内存: {sys.getsizeof(a)} 字节") # 800056 
   print(f"元组占用内存: {sys.getsizeof(b)} 字节") # 800040
   print(f"元组比列表节省: {sys.getsizeof(a) - sys.getsizeof(b)} 字节")
   
   print(timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]'))
   print(timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)'))
   ```

   ```python
   import timeit
   
   # 创建测试数据
   a = list(range(100000))
   b = tuple(range(100000))
   
   # 比较性能（执行50次）
   list_time = timeit.timeit('list(range(10000))', number=50)
   tuple_time = timeit.timeit('tuple(range(10000))', number=50)
   
   print(f"列表创建时间（50次总时间）: {list_time:.6f} 秒")
   print(f"元组创建时间（50次总时间）: {tuple_time:.6f} 秒")
   print(f"列表平均每次: {list_time/50:.6f} 秒")
   print(f"元组平均每次: {tuple_time/50:.6f} 秒")
   ```

   

   **不同 number 值的对比**

   ~~~python
   import timeit
   
   code_to_test = 'list(range(1000))'
   
   # 不同执行次数的比较
   times = [1, 10, 50, 100, 1000]
   
   for n in times:
       total_time = timeit.timeit(code_to_test, number=n)
       avg_time = total_time / n
       print(f"执行{n:4d}次 - 总时间: {total_time:.6f}秒, 平均: {avg_time:.6f}秒")
   ~~~

   - 代码含义

     ```
     code_to_test = 'list(range(1000))'
     ```

   - 这行代码的意思是：

     - `range(1000)` 生成 0 到 999 的数字序列（1000个数字）
     - `list()` 将这个序列转换为列表
     - 结果是：`[0, 1, 2, 3, ..., 999]`

   - 与 timeit 的 number 参数区分

     ```python
     import timeit
     
     # 这里的 1000 是列表元素个数
     code_to_test = 'list(range(1000))'
     
     # 这里的 1000 是循环执行次数
     result = timeit.timeit(code_to_test, number=1000)
     ```

     

   

   - **执行过程**：
     1. 代码 `list(range(1000))` 会执行 **1000次**（由 `number=1000` 决定）
     2. 每次执行都会创建一个包含 **1000个元素** 的列表

   ~~~python
   import timeit
   
   # 测试不同规模的列表创建
   sizes = [100, 1000, 10000]
   iterations = 100
   
   for size in sizes:
       code = f'list(range({size}))'  # 创建包含size个元素的列表
       time_taken = timeit.timeit(code, number=iterations)
       print(f"创建{size:5d}个元素的列表，执行{iterations}次，总时间: {time_taken:.4f}秒")
   ~~~

   输出类似：

   ```
   创建  100个元素的列表，执行100次，总时间: 0.0012秒
   创建 1000个元素的列表，执行100次，总时间: 0.0085秒  
   创建10000个元素的列表，执行100次，总时间: 0.0750秒
   ```

   

   

   **更清晰的例子**

   ~~~python
   import timeit
   
   # 明确变量名，避免混淆
   elements_count = 1000    # 列表中的元素个数
   execution_times = 1000   # 代码执行的次数
   
   # 创建包含1000个元素的列表，重复执行1000次
   code = f'list(range({elements_count}))'
   total_time = timeit.timeit(code, number=execution_times)
   
   print(f"创建{elements_count}个元素的列表")
   print(f"重复执行{execution_times}次")
   print(f"总耗时: {total_time:.4f}秒")
   print(f"平均每次: {total_time/execution_times:.6f}秒")
   ~~~

   

   

   

3. Python中的元组和列表是可以相互转换的，我们可以通过下面的代码来做到。

   ```python
   # 将元组转换成列表
   info = ('骆昊', 175, True, '四川成都')
   print(list(info))       # ['骆昊', 175, True, '四川成都']
   # 将列表转换成元组
   fruits = ['apple', 'banana', 'orange']
   print(tuple(fruits))    # ('apple', 'banana', 'orange')
   ```

   





##### 2.4.2.4 简单总结

**列表和元组都是容器型的数据类型**，即一个变量可以保存多个数据。**列表是可变数据类型**，**元组是不可变数据类型**，所以列表添加元素、删除元素、清空、排序等方法对于元组来说是不成立的。但是列表和元组都可以进行**拼接**、**成员运算**、**索引和切片**这些操作，后面我们要讲到的字符串类型也是这样，因为字符串就是字符按一定顺序构成的序列，在这一点上三者并没有什么区别。我们**推荐大家使用列表的生成式语法来创建列表**，它很好用，也是Python中非常有特色的语法。





#### 2.4.3 常用数据结构之字符串

第二次世界大战促使了现代电子计算机的诞生，世界上的第一台通用电子计算机叫ENIAC（电子数值积分计算机），诞生于美国的宾夕法尼亚大学，占地167平米，重量27吨，每秒钟大约能够完成约5000次浮点运算，如下图所示。ENIAC诞生之后被应用于导弹弹道的计算，而数值计算也是现代电子计算机最为重要的一项功能。

![image-20251015081553710](C:\Users\86181\AppData\Roaming\Typora\typora-user-images\image-20251015081553710.png)







随着时间的推移，虽然数值运算仍然是计算机日常工作中最为重要的组成部分，但是今天的计算机还要处理大量的以文本形式存在的信息。如果我们希望通过Python程序来操作本这些文本信息，就必须要先了解字符串这种数据类型以及与它相关的知识。



##### 2.4.3.1 字符串的定义

所谓**字符串**，就是**由零个或多个字符组成的有限序列**，一般记为：
$$
S = (a_1, a_2, \cdots, a_n),\quad 0 \leq n \leq \infty
$$

在Python程序中，如果我们把单个或多个字符用单引号或者双引号包围起来，就可以表示一个字符串。字符串中的字符可以是特殊符号、英文字母、中文字符、日文的平假名或片假名、希腊字母、[Emoji字符](http://www.ruanyifeng.com/blog/2017/04/emoji.html)等。

```python
s1 = 'hello, world!'
s2 = "你好，世界！"
print(s1, s2)
# 以三个双引号或单引号开头的字符串可以折行
s3 = '''
hello, 
world!
'''
print(s3, end='')
```

> **提示**：`print`函数中的`end=''`表示输出后不换行，即将默认的结束符`\n`（换行符）更换为`''`（空字符）。



##### 2.4.3.2 转义字符和原始字符串

可以在字符串中使用`\`（反斜杠）来表示转义，也就是说`\`后面的字符不再是它原来的意义，例如：`\n`不是代表反斜杠和字符`n`，而是表示换行；`\t`也不是代表反斜杠和字符`t`，而是表示制表符。所以如果字符串本身又包含了`'`、`"`、`\`这些特殊的字符，必须要通过`\`进行转义处理。例如要输出一个带单引号或反斜杠的字符串，需要用如下所示的方法。

```
s1 = '\'hello, world!\''
print(s1)
s2 = '\\hello, world!\\'
print(s2)
```



Python中的字符串可以`r`或`R`开头，这种字符串被称为原始字符串，意思是字符串中的每个字符都是它本来的含义，没有所谓的转义字符。例如，在字符串`'hello\n'`中，`\n`表示换行；而在`r'hello\n'`中，`\n`不再表示换行，就是反斜杠和字符`n`。大家可以运行下面的代码，看看会输出什么。

```python
s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'

print("s1:", s1)  # abcabc
print("s2:", s2)  # 骆昊

# 验证每个转义字符
print("\141 ->", '\141')  # a
print("\142 ->", '\142')  # b  
print("\143 ->", '\143')  # c
print("\x61 ->", '\x61')  # a
print("\x62 ->", '\x62')  # b
print("\x63 ->", '\x63')  # c
print("\u9a86 ->", '\u9a86')  # 骆
print("\u660a ->", '\u660a')  # 昊
```



**Python 中的转义序列类型**

| 转义类型 | 语法         | 示例         | 结果   |
| :------- | :----------- | :----------- | :----- |
| 八进制   | `\ooo`       | `\141`       | `'a'`  |
| 十六进制 | `\xhh`       | `\x61`       | `'a'`  |
| Unicode  | `\uhhhh`     | `\u9a86`     | `'骆'` |
| Unicode  | `\Uhhhhhhhh` | `\U0001F600` | `'😀'`  |



**实际应用场景**

~~~python
# 当无法直接输入某些字符时使用
# 1. 特殊ASCII字符
bell = '\007'  # 响铃字符
tab = '\011'   # 制表符

# 2. 非英文字符
chinese = '\u4e2d\u6587'  # "中文"
emoji = '\U0001F604'      # "😄"

# 3. 文件路径中的特殊字符
path = 'C:\Users\name\file.txt'  # 错误！\n会被解释为换行
path = 'C:\\Users\\name\\file.txt'  # 正确，使用转义
path = r'C:\Users\name\file.txt'   # 正确，使用原始字符串
~~~





##### 2.4.3.3 字符串的运算

Python为字符串类型提供了非常丰富的运算符，我们可以使用`+`运算符来实现字符串的拼接，可以使用`*`运算符来重复一个字符串的内容，可以使用`in`和`not in`来判断一个字符串是否包含另外一个字符串，我们也可以用`[]`和`[:]`运算符从字符串取出某个字符或某些字符。



###### 1️⃣ **拼接和重复**

下面的例子演示了使用`+`和`*`运算符来实现字符串的拼接和重复操作。

```python
s1 = 'hello' + ' ' + 'world'
print(s1)    # hello world
s2 = '!' * 3
print(s2)    # !!!
s1 += s2     # s1 = s1 + s2
print(s1)    # hello world!!!
s1 *= 2      # s1 = s1 * 2
print(s1)    # hello world!!!hello world!!!
```

用`*`实现字符串的重复是非常有意思的一个运算符，在很多编程语言中，要表示一个有10个`a`的字符串，你只能写成`"aaaaaaaaaa"`，但是在Python中，你可以写成`'a' * 10`。你可能觉得`"aaaaaaaaaa"`这种写法也没有什么不方便的，那么想一想，如果字符`a`要重复100次或者1000次又会如何呢？



###### 2️⃣ **比较运算**

对于两个字符串类型的变量，可以直接使用比较运算符比较两个字符串的相等性或大小。需要说明的是，因为字符串在计算机内存中也是以二进制形式存在的，那么字符串的大小比较比的是每个字符对应的编码的大小。例如`A`的编码是`65`， 而`a`的编码是`97`，所以`'A' < 'a'`的结果相当于就是`65 < 97`的结果，很显然是`True`；而`'boy' < 'bad'`，因为第一个字符都是`'b'`比不出大小，所以实际比较的是第二个字符的大小，显然`'o' < 'a'`的结果是`False`，所以`'boy' < 'bad'`的结果也是`False`。如果不清楚两个字符对应的编码到底是多少，可以使用`ord`函数来获得，例如`ord('A')`的值是`65`，而`ord('昊')`的值是`26122`。下面的代码为大家展示了字符串的比较运算。

~~~python
s1 = 'a whole new world'
s2 = 'hello world'
print(s1 == s2, s1 < s2)      # False True
print(s2 == 'hello world')    # True
print(s2 == 'Hello world')    # False
print(s2 != 'Hello world')    # True
s3 = '骆昊'
print(ord('骆'), ord('昊'))               # 39558 26122
s4 = '王大锤'
print(ord('王'), ord('大'), ord('锤'))    # 29579 22823 38180
print(s3 > s4, s3 <= s4)      # True False
~~~



需要强调一下的是，字符串的比较运算比较的是字符串的内容，Python中还有一个`is`运算符（身份运算符），如果用`is`来比较两个字符串，它比较的是两个变量对应的字符串对象的内存地址（不理解先跳过），简单的说就是两个变量是否对应内存中的同一个字符串。看看下面的代码就比较清楚`is`运算符的作用了。

~~~python
s1 = 'hello world'
s2 = 'hello world'
s3 = s2
# 比较字符串的内容
print(s1 == s2, s2 == s3)    # True True
# 比较字符串的内存地址
print(s1 is s2, s2 is s3)    # False True
~~~



###### 3️⃣ **成员运算**

Python中可以用`in`和`not in`判断一个字符串中是否存在另外一个字符或字符串，`in`和`not in`运算通常称为成员运算，会产生布尔值`True`或`False`，代码如下所示。

~~~python
s1 = 'hello, world'
print('wo' in s1)    # True
s2 = 'goodbye'
print(s2 in s1)      # False
~~~



4️⃣ **获取字符串长度**

获取字符串长度没有直接的运算符，而是使用内置函数`len`，我们在上节课的提到过这个内置函数，代码如下所示。

~~~py
s = 'hello, world'
print(len(s))                   # 12
print(len('goodbye, world'))    # 14
~~~



5️⃣ **索引和切片**

如果希望从字符串中取出某个字符，我们可以对字符串进行索引运算，运算符是`[n]`，其中`n`是一个整数，假设字符串的长度为`N`，那么`n`可以是从`0`到`N-1`的整数，其中`0`是字符串中第一个字符的索引，而`N-1`是字符串中最后一个字符的索引，通常称之为正向索引；在Python中，字符串的索引也可以是从`-1`到`-N`的整数，其中`-1`是最后一个字符的索引，而`-N`则是第一个字符的索引，通常称之为负向索引。注意，因为**字符串是不可变类型**，所以**不能通过索引运算修改字符串中的字符**。

~~~python
s = 'abc123456'
N = len(s)

# 获取第一个字符
print(s[0], s[-N])    # a a

# 获取最后一个字符
print(s[N-1], s[-1])  # 6 6

# 获取索引为2或-7的字符
print(s[2], s[-7])    # c c

# 获取索引为5和-4的字符
print(s[5], s[-4])    # 3 3
~~~

> 需要提醒大家注意的是，在进行索引操作时，如果索引越界（正向索引不在`0`到`N-1`范围，负向索引不在`-1`到`-N`范围），会引发`IndexError`异常，错误提示信息为：`string index out of range`（字符串索引超出范围）



如果要从字符串中取出多个字符，我们可以对字符串进行切片，运算符是`[i:j:k]`，其中`i`是开始索引，索引对应的字符可以取到；`j`是结束索引，索引对应的字符不能取到；`k`是步长，默认值为`1`，表示从前向后获取相邻字符的连续切片，所以`:k`部分可以省略。假设字符串的长度为`N`，当`k > 0`时表示正向切片（从前向后获取字符），如果没有给出`i`和`j`的值，则`i`的默认值是`0`，`j`的默认值是`N`；当`k < 0`时表示负向切片（从后向前获取字符），如果没有给出`i`和`j`的值，则`i`的默认值是`-1`，j的默认值是`-N - 1`。如果不理解，直接看下面的例子，记住第一个字符的索引是`0`或`-N`，最后一个字符的索引是`N-1`或`-1`就行了.

~~~python
s = 'abc123456'

# i=2, j=5, k=1的正向切片操作
print(s[2:5])       # c12

# i=-7, j=-4, k=1的正向切片操作
print(s[-7:-4])     # c12

# i=2, j=9, k=1的正向切片操作
print(s[2:])        # c123456

# i=-7, j=9, k=1的正向切片操作
print(s[-7:])       # c123456

# i=2, j=9, k=2的正向切片操作
print(s[2::2])      # c246

# i=-7, j=9, k=2的正向切片操作
print(s[-7::2])     # c246

# i=0, j=9, k=2的正向切片操作
print(s[::2])       # ac246

# i=1, j=-1, k=2的正向切片操作
print(s[1:-1:2])    # b135

# i=7, j=1, k=-1的负向切片操作
print(s[7:1:-1])    # 54321c

# i=-2, j=-8, k=-1的负向切片操作
print(s[-2:-8:-1])  # 54321c

# i=7, j=-10, k=-1的负向切片操作
print(s[7::-1])     # 54321cba

# i=-1, j=1, k=-1的负向切片操作
print(s[:1:-1])     # 654321c

# i=0, j=9, k=1的正向切片
print(s[:])         # abc123456

# i=0, j=9, k=2的正向切片
print(s[::2])       # ac246

# i=-1, j=-10, k=-1的负向切片
print(s[::-1])      # 654321cba

# i=-1, j=-10, k=-2的负向切片
print(s[::-2])      # 642ca
~~~



- 字符串索引图示

  ```
  字符串:    a   b   c   1   2   3   4   5   6
  正向索引:  0   1   2   3   4   5   6   7   8
  反向索引: -9  -8  -7  -6  -5  -4  -3  -2  -1
  ```

  

- 正向索引取值（从左到右）

  | 索引 | 字符 | 代码示例 | 结果  |
  | :--- | :--- | :------- | :---- |
  | 0    | a    | `s[0]`   | `'a'` |
  | 1    | b    | `s[1]`   | `'b'` |
  | 2    | c    | `s[2]`   | `'c'` |
  | 3    | 1    | `s[3]`   | `'1'` |
  | 4    | 2    | `s[4]`   | `'2'` |
  | 5    | 3    | `s[5]`   | `'3'` |
  | 6    | 4    | `s[6]`   | `'4'` |
  | 7    | 5    | `s[7]`   | `'5'` |
  | 8    | 6    | `s[8]`   | `'6'` |



- 反向索引取值（从右到左）

  | 索引 | 字符 | 代码示例 | 结果  |
  | :--- | :--- | :------- | :---- |
  | -1   | 6    | `s[-1]`  | `'6'` |
  | -2   | 5    | `s[-2]`  | `'5'` |
  | -3   | 4    | `s[-3]`  | `'4'` |
  | -4   | 3    | `s[-4]`  | `'3'` |
  | -5   | 2    | `s[-5]`  | `'2'` |
  | -6   | 1    | `s[-6]`  | `'1'` |
  | -7   | c    | `s[-7]`  | `'c'` |
  | -8   | b    | `s[-8]`  | `'b'` |
  | -9   | a    | `s[-9]`  | `'a'` |



- 验证代码

  ```python
  s = 'abc123456'
  
  print("=== 正向索引 ===")
  for i in range(len(s)):
      print(f"s[{i}] = '{s[i]}'")
  
  print("\n=== 反向索引 ===")
  for i in range(-1, -len(s)-1, -1):
      print(f"s[{i}] = '{s[i]}'")
  
  print("\n=== 同时显示 ===")
  print("字符: ", end="")
  for char in s:
      print(f"  {char}  ", end="")
  print()
  
  print("正向: ", end="")
  for i in range(len(s)):
      print(f"  {i}  ", end="")
  print()
  
  print("反向: ", end="")
  for i in range(-1, -len(s)-1, -1):
      print(f" {i} ", end="")
  print()
  ```

  输出结果：

  ```
  === 正向索引 ===
  s[0] = 'a'
  s[1] = 'b'
  s[2] = 'c'
  s[3] = '1'
  s[4] = '2'
  s[5] = '3'
  s[6] = '4'
  s[7] = '5'
  s[8] = '6'
  
  === 反向索引 ===
  s[-1] = '6'
  s[-2] = '5'
  s[-3] = '4'
  s[-4] = '3'
  s[-5] = '2'
  s[-6] = '1'
  s[-7] = 'c'
  s[-8] = 'b'
  s[-9] = 'a'
  
  === 同时显示 ===
  字符:   a    b    c    1    2    3    4    5    6
  正向:   0    1    2    3    4    5    6    7    8
  反向:  -1  -2  -3  -4  -5  -6  -7  -8  -9
  ```

- 切片操作示例

  ```python
  s = 'abc123456'
  
  # 正向切片
  print(s[0:3])    # 'abc'     - 索引0到2
  print(s[3:6])    # '123'     - 索引3到5
  print(s[6:9])    # '456'     - 索引6到8
  
  # 反向切片
  print(s[-9:-6])  # 'abc'     - 索引-9到-7
  print(s[-6:-3])  # '123'     - 索引-6到-4
  print(s[-3:])    # '456'     - 索引-3到最后
  
  # 混合索引
  print(s[0:-6])   # 'abc'     - 索引0到-7
  print(s[-9:3])   # 'abc'     - 索引-9到2
  ```

  

- 实用技巧

  ```python
  s = 'abc123456'
  
  # 获取最后一个字符
  print(s[-1])     # '6'
  
  # 获取最后三个字符
  print(s[-3:])    # '456'
  
  # 排除最后三个字符
  print(s[:-3])    # 'abc123'
  
  # 反转字符串
  print(s[::-1])   # '654321cba'
  
  # 隔一个取一个
  print(s[::2])    # 'ac246'
  ```

  

- 总结

  - **正向索引**：从 `0` 到 `len(s)-1`（从左到右）

  - **反向索引**：从 `-1` 到 `-len(s)`（从右到左）

  - 字符串 `'abc123456'` 的长度是 9

  - 正向索引范围：0 到 8

  - 反向索引范围：-1 到 -9



##### 2.4.3.4 循环遍历每个字符

如果希望从字符串中取出每个字符，可以使用`for`循环对字符串进行遍历，有两种方式。

###### 1️⃣ 方式一：

```python
s1 = 'hello'
for index in range(len(s1)):
    print(s1[index])
```



###### 2️⃣ 方式二：

```python
s1 = 'hello'
for ch in s1:
    print(ch)
```





##### 2.4.3.5 字符串的方法

在Python中，我们可以通过字符串类型自带的方法对字符串进行操作和处理，对于一个字符串类型的变量，我们可以用`变量名.方法名()`的方式来调用它的方法。所谓方法其实就是跟某个类型的变量绑定的函数，后面我们讲面向对象编程的时候还会对这一概念详加说明。



###### 1️⃣ **大小写相关操作**

下面的代码演示了和字符串大小写变换相关的方法。

```python
s1 = 'hello, world!'

# 使用capitalize方法获得字符串首字母大写后的字符串
print(s1.capitalize())   # Hello, world!

# 使用title方法获得字符串每个单词首字母大写后的字符串
print(s1.title())        # Hello, World!

# 使用upper方法获得字符串大写后的字符串
print(s1.upper())        # HELLO, WORLD!

s2 = 'GOODBYE'
# 使用lower方法获得字符串小写后的字符串
print(s2.lower())        # goodbye
```





###### 2️⃣ **查找操作**

如果想在一个字符串中从前向后查找有没有另外一个字符串，可以使用字符串的`find`或`index`方法。

```python
s = 'hello, world!'

# find方法从字符串中查找另一个字符串所在的位置
# 找到了返回字符串中另一个字符串首字符的索引
print(s.find('or'))        # 8

# 找不到返回-1
print(s.find('shit'))      # -1

# index方法与find方法类似
# 找到了返回字符串中另一个字符串首字符的索引
print(s.index('or'))       # 8

# 找不到引发异常
print(s.index('shit'))     # ValueError: substring not found
```



在使用`find`和`index`方法时还可以通过方法的参数来指定查找的范围，也就是查找不必从索引为`0`的位置开始。`find`和`index`方法还有逆向查找（从后向前查找）的版本，分别是`rfind`和`rindex`，代码如下所示。

~~~python
s = 'hello good world!'

# 从前向后查找字符o出现的位置(相当于第一次出现)
print(s.find('o'))       # 4
# 从索引为5的位置开始查找字符o出现的位置
print(s.find('o', 5))    # 7
# 从后向前查找字符o出现的位置(相当于最后一次出现)
print(s.rfind('o'))      # 12
~~~





###### 3️⃣ **性质判断**

可以通过字符串的`startswith`、`endswith`来判断字符串是否以某个字符串开头和结尾；还可以用`is`开头的方法判断字符串的特征，这些方法都返回布尔值，代码如下所示。

~~~python
s1 = 'hello, world!'

# startwith方法检查字符串是否以指定的字符串开头返回布尔值
print(s1.startswith('He'))    # False
print(s1.startswith('hel'))   # True
# endswith方法检查字符串是否以指定的字符串结尾返回布尔值
print(s1.endswith('!'))       # True

s2 = 'abc123456'

# isdigit方法检查字符串是否由数字构成返回布尔值
print(s2.isdigit())    # False
# isalpha方法检查字符串是否以字母构成返回布尔值
print(s2.isalpha())    # False
# isalnum方法检查字符串是否以数字和字母构成返回布尔值
print(s2.isalnum())    # True
~~~



###### 4️⃣ **格式化字符串**

在Python中，字符串类型可以通过`center`、`ljust`、`rjust`方法做居中、左对齐和右对齐的处理。如果要在字符串的左侧补零，也可以使用`zfill`方法。

~~~python
s = 'hello, world'

# center方法以宽度20将字符串居中并在两侧填充*
print(s.center(20, '*'))  # ****hello, world****
# rjust方法以宽度20将字符串右对齐并在左侧填充空格
print(s.rjust(20))        #         hello, world
# ljust方法以宽度20将字符串左对齐并在右侧填充~
print(s.ljust(20, '~'))   # hello, world~~~~~~~~
# 在字符串的左侧补零
print('33'.zfill(5))      # 00033
print('-33'.zfill(5))     # -0033
~~~



我们之前讲过，在用`print`函数输出字符串时，可以用下面的方式对字符串进行格式化。

```
a = 321
b = 123
print('%d * %d = %d' % (a, b, a * b))
```



~~~python
# 不同数据类型的格式化
# 其他格式化占位符
name = "Alice"
age = 25
score = 95.5

print('%s今年%d岁，成绩%.1f分' % (name, age, score))
# 输出: Alice今年25岁，成绩95.5分
~~~

| 占位符 | 数据类型 | 示例             |
| :----- | :------- | :--------------- |
| `%d`   | 整数     | `%d` → `123`     |
| `%s`   | 字符串   | `%s` → `"hello"` |
| `%f`   | 浮点数   | `%.2f` → `3.14`  |
| `%x`   | 十六进制 | `%x` → `7b`      |



当然，我们也可以用字符串的方法来完成字符串的格式，代码如下所示。

```
a = 321
b = 123
print('{0} * {1} = {2}'.format(a, b, a * b))
```



从Python 3.6开始，格式化字符串还有更为简洁的书写方式，就是在字符串前加上`f`来格式化字符串，在这种以`f`打头的字符串中，`{变量名}`是一个占位符，会被变量对应的值将其替换掉，代码如下所示。

```
a = 321
b = 123
print(f'{a} * {b} = {a * b}')
```



如果需要进一步控制格式化语法中变量值的形式，可以参照下面的表格来进行字符串格式化操作。

如果需要进一步控制格式化语法中变量值的形式，可以参照下面的表格来进行字符串格式化操作。

| 变量值      | 占位符     | 格式化结果      | 说明                   |
| ----------- | ---------- | --------------- | ---------------------- |
| `3.1415926` | `{:.2f}`   | `'3.14'`        | 保留小数点后两位       |
| `3.1415926` | `{:+.2f}`  | `'+3.14'`       | 带符号保留小数点后两位 |
| `-1`        | `{:+.2f}`  | `'-1.00'`       | 带符号保留小数点后两位 |
| `3.1415926` | `{:.0f}`   | `'3'`           | 不带小数               |
| `123`       | `{:0>10d}` | `'0000000123'`  | 左边补`0`，补够10位    |
| `123`       | `{:x<10d}` | `'123xxxxxxx'`  | 右边补`x` ，补够10位   |
| `123`       | `{:>10d}`  | `'       123'`  | 左边补空格，补够10位   |
| `123`       | `{:<10d}`  | `'123       '`  | 右边补空格，补够10位   |
| `123456789` | `{:,}`     | `'123,456,789'` | 逗号分隔格式           |
| `0.123`     | `{:.2%}`   | `'12.30%'`      | 百分比格式             |
| `123456789` | `{:.2e}`   | `'1.23e+08'`    | 科学计数法格式         |





###### 5️⃣ **修剪操作**

字符串的`strip`方法可以帮我们获得将原字符串修剪掉左右两端空格之后的字符串。这个方法非常有实用价值，通常用来将用户输入中因为不小心键入的头尾空格去掉，`strip`方法还有`lstrip`和`rstrip`两个版本，相信从名字大家已经猜出来这两个方法是做什么用的。

~~~python
s = '   jackfrued@126.com  \t\r\n'
# strip方法获得字符串修剪左右两侧空格之后的字符串
print(s.strip())    # jackfrued@126.com
~~~





###### 6️⃣ **替换操作**

如果希望用新的内容替换字符串中指定的内容，可以使用`replace`方法，代码如下所示。`replace`方法的第一个参数是被替换的内容，第二个参数是替换后的内容，还可以通过第三个参数指定替换的次数。

```python
s = 'hello, world'
print(s.replace('o', '@'))     # hell@, w@rld
print(s.replace('o', '@', 1))  # hell@, world
```



###### 7️⃣ **拆分/合并操作**

可以使用字符串的`split`方法将一个字符串拆分为多个字符串（放在一个列表中），也可以使用字符串的`join`方法将列表中的多个字符串连接成一个字符串，代码如下所示。

```
s = 'I love you'
words = s.split()
print(words)            # ['I', 'love', 'you']
print('#'.join(words))  # I#love#you
```



需要说明的是，`split`方法默认使用空格进行拆分，我们也可以指定其他的字符来拆分字符串，而且还可以指定最大拆分次数来控制拆分的效果，代码如下所示。

```
s = 'I#love#you#so#much'
words = s.split('#')
print(words)  # ['I', 'love', 'you', 'so', 'much']
words = s.split('#', 3)
print(words)  # ['I', 'love', 'you', 'so#much']
```

**作用**：使用 `#` 作为分隔符，但**最多只分割 3 次**
**参数说明**：

- `'#'`：分隔符
- `3`：最大分割次数



- 更多例子

  ```python
  s = 'a,b,c,d,e,f'
  
  print(s.split(','))      # ['a', 'b', 'c', 'd', 'e', 'f'] - 全部分割
  print(s.split(',', 2))   # ['a', 'b', 'c,d,e,f'] - 分割2次
  print(s.split(',', 0))   # ['a,b,c,d,e,f'] - 不分割
  print(s.split(',', 1))   # ['a', 'b,c,d,e,f'] - 分割1次
  ```

  

- 实际应用场景

  ```python
  # 处理CSV数据
  csv_data = "John,25,Engineer,New York"
  name, age, job, city = csv_data.split(',', 3)
  print(f"姓名: {name}, 年龄: {age}, 职业: {job}, 城市: {city}")
  
  # 解析URL路径
  url = "https://example.com/blog/python-tutorial"
  protocol, rest = url.split('://', 1)
  domain, path = rest.split('/', 1)
  print(f"协议: {protocol}, 域名: {domain}, 路径: {path}")
  
  # 处理日志文件
  log_line = "ERROR 2023-10-01 10:30:15 Database connection failed"
  level, date, time, message = log_line.split(' ', 3)
  print(f"级别: {level}, 日期: {date}, 时间: {time}, 信息: {message}")
  ```

  

###### 8️⃣ **编码/解码操作**

Python中除了字符串`str`类型外，还有一种表示二进制数据的字节串类型（`bytes`）。所谓字节串，就是**由零个或多个字节组成的有限序列**。通过字符串的`encode`方法，我们可以按照某种编码方式将字符串编码为字节串，我们也可以使用字节串的`decode`方法，将字节串解码为字符串，代码如下所示。

~~~python
a = '骆昊'
b = a.encode('utf-8')
c = a.encode('gbk')
print(a)
print(b, c)  # b'\xe9\xaa\x86\xe6\x98\x8a' b'\xc2\xe6\xea\xbb'
print(b.decode('utf-8'))
print(c.decode('gbk'))
~~~



注意，如果编码和解码的方式不一致，会导致乱码问题（无法再现原始的内容）或引发`UnicodeDecodeError`错误导致程序崩溃。



###### 9️⃣ **其他方法**

对于字符串类型来说，还有一个常用的操作是对字符串进行匹配检查，即检查字符串是否满足某种特定的模式。例如，一个网站对用户注册信息中用户名和邮箱的检查，就属于模式匹配检查。实现模式匹配检查的工具叫做正则表达式，Python语言通过标准库中的`re`模块提供了对正则表达式的支持，我们会在后续的课程中为大家讲解这个知识点。



###### 🔟 **简单的总结**

知道如何表示和操作字符串对程序员来说是非常重要的，因为我们需要处理文本信息，Python中操作字符串可以用拼接、切片等运算符，也可以使用字符串类型的方法。



#### 2.4.5 常用数据结构之集合

在学习了列表和元组之后，我们再来学习一种容器型的数据类型，它的名字叫集合（set）。说到集合这个词大家一定不会陌生，在数学课本上就有这个概念。通常我们对集合的定义是“**把一定范围的、确定的、可以区别的事物当作一个整体来看待**”，集合中的各个事物通常称为集合的**元素**。集合应该满足以下特性：

1. **无序性**：一个集合中，每个元素的地位都是相同的，元素之间是无序的。
2. **互异性**：一个集合中，任何两个元素都是不相同的，即元素在集合中只能出现一次。
3. **确定性**：给定一个集合和一个任意元素，该元素要么属这个集合，要么不属于这个集合，二者必居其一，不允许有模棱两可的情况出现。

Python程序中的集合跟数学上的集合是完全一致的，需要强调的是上面所说的无序性和互异性。无序性说明集合中的元素并不像列中的元素那样一个挨着一个，可以通过索引实现随机访问（随机访问指的是给定一个有效的范围，随机抽取出一个数字，然后通过这个数字可以获取到对应的元素），所以Python中的**集合肯定不能够支持索引运算**。另外，集合的互异性决定了**集合中不能有重复元素**，这一点也是集合区别于列表的关键，说得更直白一些就是，Python中的集合类型会对其中的元素做去重处理。Python中的集合一定是支持`in`和`not in`成员运算的，这样就可以确定一个元素是否属于集合，也就是上面所说的集合的确定性。**集合的成员运算在性能上要优于列表的成员运算**，这是集合的底层存储特性（哈希存储）决定的，此处我们暂时不做讨论，大家可以先记下这个结论。





##### 2.4.5.1 创建集合

在Python中，创建集合可以使用`{}`字面量语法，`{}`中需要至少有一个元素，因为没有元素的`{}`并不是空集合而是一个空字典，我们下一节课就会大家介绍字典的知识。当然，也可以使用内置函数`set`来创建一个集合，准确的说`set`并不是一个函数，而是创建集合对象的构造器，这个知识点我们很快也会讲到，现在不理解跳过它就可以了。要创建空集合可以使用`set()`；也可以将其他序列转换成集合，例如：`set('hello')`会得到一个包含了4个字符的集合（重复的`l`会被去掉）。除了这两种方式，我们还可以使用生成式语法来创建集合，就像我们之前用生成式创建列表那样。要知道集合中有多少个元素，还是使用内置函数`len`；使用`for`循环可以实现对集合元素的遍历。

~~~python
# 创建集合的字面量语法(重复元素不会出现在集合中)
set1 = {1, 2, 3, 3, 3, 2}
print(set1)         # {1, 2, 3}
print(len(set1))    # 3

# 创建集合的构造器语法(后面会讲到什么是构造器)
set2 = set('hello')
print(set2)         # {'h', 'l', 'o', 'e'}

# 将列表转换成集合(可以去掉列表中的重复元素)
set3 = set([1, 2, 3, 3, 2, 1])
print(set3)         # {1, 2, 3}

# 创建集合的生成式语法(将列表生成式的[]换成{})
set4 = {num for num in range(1, 20) if num % 3 == 0 or num % 5 == 0}
print(set4)         # {3, 5, 6, 9, 10, 12, 15, 18}

# 集合元素的循环遍历
for elem in set4:
    print(elem, end= ' ')
~~~



**集合的交集、并集、差集运算还可以跟赋值运算一起构成复合赋值运算，如下所示。**

```python
set1 = {1, 3, 5, 7}
set2 = {2, 4, 6}
# 将set1和set2求并集再赋值给set1
# 也可以通过set1.update(set2)来实现
set1 |= set2
print(set1)    # {1, 2, 3, 4, 5, 6, 7}
set3 = {3, 6, 9}
# 将set1和set3求交集再赋值给set1
# 也可以通过set1.intersection_update(set3)来实现
set1 &= set3
print(set1)    # {3, 6}
```



**比较运算**

两个集合可以用`==`和`!=`进行相等性判断，如果两个集合中的元素完全相同，那么`==`比较的结果就是`True`，否则就是`False`。如果集合`A`的任意一个元素都是集合`B`的元素，那么集合`A`称为集合`B`的子集，即对于 $ \forall{a} \in {A}$ ，均有 $ {a} \in {B} $ ，则 $ {A} \subseteq {B} $ ，`A`是`B`的子集，反过来也可以称`B`是`A`的超集。如果`A`是`B`的子集且`A`不等于`B`，那么`A`就是`B`的真子集。Python为集合类型提供了判断子集和超集的运算符，其实就是我们非常熟悉的`<`和`>`运算符，代码如下所示。

```
set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
set3 = set2
# <运算符表示真子集，<=运算符表示子集
print(set1 < set2, set1 <= set2)    # True True
print(set2 < set3, set2 <= set3)    # False True
# 通过issubset方法也能进行子集判断
print(set1.issubset(set2))      # True

# 反过来可以用issuperset或>运算符进行超集判断
print(set2.issuperset(set1))    # True
print(set2 > set1)              # True
```



如果要判断两个集合有没有相同的元素可以使用`isdisjoint`方法，没有相同元素返回`True`，否则返回`False`，代码如下所示。

```
set1 = {'Java', 'Python', 'Go', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Objective-C', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}
print(set1.isdisjoint(set2))    # False
print(set1.isdisjoint(set3))    # True
```





##### 2.4.5.2 集合的基本特性

```python
# 创建集合
set1 = {1, 2, 3, 4, 5}
set2 = set([3, 4, 5, 6, 7])  # 从列表创建
set3 = set()  # 空集合（不能用 {}，那是字典）

print(set1)  # {1, 2, 3, 4, 5}
print(set2)  # {3, 4, 5, 6, 7}
```



##### 2.4.5.3 集合的核心特性

###### 1. 无序性

```python
my_set = {3, 1, 4, 1, 4, 5, 9, 2}
print(my_set)  # 输出顺序可能不同：{1, 2, 3, 4, 5, 9}
```



###### 2. 元素唯一性（自动去重）

```python
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3, 4}
```



###### 3. 可变集合操作

Python中的集合是可变类型，我们可以通过集合类型的方法为集合添加或删除元素。

```python
# 添加元素
fruits = {"apple", "banana"}
fruits.add("orange")
fruits.update(["grape", "kiwi"])  # 添加多个
print(fruits)  # {'apple', 'banana', 'orange', 'grape', 'kiwi'}

# 删除元素
fruits.remove("banana")  # 如果不存在会报错
fruits.discard("mango")  # 如果不存在不会报错
popped = fruits.pop()    # 随机删除一个元素
print(f"删除了: {popped}, 剩余: {fruits}")

# 清空集合
fruits.clear()
```



```python
# 创建一个空集合
set1 = set()

# 通过add方法添加元素
set1.add(33)
set1.add(55)
set1.update({1, 10, 100, 1000})
print(set1)    # {33, 1, 100, 55, 1000, 10}

# 通过discard方法删除指定元素
set1.discard(100)
set1.discard(99)
print(set1)    # {1, 10, 33, 55, 1000}

# 通过remove方法删除指定元素，建议先做成员运算再删除
# 否则元素如果不在集合中就会引发KeyError异常
if 10 in set1:
    set1.remove(10)
print(set1)    # {33, 1, 55, 1000}

# pop方法可以从集合中随机删除一个元素并返回该元素
print(set1.pop())

# clear方法可以清空整个集合
set1.clear()

print(set1)    # set()
```





##### 2.4.5.4 集合运算

Python为集合类型提供了非常丰富的运算符，主要包括：成员运算、交集运算、并集运算、差集运算、比较运算（相等性、子集、超集）等。

```python
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# 交集
# 方法一: 使用 & 运算符
print(set1 & set2)                # {2, 4, 6}
# 方法二: 使用intersection方法
print(set1.intersection(set2))    # {2, 4, 6}

# 并集
# 方法一: 使用 | 运算符
print(set1 | set2)         # {1, 2, 3, 4, 5, 6, 7, 8, 10}
# 方法二: 使用union方法
print(set1.union(set2))    # {1, 2, 3, 4, 5, 6, 7, 8, 10}

# 差集
# 方法一: 使用 - 运算符
print(set1 - set2)              # {1, 3, 5, 7}
# 方法二: 使用difference方法
print(set1.difference(set2))    # {1, 3, 5, 7}

# 对称差
# 方法一: 使用 ^ 运算符
print(set1 ^ set2)                        # {1, 3, 5, 7, 8, 10}
# 方法二: 使用symmetric_difference方法
print(set1.symmetric_difference(set2))    # {1, 3, 5, 7, 8, 10}
# 方法三: 对称差相当于两个集合的并集减去交集
print((set1 | set2) - (set1 & set2))      # {1, 3, 5, 7, 8, 10}
```

通过上面的代码可以看出，对两个集合求交集，`&`运算符和`intersection`方法的作用是完全相同的，使用运算符的方式更直观而且代码也比较简短。相信大家对交集、并集、差集、对称差这几个概念是比较清楚的，如果没什么印象了可以看看下面的图。

![image-20251015091233624](C:\Users\86181\AppData\Roaming\Typora\typora-user-images\image-20251015091233624.png)







###### 1. 基本成员检查

~~~python
fruits = {"apple", "banana", "orange", "grape"}

# 使用 in 运算符检查成员
print("apple" in fruits)    # True
print("mango" in fruits)    # False

# 使用 not in 运算符
print("apple" not in fruits) # False
print("mango" not in fruits) # True
~~~



###### 2. 成员运算的性能优势

```python
import time

# 列表 vs 集合 成员检查性能对比
large_list = list(range(1000000))
large_set = set(range(1000000))

# 列表查找（O(n)）
start = time.time()
result1 = 999999 in large_list
end = time.time()
print(f"列表查找时间: {end - start:.6f}秒")

# 集合查找（O(1)）
start = time.time()
result2 = 999999 in large_set
end = time.time()
print(f"集合查找时间: {end - start:.6f}秒")
```





###### 3. 实际应用场景

1. 数据过滤

```python
# 过滤有效用户
valid_users = {"alice", "bob", "charlie", "david"}
current_users = ["alice", "eve", "bob", "frank"]

valid_current_users = [user for user in current_users if user in valid_users]
print(f"有效用户: {valid_current_users}")  # ['alice', 'bob']
```



2. 权限检查

```python
# 用户权限验证
admin_roles = {"super_admin", "content_admin", "user_admin"}
user_roles = {"user", "content_admin"}

def has_admin_access(roles):
    return any(role in admin_roles for role in roles)

print(has_admin_access(user_roles))  # True
```



3. 黑名单过滤

```python
# 内容过滤
blacklist_words = {"spam", "scam", "fake", "fraud"}
user_message = "this is a fake product"

# 检查是否包含黑名单词汇
contains_blacklist = any(word in user_message for word in blacklist_words)
print(f"包含违禁词: {contains_blacklist}")  # True

# 或者找到具体的违禁词
found_blacklist = [word for word in blacklist_words if word in user_message]
print(f"发现的违禁词: {found_blacklist}")  # ['fake']
```







##### 2.4.5.5 集合关系判断

```python
set_x = {1, 2, 3}
set_y = {1, 2, 3, 4, 5}
set_z = {1, 2}

# 子集判断
print(set_z.issubset(set_x))    # True
print(set_z.issubset(set_y))    # True
print(set_z <= set_y)           # True

# 超集判断
print(set_y.issuperset(set_z))  # True
print(set_y >= set_z)           # True

# 交集判断
print(set_x.isdisjoint({6, 7, 8}))  # True (没有交集)
```



##### 2.4.5.6 实际应用场景

###### 1. 数据去重

```python
# 快速去重
emails = ["a@test.com", "b@test.com", "a@test.com", "c@test.com"]
unique_emails = set(emails)
print(f"唯一邮箱数量: {len(unique_emails)}")
```



###### 2. 关系测试

```python
# 寻找共同兴趣
alice_interests = {"reading", "music", "travel"}
bob_interests = {"sports", "music", "cooking"}
common_interests = alice_interests & bob_interests
print(f"共同兴趣: {common_interests}")  # {'music'}
```



###### 3. 成员检查（高效）

```python
# 集合的成员检查是 O(1) 时间复杂度
valid_codes = {1001, 1002, 1003, 1004, 1005}
user_code = 1003

if user_code in valid_codes:
    print("验证码有效")
else:
    print("验证码无效")
```



##### 2.4.5.7 集合推导式

```python
# 创建平方数集合
squares = {x**2 for x in range(10)}
print(squares)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# 过滤偶数
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
even_numbers = {x for x in numbers if x % 2 == 0}
print(even_numbers)  # {2, 4, 6, 8}
```



##### 2.4.5.8 不可变集合 (frozenset)

Python中还有一种不可变类型的集合，名字叫`frozenset`。`set`跟`frozenset`的区别就如同`list`跟`tuple`的区别，`frozenset`由于是不可变类型，能够计算出哈希码，因此它可以作为`set`中的元素。除了不能添加和删除元素，`frozenset`在其他方面跟`set`基本是一样的，下面的代码简单的展示了`frozenset`的用法。

```python
# 创建不可变集合
immutable_set = frozenset([1, 2, 3, 4])
print(immutable_set)  # frozenset({1, 2, 3, 4})

# 可以用作字典的键
dict_with_frozenset = {immutable_set: "value"}
```



```python
set1 = frozenset({1, 3, 5, 7})
set2 = frozenset(range(1, 6))
print(set1 & set2)    # frozenset({1, 3, 5})
print(set1 | set2)    # frozenset({1, 2, 3, 4, 5, 7})
print(set1 - set2)    # frozenset({7})
print(set1 < set2)    # False
```



##### 2.4.5.9 注意事项

```python
# 集合只能包含不可变类型
valid_set = {1, "hello", (1, 2)}  # ✓
# invalid_set = {1, [1, 2]}       # ✗ 列表是可变的，会报错

# 集合比较是基于内容的
set_a = {1, 2, 3}
set_b = {3, 2, 1}
print(set_a == set_b)  # True (顺序不重要)
```





##### 2.4.5.10 集合间的成员运算

###### 1. 检查子集关系

```python
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {4, 5}

# 检查是否所有元素都在另一个集合中
print(all(x in B for x in A))  # True
print(all(x in B for x in C))  # True

# 使用内置方法（更高效）
print(A.issubset(B))  # True
print(C.issubset(B))  # True
```



###### 2. 检查交集

```python
group1 = {"math", "physics", "chemistry"}
group2 = {"biology", "physics", "history"}

# 检查是否有共同元素
has_common = any(subject in group2 for subject in group1)
print(f"有共同科目: {has_common}")  # True

# 找到具体共同元素
common_subjects = {subject for subject in group1 if subject in group2}
print(f"共同科目: {common_subjects}")  # {'physics'}
```





##### 2.4.5.11 集合间的成员运算

###### 1. 检查子集关系

```python
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {4, 5}

# 检查是否所有元素都在另一个集合中
print(all(x in B for x in A))  # True
print(all(x in B for x in C))  # True

# 使用内置方法（更高效）
print(A.issubset(B))  # True
print(C.issubset(B))  # True
```



###### 2. 检查交集

```python
group1 = {"math", "physics", "chemistry"}
group2 = {"biology", "physics", "history"}

# 检查是否有共同元素
has_common = any(subject in group2 for subject in group1)
print(f"有共同科目: {has_common}")  # True

# 找到具体共同元素
common_subjects = {subject for subject in group1 if subject in group2}
print(f"共同科目: {common_subjects}")  # {'physics'}
```



##### 2.4.5.12 高级成员运算技巧

###### 1. 多重条件检查

```python
# 复合条件成员检查
vip_users = {"alice", "bob", "charlie"}
active_users = {"bob", "david", "eve"}
premium_users = {"charlie", "frank"}

# 检查用户是否满足多个条件
def is_elite_user(username):
    return (username in vip_users and 
            username in active_users and 
            username in premium_users)

print(is_elite_user("charlie"))  # False (不在active_users)
print(is_elite_user("bob"))      # False (不在premium_users)

# 更简洁的写法
def is_elite_user_v2(username):
    return username in (vip_users & active_users & premium_users)

print(is_elite_user_v2("charlie"))  # False
```



###### 2. 动态成员检查

```python
# 基于条件的动态成员检查
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# 检查是否存在满足条件的成员
has_even = any(x % 2 == 0 for x in numbers)
has_large = any(x > 8 for x in numbers)
has_specific = any(x in {3, 7, 11} for x in numbers)

print(f"有偶数: {has_even}")        # True
print(f"有大数: {has_large}")       # True  
print(f"有特定数: {has_specific}")  # True
```



###### 3. 成员统计

```python
# 统计满足条件的成员数量
survey_responses = {"excellent", "good", "fair", "poor", "good", "excellent"}

positive_responses = {"excellent", "good"}
negative_responses = {"fair", "poor"}

positive_count = sum(1 for response in survey_responses if response in positive_responses)
negative_count = sum(1 for response in survey_responses if response in negative_responses)

print(f"正面评价: {positive_count}")  # 3
print(f"负面评价: {negative_count}")  # 1
```



##### 2.4.5.13 性能优化技巧

```python
# 在条件语句中直接使用
allowed_domains = {"gmail.com", "yahoo.com", "hotmail.com"}
user_email = "user@gmail.com"

domain = user_email.split('@')[-1]
if domain in allowed_domains:
    print("邮箱域名有效")
else:
    print("请使用支持的邮箱域名")

# 在循环中过滤
data = [("apple", 1.2), ("banana", 0.8), ("orange", 1.5), ("grape", 2.0)]
available_fruits = {"apple", "orange", "mango"}

# 只处理可用的水果
for fruit, price in data:
    if fruit in available_fruits:
        print(f"{fruit}: ${price}")
```



##### 2.4.5.14 成员运算的返回值应用

~~~python
# 在条件语句中直接使用
allowed_domains = {"gmail.com", "yahoo.com", "hotmail.com"}
user_email = "user@gmail.com"

domain = user_email.split('@')[-1]
if domain in allowed_domains:
    print("邮箱域名有效")
else:
    print("请使用支持的邮箱域名")

# 在循环中过滤
data = [("apple", 1.2), ("banana", 0.8), ("orange", 1.5), ("grape", 2.0)]
available_fruits = {"apple", "orange", "mango"}

# 只处理可用的水果
for fruit, price in data:
    if fruit in available_fruits:
        print(f"{fruit}: ${price}")
~~~



输出结果：

```
邮箱域名有效
apple: $1.2
orange: $1.5
```





##### 2.4.5.15 简单的总结

Python中的集合底层使用了**哈希存储**的方式，对于这一点我们暂时不做介绍，在后面的课程有需要的时候再为大家讲解集合的底层原理，现阶段大家只需要知道**集合是一种容器**，元素必须是`hashable`类型，与列表不同的地方在于集合中的元素**没有序**、**不能用索引运算**、**不能重复**。





#### 2.4.6 常用数据结构之字典

迄今为止，我们已经为大家介绍了Python中的三种容器型数据类型，但是这些数据类型仍然不足以帮助我们解决所有的问题。例如，我们要保存一个人的信息，包括姓名、年龄、体重、单位地址、家庭住址、本人手机号、紧急联系人手机号等信息，你会发现我们之前学过的列表、元组和集合都不是最理想的选择。

```
person1 = ['王大锤', 55, 60, '科华北路62号', '中同仁路8号', '13122334455', '13800998877']
person2 = ('王大锤', 55, 60, '科华北路62号', '中同仁路8号', '13122334455', '13800998877')
person3 = {'王大锤', 55, 60, '科华北路62号', '中同仁路8号', '13122334455', '13800998877'}
```



集合肯定是最不合适的，因为集合有去重特性，如果一个人的年龄和体重相同，那么集合中就会少一项信息；同理，如果这个人的家庭住址和单位地址是相同的，那么集合中又会少一项信息。另一方面，虽然列表和元组可以把一个人的所有信息都保存下来，但是当你想要获取这个人的手机号时，你得先知道他的手机号是列表或元组中的第6个还是第7个元素；当你想获取一个人的家庭住址时，你还得知道家庭住址是列表或元组中的第几项。总之，在遇到上述的场景时，列表、元组、字典都不是最合适的选择，我们还需字典（dictionary）类型，这种数据类型最适合把相关联的信息组装到一起，并且可以帮助我们解决程序中为真实事物建模的问题。

说到字典这个词，大家一定不陌生，读小学的时候每个人基本上都有一本《新华字典》，如下图所示。

![image-20251015095734604](C:\Users\86181\AppData\Roaming\Typora\typora-user-images\image-20251015095734604.png)

Python程序中的字典跟现实生活中的字典很像，它以键值对（键和值的组合）的方式把数据组织到一起，我们可以通过键找到与之对应的值并进行操作。就像《新华字典》中，每个字（键）都有与它对应的解释（值）一样，每个字和它的解释合在一起就是字典中的一个条目，而字典中通常包含了很多个这样的条目。



##### 2.4.6.1 创建和使用字典

在Python中创建字典可以使用`{}`字面量语法，这一点跟上一节课讲的集合是一样的。但是字典的`{}`中的元素是以键值对的形式存在的，每个元素由`:`分隔的两个值构成，`:`前面是键，`:`后面是值，代码如下所示。

```python
xinhua = {
    '麓': '山脚下',
    '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
    '蕗': '甘草的别名',
    '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
}
print(xinhua)
person = {
    'name': '王大锤', 'age': 55, 'weight': 60, 'office': '科华北路62号',
    'home': '中同仁路8号', 'tel': '13122334455', 'econtact': '13800998877'
}
print(person)
```



通过上面的代码，相信大家已经看出来了，用字典来保存一个人的信息远远优于使用列表或元组，因为我们可以用`:`前面的键来表示条目的含义，而`:`后面就是这个条目所对应的值。

当然，如果愿意，我们也可以使用内置函数`dict`或者是字典的生成式语法来创建字典，代码如下所示。

```python
# dict函数(构造器)中的每一组参数就是字典中的一组键值对
person = dict(name='王大锤', age=55, weight=60, home='中同仁路8号')
print(person)    # {'name': '王大锤', 'age': 55, 'weight': 60, 'home': '中同仁路8号'}

# 可以通过Python内置函数zip压缩两个序列并创建字典
items1 = dict(zip('ABCDE', '12345'))
print(items1)    # {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'}
items2 = dict(zip('ABCDE', range(1, 10)))
print(items2)    # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

# 用字典生成式语法创建字典
items3 = {x: x ** 3 for x in range(1, 6)}
print(items3)     # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
```



想知道字典中一共有多少组键值对，仍然是使用`len`函数；如果想对字典进行遍历，可以用`for`循环，但是需要注意，`for`循环只是对字典的键进行了遍历，不过没关系，在讲完字典的运算后，我们可以通过字典的键获取到和这个键对应的值。

```python
person = {'name': '王大锤', 'age': 55, 'weight': 60, 'office': '科华北路62号'}

print("=== 方法1: 通过key获取value ===")
for key in person:
    print(person[key])

print("\n=== 方法2: 直接遍历values ===")
for value in person.values():
    print(value)

print("\n=== 方法3: 同时显示键值对 ===")
for key, value in person.items():
    print(f"{key}: {value}")

print("\n=== 方法4: 一次性获取所有值 ===")
print(list(person.values()))
```



##### 2.4.6.2 字典的运算

**对于字典类型来说，成员运算和索引运算肯定是最为重要的，前者可以判定指定的键在不在字典中，后者可以通过键获取对应的值或者向字典中加入新的键值对。**值得注意的是，字典的索引不同于列表的索引，列表中的元素因为有属于自己有序号，所以列表的索引是一个整数；字典中因为保存的是键值对，所以字典的索引是键值对中的键，通过索引操作可以修改原来的值或者向字典中存入新的键值对。需要**特别提醒**大家注意的是，**字典中的键必须是不可变类型**，例如整数（`int`）、浮点数（`float`）、字符串（`str`）、元组（`tuple`）等类型的值；显然，列表（`list`）和集合（`set`）是不能作为字典中的键的，当然字典类型本身也不能再作为字典中的键，因为字典也是可变类型，但是字典可以作为字典中的值。关于可变类型不能作为字典中的键的原因，我们在后面的课程中再为大家详细说明。这里，我们先看看下面的代码，了解一下字典的成员运算和索引运算。

```python
person = {'name': '王大锤', 'age': 55, 'weight': 60, 'office': '科华北路62号'}
# 检查name和tel两个键在不在person字典中
print('name' in person, 'tel' in person)    # True False

# 通过age修将person字典中对应的值修改为25
if 'age' in person:
    person['age'] = 25
    
# 通过索引操作向person字典中存入新的键值对
person['tel'] = '13122334455'
person['signature'] = '你的男朋友是一个盖世垃圾，他会踏着五彩祥云去迎娶你的闺蜜'
print('name' in person, 'tel' in person)    # True True

# 检查person字典中键值对的数量
print(len(person))    # 6


# 对字典的键进行循环并通索引运算获取键对应的值
for key in person:
    print(f'{key}: {person[key]}') # key:value, value获取的表达方式：person[key]
    print(person.values())
```

> 需要注意，在通过索引运算获取字典中的值时，如指定的键没有在字典中，将会引发`KeyError`异常。



##### 2.4.6.3 字典的方法

字典类型的方法基本上都跟字典的键值对操作相关，可以通过下面的例子来了解这些方法的使用。例如，我们要用一个字典来保存学生的信息，我们可以使用学生的学号作为字典中的键，通过学号做索引运算就可以得到对应的学生；我们可以把字典的值也做成一个字典，这样就可以用多组键值对分别存储学生的姓名、性别、年龄、籍贯等信息，代码如下所示。

```python
# 字典中的值又是一个字典(嵌套的字典)
students = {
    1001: {'name': '狄仁杰', 'sex': True, 'age': 22, 'place': '山西大同'},
    1002: {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'},
    1003: {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}
}

# 使用get方法通过键获取对应的值，如果取不到不会引发KeyError异常而是返回None或设定的默认值
print(students.get(1002))    # {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'}
print(students.get(1005))    # None
print(students.get(1005, {'name': '无名氏'}))    # {'name': '无名氏'}

# 获取字典中所有的键
print(students.keys())      # dict_keys([1001, 1002, 1003])
# 获取字典中所有的值
print(students.values())    # dict_values([{...}, {...}, {...}])
# 获取字典中所有的键值对
print(students.items())     # dict_items([(1001, {...}), (1002, {....}), (1003, {...})])
# 对字典中所有的键值对进行循环遍历
for key, value in students.items():
    print(key, '--->', value)

# 使用pop方法通过键删除对应的键值对并返回该值
stu1 = students.pop(1002)
print(stu1)             # {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'}
print(len(students))    # 2
# stu2 = students.pop(1005)    # KeyError: 1005
stu2 = students.pop(1005, {})
print(stu2)             # {}

# 使用popitem方法删除字典中最后一组键值对并返回对应的二元组
# 如果字典中没有元素，调用该方法将引发KeyError异常
key, value = students.popitem()
print(key, value)    # 1003 {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}

# 如果这个键在字典中存在，setdefault返回原来与这个键对应的值
# 如果这个键在字典中不存在，向字典中添加键值对，返回第二个参数的值，默认为None
result = students.setdefault(1005, {'name': '方启鹤', 'sex': True})
print(result)        # {'name': '方启鹤', 'sex': True}
print(students)      # {1001: {...}, 1005: {...}}

# 使用update更新字典元素，相同的键会用新值覆盖掉旧值，不同的键会添加到字典中
others = {
    1005: {'name': '乔峰', 'sex': True, 'age': 32, 'place': '北京大兴'},
    1010: {'name': '王语嫣', 'sex': False, 'age': 19},
    1008: {'name': '钟灵', 'sex': False}
}
students.update(others)
print(students)      # {1001: {...}, 1005: {...}, 1010: {...}, 1008: {...}}
```



跟列表一样，从字典中删除元素也可以使用`del`关键字，在删除元素的时候如果指定的键索引不到对应的值，一样会引发`KeyError`异常，具体的做法如下所示。

```python
person = {'name': '王大锤', 'age': 25, 'sex': True}
del person['age']
print(person)    # {'name': '王大锤', 'sex': True}
```



##### 2.4.6.4 字典的应用

我们通过几个简单的例子来讲解字典的应用。

**例子1**：输入一段话，统计每个英文字母出现的次数。

```python
sentence = input('请输入一段话: ')
counter = {}
for ch in sentence:
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        counter[ch] = counter.get(ch, 0) + 1
for key, value in counter.items():
    print(f'字母{key}出现了{value}次.')
```



**忽略大小写**

```python
sentence = input('请输入一段话: ')
counter = {}
for ch in sentence:
    if ch.isalpha():  # 更Pythonic的判断方式
        ch_lower = ch.lower()  # 转换为小写
        counter[ch_lower] = counter.get(ch_lower, 0) + 1

for key, value in counter.items():
    print(f'字母{key}出现了{value}次.')
```

输出结果：

```
请输入一段话: hello world
字母h出现了1次.
字母e出现了1次.
字母l出现了3次.
字母o出现了2次.
字母w出现了1次.
字母r出现了1次.
字母d出现了1次.
```



**使用 defaultdict 简化代码**

~~~python
from collections import defaultdict

sentence = input('请输入一段话: ')
counter = defaultdict(int)  # 默认值为0

for ch in sentence:
    if ch.isalpha():
        counter[ch] += 1  # 不需要get()方法了

for key, value in counter.items():
    print(f'字母{key}出现了{value}次.')
~~~

输出结果：

```
请输入一段话: Hello World
字母H出现了1次.
字母e出现了1次.
字母l出现了3次.
字母o出现了2次.
字母W出现了1次.
字母r出现了1次.
字母d出现了1次.
```



**按字母顺序输出**

```python
sentence = input('请输入一段话: ')
counter = {}
for ch in sentence:
    if ch.isalpha():
        counter[ch] = counter.get(ch, 0) + 1

# 按字母顺序排序输出
for key in sorted(counter.keys()):
    print(f'字母{key}出现了{counter[key]}次.')
```

输出结果：

```
请输入一段话: hello world
字母d出现了1次.
字母e出现了1次.
字母h出现了1次.
字母l出现了3次.
字母o出现了2次.
字母r出现了1次.
字母w出现了1次.
```



**例子2**：在一个字典中保存了股票的代码和价格，找出股价大于100元的股票并创建一个新的字典。

> **说明**：可以用字典的生成式语法来创建这个新字典。

```python
stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
stocks2 = {key: value for key, value in stocks.items() if value > 100}
print(stocks2)
```





1. 转换键或值

```python
# 将所有价格转换为整数
stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
stocks_int = {key: int(value) for key, value in stocks.items()}
print(stocks_int)
# {'AAPL': 191, 'GOOG': 1186, 'IBM': 149, 'ORCL': 48, 'ACN': 166, 'FB': 208, 'SYMC': 21}

# 将键转换为小写
stocks_lower = {key.lower(): value for key, value in stocks.items()}
print(stocks_lower)
# {'aapl': 191.88, 'goog': 1186.96, 'ibm': 149.24, ...}
```



2. 复杂条件过滤

```python
# 筛选价格在50-200之间的股票
stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
stocks_mid = {key: value for key, value in stocks.items() if 50 <= value <= 200}
print(stocks_mid)
# {'AAPL': 191.88, 'IBM': 149.24, 'ACN': 166.89, 'FB': 208.09}

# 筛选股票代码长度等于4的
stocks_len4 = {key: value for key, value in stocks.items() if len(key) == 4}
print(stocks_len4)
# {'AAPL': 191.88, 'GOOG': 1186.96}
```



3. 键值同时转换

```python
# 创建新的键值对格式
stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
stocks_formatted = {f"Stock_{key}": f"${value}" for key, value in stocks.items()}
print(stocks_formatted)
# {'Stock_AAPL': '$191.88', 'Stock_GOOG': '$1186.96', ...}

# 计算价格百分比变化（假设原价）
original_prices = {'AAPL': 180, 'GOOG': 1100, 'IBM': 150, 'ORCL': 50, 'ACN': 160, 'FB': 200, 'SYMC': 20}
price_change = {key: ((stocks[key] - original_prices[key]) / original_prices[key]) * 100 
                for key in stocks if key in original_prices}
print(price_change)
# 计算每只股票的涨幅百分比
```



4. 嵌套字典推导式

```python
# 处理嵌套字典
portfolio = {
    'tech': {'AAPL': 191.88, 'GOOG': 1186.96, 'FB': 208.09},
    'services': {'IBM': 149.24, 'ACN': 166.89},
    'other': {'ORCL': 48.44, 'SYMC': 21.29}
}

# 筛选每个类别中价格大于100的股票
filtered_portfolio = {
    category: {stock: price for stock, price in stocks.items() if price > 100}
    for category, stocks in portfolio.items()
}
print(filtered_portfolio)
```



5. 与其他数据结构结合

```python
stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 与zip结合使用
names = ['Apple', 'Google', 'IBM', 'Oracle', 'Accenture', 'Facebook', 'Symantec']
codes = ['AAPL', 'GOOG', 'IBM', 'ORCL', 'ACN', 'FB', 'SYMC']

# 创建名称到价格的映射
name_to_price = {name: stocks[code] for name, code in zip(names, codes)}
print(name_to_price)
```



##### 2.4.6.5 简单的总结

Python程序中的字典跟现实生活中字典非常像，允许我们**以键值对的形式保存数据**，再**通过键索引对应的值**。这是一种非常**有利于数据检索**的数据类型，底层原理我们在后续的课程中为大家讲解。再次提醒大家注意，**字典中的键必须是不可变类型**，字典中的值可以是任意类型。







#### 2.4.7 字典（dictionary）- 补充内容

##### 2.4.7.1 什么是「字典（dictionary）」？

在 Python 中，**字典（`dict`）** 是一种用来 **存储 “键值对” 数据** 的数据结构。

它就像一本“查字典”📖：

> 通过 “词”（key） 可以快速找到对应的 “解释”（value）。



##### 2.4.7.2 基本结构

一个字典由一组 **键（key）和值（value）** 组成，格式如下：

```python
字典名 = {键1: 值1, 键2: 值2, 键3: 值3, ...}
```

比如：

```
student = {"name": "Alice", "age": 18, "grade": "A"}
```

表示一个学生的信息：

- 键 `"name"` 对应的值是 `"Alice"`
- 键 `"age"` 对应的值是 `18`
- 键 `"grade"` 对应的值是 `"A"`



##### 2.4.7.3 如何使用字典

###### 1️⃣ 取值（通过 key）

```
print(student["name"])   # 输出：Alice
print(student["age"])    # 输出：18
```



###### 2️⃣ 修改值

```
student["age"] = 19
```



###### 3️⃣ 新增键值对

```
student["school"] = "Maple High School"
```



###### 4️⃣ 删除键值对

```
del student["grade"]
```



###### 5️⃣ 遍历字典

```
for key, value in student.items():
    print(key, ":", value)
```

输出：

```
name : Alice
age : 19
school : Maple High School
```



##### 2.4.7.4 结合你那段“掷色子”的例子

在这段代码中：

```
dice_counts = {i: 0 for i in range(1, 7)}
```

这是一个字典，意思是：

| 键（key） | 值（value） | 含义             |
| --------- | ----------- | ---------------- |
| 1         | 0           | “1点” 出现的次数 |
| 2         | 0           | “2点” 出现的次数 |
| 3         | 0           | “3点” 出现的次数 |
| 4         | 0           | “4点” 出现的次数 |
| 5         | 0           | “5点” 出现的次数 |
| 6         | 0           | “6点” 出现的次数 |

当你掷出一个点数，比如 4：

```
dice_counts[4] += 1
```

就相当于把 `"4点出现的次数"` 加 1。



##### 2.4.7.5 总结一句话：

> 🔑 **字典（dict）** 就是一种 **“键 → 值”** 的映射结构，
> 用来存储和快速查找数据，非常常用。





### 2.5 函数

#### 2.5.1 函数和模块

在讲解本节课的内容之前，我们先来研究一道数学题，请说出下面的方程有多少组正整数解。

$$
x_1 + x_2 + x_3 + x_4 = 8
$$

你可能已经想到了，这个问题其实等同于将8个苹果分成四组且每组至少一个苹果有多少种方案，因此该问题还可以进一步等价于在分隔8个苹果的7个空隙之间插入三个隔板将苹果分成四组有多少种方案，也就是从7个空隙选出3个空隙放入隔板的组合数，所以答案是 $C_7^3 = 35$。组合数的计算公式如下所示。

$$
C_M^N = \frac{M!}{N!(M-N)!}
$$

根据我们前面学习的知识，可以用循环做累乘的方式来计算阶乘，那么通过下面的 Python 代码我们就可以计算出组合数 $C_M^N$ 的值，代码如下所示。

##### 2.5.1.1 举例子

~~~python
"""
输入M和N计算C(M,N)

Version: 0.1
Author: 骆昊
"""

# 定义函数：def是定义函数的关键字、fac是函数名，num是参数（自变量）
def fac(num):
    """求阶乘"""
    result = 1
    for i in range(1, num + 1):  # 使用i作为循环变量
        result *= i
        print(f"i={i}: result={result}")
    return result

m = int(input('m = '))  # m = 4
n = int(input('n = '))  # n = 3

# 当需要计算阶乘的时候不用再写重复的代码而是直接调用函数fac
# 调用函数的语法是在函数名后面跟上圆括号并传入参数
print(fac(m) // fac(n) // fac(m - n))
~~~



##### 2.5.1.2 **数据调用过程（假设输入 m=4, n=3）**

第一步：计算 `fac(m)` 即 `fac(4)`

```
进入 fac(4) 函数：
i = 1: result = 1 * 1 = 1
i = 2: result = 1 * 2 = 2
i = 3: result = 2 * 3 = 6
i = 4: result = 6 * 4 = 24
返回结果：24
```



第二步：计算 `fac(n)` 即 `fac(3)`

```
进入 fac(3) 函数：
i = 1: result = 1 * 1 = 1
i = 2: result = 1 * 2 = 2
i = 3: result = 2 * 3 = 6
返回结果：6
```



第三步：计算 `fac(m - n)` 即 `fac(1)`

```
进入 fac(1) 函数：
i = 1: result = 1 * 1 = 1
返回结果：1
```



第四步：计算组合数

```
C(4, 3) = 24 // 6 // 1 = 4
最终输出：4
```



完整执行流程：

```
m = 4
n = 3

计算 fac(4):
i=1: result=1
i=2: result=2
i=3: result=6
i=4: result=24

计算 fac(3):
i=1: result=1
i=2: result=2
i=3: result=6

计算 fac(1):
i=1: result=1

最终结果：24 // 6 // 1 = 4
```



关键改进：

- 将循环变量从 `n` 改为 `i`，避免了与参数 `num` 的混淆
- 这样代码更清晰，不会让读者误解循环变量与函数参数的关系
- 添加了更详细的打印信息，便于理解执行过程

计算结果仍然是正确的：`C(4, 3) = 4`



~~~python
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
~~~



```
m = 4
n = 3
计算 C(4, 3) = 4! // 3! // (4-3)!
==================================================
计算 4! 的过程：
i = 1: result = 1 * 1 = 1
i = 2: result = 1 * 2 = 2
i = 3: result = 2 * 3 = 6
i = 4: result = 6 * 4 = 24
4! = 24

计算 3! 的过程：
i = 1: result = 1 * 1 = 1
i = 2: result = 1 * 2 = 2
i = 3: result = 2 * 3 = 6
3! = 6

计算 1! 的过程：
i = 1: result = 1 * 1 = 1
1! = 1

==================================================
最终结果：C(4, 3) = 24 // 6 // 1 = 4
```



> **说明**：事实上，Python标准库的`math`模块中有一个名为`factorial`的函数已经实现了求阶乘的功能，我们可以直接使用该函数来计算阶乘。**将来我们使用的函数，要么是自定义的函数，要么是Python标准库或者三方库中提供的函数**。



##### 2.5.1.3 完全使用math.factorial（推荐）

~~~python
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
~~~



**最简洁的版本**

~~~python
import math

# 最简单的实现
m = int(input('m = '))
n = int(input('n = '))

# 直接使用math.factorial
combination = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))

print(f"C({m}, {n}) = {combination}")
~~~





##### 2.5.1.4 函数的参数

如果函数中没有`return`语句，那么函数默认返回代表空值的`None`。另外，在定义函数时，函数也可以没有自变量，但是函数名后面的圆括号是必须有的。Python中还允许函数的参数拥有默认值，我们可以把之前讲过的一个例子“CRAPS赌博游戏”中摇色子获得点数的功能封装成函数，代码如下所示。

~~~python
from random import randint

def roll_dice(n=2):
    """摇色子返回总的点数"""
    total = 0
    print(f"开始摇{n}个色子：")
    for i in range(n):
        point = randint(1, 6)
        total += point
        print(f"  第{i+1}次摇色子点数: {point}，当前总分: {total}")
    print(f"摇色子总点数: {total}\n")
    return total

# 测试
print("=== 第一次摇色子 ===")
result1 = roll_dice() # 设置默认值为 n = 2
print(f"返回值: {result1}\n")

print("=== 第二次摇色子 ===")
result2 = roll_dice(3)
print(f"返回值: {result2}")
~~~

> - [ ] print(roll_dice())  # 没有传入参数，使用默认值 n=2, 这相当于：print(roll_dice(2))  # 明确传入参数 2

输出结果：

```
=== 第一次摇色子 ===
开始摇2个色子：
  第1次摇色子点数: 6，当前总分: 6
  第2次摇色子点数: 6，当前总分: 12
摇色子总点数: 12

返回值: 12

=== 第二次摇色子 ===
开始摇3个色子：
  第1次摇色子点数: 6，当前总分: 6
  第2次摇色子点数: 5，当前总分: 11
  第3次摇色子点数: 5，当前总分: 16
摇色子总点数: 16

返回值: 16
```



我们再来看一个更为简单的例子。

```python
def add(a=0, b=0, c=0):
    """三个数相加求和"""
    return a + b + c

# 调用add函数，没有传入参数，那么a、b、c都使用默认值0
print(add())         # 0

# 调用add函数，传入一个参数，那么该参数赋值给变量a, 变量b和c使用默认值0
print(add(1))        # 1

# 调用add函数，传入两个参数，1和2分别赋值给变量a和b，变量c使用默认值0
print(add(1, 2))     # 3

# 调用add函数，传入三个参数，分别赋值给a、b、c三个变量
print(add(1, 2, 3))  # 6

# 传递参数时可以不按照设定的顺序进行传递，但是要用“参数名=参数值”的形式
print(add(c=50, a=100, b=200))    # 350

# 调用add函数，只计算两个数，第三个用默认值0
print(add(5, 10))        # 15

# 调用add函数，只计算第一个和第三个数
print(add(5, c=15))      # 20

# 调用add函数，只计算第二个和第三个数
print(add(b=10, c=20))   # 30

# 调用add函数，混合使用位置参数和关键字参数
print(add(1, c=3))       # 4 (a=1, b=0, c=3)
```

> **注意**：带默认值的参数必须放在不带默认值的参数之后，否则将产生`SyntaxError`错误，错误消息是：`non-default argument follows default argument`，翻译成中文的意思是“没有默认值的参数放在了带默认值的参数后面”。

**错误示例：**

python

```
# 语法错误：带默认值的参数在前面，不带默认值的在后面
def wrong_func(a=1, b, c=2):  # ❌ SyntaxError
    return a + b + c
```



**正确示例：**

python

```
# 正确：不带默认值的参数在前面，带默认值的在后面
def correct_func(b, a=1, c=2):  # ✅
    return a + b + c
```



##### 2.5.1.5 可变参数

接下来，我们还可以实现一个对任意多个数求和的`add`函数，因为Python语言中的函数可以通过星号表达式语法来支持可变参数。所谓可变参数指的是在调用函数时，可以向函数传入`0`个或任意多个参数。将来我们以团队协作的方式开发商业项目时，很有可能要设计函数给其他人使用，但有的时候我们并不知道函数的调用者会向该函数传入多少个参数，这个时候可变参数就可以派上用场。下面的代码演示了用可变参数实现对任意多个数求和的`add`函数。

~~~python
"""
可变参数

Version: 0.1
Author: 骆昊
"""

# 用星号表达式来表示args可以接收0个或任意多个参数
def add(*args):
    total = 0
    # 可变参数可以放在for循环中取出每个参数的值
    for val in args:
        if type(val) in (int, float):
            total += val
    return total


# 在调用add函数时可以传入0个或任意多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))
~~~



可变参数（Variable Arguments）是Python中非常强大的特性，允许函数接受任意数量的参数。

###### 2.5.1.5.1 使用 `*args` 接收任意数量的位置参数

**基本用法：**

```python
def add(*args):
    """计算任意数量的数字之和"""
    print(f"接收到的参数: {args}, 类型: {type(args)}")
    total = 0
    for num in args:
        total += num
    return total

# 测试
print(add(1, 2))           # 接收到的参数: (1, 2), 类型: <class 'tuple'>
print(add(1, 2, 3, 4, 5))  # 接收到的参数: (1, 2, 3, 4, 5), 类型: <class 'tuple'>
print(add())               # 接收到的参数: (), 类型: <class 'tuple'>
```



**改进的add函数：**

```python
def add(*numbers):
    """更灵活的加法函数"""
    return sum(numbers)

print(add(1))              # 1
print(add(1, 2))           # 3
print(add(1, 2, 3, 4, 5))  # 15
print(add())               # 0
```



###### 2.5.1.5.2 使用 `**kwargs` 接收任意数量的关键字参数

```python
def person_info(**kwargs):
    """接收任意数量的关键字参数"""
    print(f"接收到的参数: {kwargs}, 类型: {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 测试
person_info(name="张三", age=25)
person_info(name="李四", age=30, city="北京", job="工程师")
person_info()  # 也可以不传参数
```

输出：

```
接收到的参数: {'name': '张三', 'age': 25}, 类型: <class 'dict'>
name: 张三
age: 25
```



###### 2.5.1.5.3 混合使用：位置参数 + 可变参数

```python
def student_info(name, age, *scores, **extras):
    """混合使用各种参数"""
    print(f"姓名: {name}")
    print(f"年龄: {age}")
    print(f"成绩: {scores}")
    print(f"其他信息: {extras}")

# 测试
student_info("张三", 18, 90, 85, 92, city="北京", hobby="篮球")
```

输出：

```
姓名: 张三
年龄: 18
成绩: (90, 85, 92)
其他信息: {'city': '北京', 'hobby': '篮球'}
```



###### 2.5.1.5.4 实际应用示例

**示例1：日志函数**

```python
def log_message(level, *messages, **options):
    """灵活的日志记录函数"""
    timestamp = options.get('timestamp', '未知时间')
    print(f"[{level}] {timestamp}: ", end="")
    for msg in messages:
        print(msg, end=" ")
    print()

log_message("INFO", "系统启动", "一切正常")
log_message("ERROR", "数据库连接失败", "请检查配置", timestamp="2024-01-01 10:00:00")
```



**示例2：配置函数**

```python
def create_config(**settings):
    """创建配置字典"""
    default_config = {
        'host': 'localhost',
        'port': 8080,
        'debug': False
    }
    # 用传入的参数更新默认配置
    default_config.update(settings)
    return default_config

config1 = create_config()
config2 = create_config(host='192.168.1.1', port=9000)
config3 = create_config(debug=True, timeout=30)

print(config1)
print(config2)
print(config3)
```



###### 2.5.1.5.5 解包参数

```python
def introduce(name, age, city):
    print(f"我叫{name}，今年{age}岁，来自{city}")

# 正常调用
introduce("张三", 25, "北京")

# 使用解包
person = ("李四", 30, "上海")
introduce(*person)  # 解包元组

info = {"name": "王五", "age": 28, "city": "广州"}
introduce(**info)   # 解包字典
```



###### 2.5.1.5.6 参数顺序规则

正确的参数顺序：

```python
def correct_order(required1, required2, *args, default1="默认1", default2="默认2", **kwargs):
    """展示正确的参数顺序"""
    print(f"必需参数: {required1}, {required2}")
    print(f"可变位置参数 *args: {args}")
    print(f"默认参数: {default1}, {default2}")
    print(f"可变关键字参数 **kwargs: {kwargs}")
    print("-" * 40)
    
correct_order("值1", "值2", default1="新默认1", default2="新默认2")
correct_order("值1", "值2", name="张三", age=25, city="北京")
```



**实际应用示例：**

```python
def send_email(to, subject, *attachments, cc=None, bcc=None, **headers):
    """发送邮件函数"""
    print(f"收件人: {to}")
    print(f"主题: {subject}")
    print(f"附件: {attachments}")
    print(f"抄送: {cc}")
    print(f"密送: {bcc}")
    print(f"其他头信息: {headers}")

# 使用示例
send_email("user@example.com", "测试邮件", "file1.pdf", "file2.jpg",
           cc="boss@example.com", priority="high", reply_to="admin@example.com")
```

输出结果：

```
收件人: user@example.com
主题: 测试邮件
附件: ('file1.pdf', 'file2.jpg')
抄送: boss@example.com
密送: None
其他头信息: {'priority': 'high', 'reply_to': 'admin@example.com'}
```



**记忆口诀：**

- 必需参数 → `*args` → 默认参数 → `**kwargs`

###### 2.5.1.5.7 总结

**可变参数的优势：**

- 灵活性：可以处理不确定数量的参数
- 可读性：使用关键字参数时代码更清晰
- 扩展性：函数接口更容易扩展

**使用场景：**

- 数学运算（如求和、求平均）
- 日志记录
- 配置管理
- 包装器函数
- API调用





##### 2.5.1.6 用模块管理函数

不管用什么样的编程语言来写代码，给变量、函数起名字都是一个让人头疼的问题，因为我们会遇到**命名冲突**这种尴尬的情况。最简单的场景就是在同一个`.py`文件中定义了两个同名的函数，如下所示

~~~python
def foo():
    print('hello, world!')


def foo():
    print('goodbye, world!')

    
foo()    # 大家猜猜调用foo函数会输出什么
~~~

当然上面的这种情况我们很容易就能避免，但是如果项目是团队协作多人开发的时候，团队中可能有多个程序员都定义了名为`foo`的函数，这种情况下怎么解决命名冲突呢？答案其实很简单，Python中每个文件就代表了一个模块（module），我们在不同的模块中可以有同名的函数，在使用函数的时候我们通过`import`关键字导入指定的模块再使用**完全限定名**的调用方式就可以区分到底要使用的是哪个模块中的`foo`函数，代码如下所示。

`module1.py`

```
def foo():
    print('hello, world!')
```

`module2.py`

```
def foo():
    print('goodbye, world!')
```

`test.py`

```
import module1
import module2

# 用“模块名.函数名”的方式（完全限定名）调用函数，
module1.foo()    # hello, world!
module2.foo()    # goodbye, world!
```



在导入模块时，还可以使用`as`关键字对模块进行别名，这样我们可以使用更为简短的完全限定名。

`test.py`

~~~python
import module1 as m1
import module2 as m2

m1.foo()    # hello, world!
m2.foo()    # goodbye, world!
~~~



上面的代码我们导入了定义函数的模块，我们也可以使用`from...import...`语法从模块中直接导入需要使用的函数，代码如下所示。

`test.py`

~~~python
from module1 import foo

foo()    # hello, world!

from module2 import foo

foo()    # goodbye, world!
~~~

但是，如果我们如果从两个不同的模块中导入了同名的函数，后导入的函数会覆盖掉先前的导入，就像下面的代码中，调用`foo`会输出`hello, world!`，因为我们先导入了`module2`的`foo`，后导入了`module1`的`foo` 。如果两个`from...import...`反过来写，就是另外一番光景了。

`test.py`

```python
from module2 import foo
from module1 import foo

foo()    # hello, world!
```



如果想在上面的代码中同时使用来自两个模块中的`foo`函数也是有办法的，大家可能已经猜到了，还是用`as`关键字对导入的函数进行别名，代码如下所示。

`test.py`

```python
from module1 import foo as f1
from module2 import foo as f2

f1()    # hello, world!
f2()    # goodbye, world!
```



##### 2.5.1.7 标准库中的模块和函数



Python标准库中提供了大量的模块和函数来简化我们的开发工作，我们之前用过的`random`模块就为我们提供了生成随机数和进行随机抽样的函数；而`time`模块则提供了和时间操作相关的函数；上面求阶乘的函数在Python标准库中的`math`模块中已经有了，实际开发中并不需要我们自己编写，而`math`模块中还包括了计算正弦、余弦、指数、对数等一系列的数学函数。随着我们进一步的学习Python编程知识，我们还会用到更多的模块和函数。

Python标准库中还有一类函数是不需要`import`就能够直接使用的，我们将其称之为内置函数，这些内置函数都是很有用也是最常用的，下面的表格列出了一部分的内置函数。



| 函数    | 说明                                                         |
| ------- | ------------------------------------------------------------ |
| `abs`   | 返回一个数的绝对值，例如：`abs(-1.3)`会返回`1.3`。           |
| `bin`   | 把一个整数转换成以`'0b'`开头的二进制字符串，例如：`bin(123)`会返回`'0b1111011'`。 |
| `chr`   | 将Unicode编码转换成对应的字符，例如：`chr(8364)`会返回`'€'`。 |
| `hex`   | 将一个整数转换成以`'0x'`开头的十六进制字符串，例如：`hex(123)`会返回`'0x7b'`。 |
| `input` | 从输入中读取一行，返回读到的字符串。                         |
| `len`   | 获取字符串、列表等的长度。                                   |
| `max`   | 返回多个参数或一个可迭代对象中的最大值，例如：`max(12, 95, 37)`会返回`95`。 |
| `min`   | 返回多个参数或一个可迭代对象中的最小值，例如：`min(12, 95, 37)`会返回`12`。 |
| `oct`   | 把一个整数转换成以`'0o'`开头的八进制字符串，例如：`oct(123)`会返回`'0o173'`。 |
| `open`  | 打开一个文件并返回文件对象。                                 |
| `ord`   | 将字符转换成对应的Unicode编码，例如：`ord('€')`会返回`8364`。 |
| `pow`   | 求幂运算，例如：`pow(2, 3)`会返回`8`；`pow(2, 0.5)`会返回`1.4142135623730951`。 |
| `print` | 打印输出。                                                   |
| `range` | 构造一个范围序列，例如：`range(100)`会产生`0`到`99`的整数序列。 |
| `round` | 按照指定的精度对数值进行四舍五入，例如：`round(1.23456, 4)`会返回`1.2346`。 |
| `sum`   | 对一个序列中的项从左到右进行求和运算，例如：`sum(range(1, 101))`会返回`5050`。 |
| `type`  | 返回对象的类型，例如：`type(10)`会返回`int`；而` type('hello')`会返回`str`。 |



**简单的总结**

**函数是对功能相对独立且会重复使用的代码的封装**。学会使用定义和使用函数，就能够写出更为优质的代码。当然，Python语言的标准库中已经为我们提供了大量的模块和常用的函数，用好这些模块和函数就能够用更少的代码做更多的事情；如果这些模块和函数不能满足我们的要求，我们就需要自定义函数，然后用模块的概念来管理这些自定义函数。





#### 2.5.2 函数的应用

接下来我们通过一些案例来为大家讲解函数的应用。

##### 2.5.2.1 生成验证码的函数

###### 案例1：设计一个生成验证码的函数。

> **说明**：验证码由数字和英文大小写字母构成，长度可以用参数指定。

~~~python
import random
import string

ALL_CHARS = string.digits + string.ascii_letters


def generate_code(code_len=4):
    """生成指定长度的验证码
    
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码字符串
    """
    return ''.join(random.choices(ALL_CHARS, k=code_len))

for _ in range(10):
    print(generate_code()) 
~~~





> **说明1**：`string`模块的`digits`代表0到9的数字构成的字符串`'0123456789'`，`string`模块的`ascii_letters`代表大小写英文字母构成的字符串`'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'`。
>
> **说明**：`random`模块的`sample`和`choices`函数都可以实现随机抽样，`sample`实现无放回抽样，这意味着抽样取出的字符是不重复的；`choices`实现有放回抽样，这意味着可能会重复选中某些字符。这两个函数的第一个参数代表抽样的总体，而参数`k`代表抽样的数量。







###### 案例2：基础版本 --> 数字+大小写字母

~~~python
import random
import string

def generate_captcha(length=4):
    """生成指定长度的验证码（包含数字和大小写字母）"""
    # 定义字符池：数字 + 小写字母 + 大写字母
    characters = string.digits + string.ascii_letters
    # 随机选择指定长度的字符
    captcha = ''.join(random.choice(characters) for _ in range(length))
    return captcha

# 测试
print("默认长度验证码:", generate_captcha())           # 默认4位
print("6位验证码:", generate_captcha(6))              # 6位
print("8位验证码:", generate_captcha(8))              # 8位
~~~



###### 案例3：增强版本 --> 支持自定义字符类型

~~~python
import random
import string

def generate_advanced_captcha(length=4, use_digits=True, use_lowercase=True, use_uppercase=True):
    """
    生成高级验证码
    
    参数:
    length: 验证码长度
    use_digits: 是否包含数字
    use_lowercase: 是否包含小写字母  
    use_uppercase: 是否包含大写字母
    """
    # 构建字符池
    char_pool = ""
    if use_digits:
        char_pool += string.digits
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_uppercase:
        char_pool += string.ascii_uppercase
    
    # 检查字符池是否为空
    if not char_pool:
        raise ValueError("至少选择一种字符类型！")
    
    # 生成验证码
    captcha = ''.join(random.choice(char_pool) for _ in range(length))
    return captcha

# 测试各种组合
print("纯数字验证码:", generate_advanced_captcha(6, use_lowercase=False, use_uppercase=False))
print("纯小写字母:", generate_advanced_captcha(6, use_digits=False, use_uppercase=False))
print("纯大写字母:", generate_advanced_captcha(6, use_digits=False, use_lowercase=False))
print("数字+小写:", generate_advanced_captcha(6, use_uppercase=False))
print("完整验证码:", generate_advanced_captcha(8))
~~~



###### 案例4：专业版本 --> 排除容易混淆的字符

~~~python
import random
import string

def generate_pro_captcha(length=4, exclude_similar=True):
    """
    生成专业验证码，可排除容易混淆的字符
    
    参数:
    length: 验证码长度
    exclude_similar: 是否排除容易混淆的字符 (0Oo1lI)
    """
    # 容易混淆的字符
    similar_chars = "0Oo1lI"
    
    # 基础字符池
    char_pool = string.digits + string.ascii_letters
    
    if exclude_similar:
        # 排除容易混淆的字符
        char_pool = ''.join(c for c in char_pool if c not in similar_chars)
    
    # 检查字符池长度
    if len(char_pool) < 4:
        raise ValueError("字符池太小，请减少排除的字符或关闭exclude_similar选项")
    
    # 生成验证码
    captcha = ''.join(random.choice(char_pool) for _ in range(length))
    return captcha

# 测试
print("普通验证码:", generate_pro_captcha(6, exclude_similar=False))
print("排除混淆字符:", generate_pro_captcha(6, exclude_similar=True))
~~~



###### 案例5：批量生成版本

~~~python
import random
import string

def generate_captcha_batch(count=5, length=4, char_type="all"):
    """
    批量生成验证码
    
    参数:
    count: 生成数量
    length: 每个验证码长度
    char_type: 字符类型 ('digits', 'letters', 'all')
    """
    # 定义字符池
    if char_type == "digits":
        char_pool = string.digits
    elif char_type == "letters":
        char_pool = string.ascii_letters
    else:  # all
        char_pool = string.digits + string.ascii_letters
    
    captchas = []
    for i in range(count):
        captcha = ''.join(random.choice(char_pool) for _ in range(length))
        captchas.append(captcha)
    
    return captchas

# 测试批量生成
print("5个数字验证码:", generate_captcha_batch(5, 4, "digits"))
print("3个字母验证码:", generate_captcha_batch(3, 6, "letters"))
print("4个混合验证码:", generate_captcha_batch(4, 5, "all"))
~~~





###### 案例6：使用示例和输出

~~~python
import random
import string

def generate_captcha(length=4):
    """生成指定长度的验证码（包含数字和大小写字母）"""
    # 定义字符池：数字 + 小写字母 + 大写字母
    characters = string.digits + string.ascii_letters
    # 随机选择指定长度的字符
    captcha = ''.join(random.choice(characters) for _ in range(length))
    return captcha

def generate_advanced_captcha(length=4, use_digits=True, use_lowercase=True, use_uppercase=True):
    """
    生成高级验证码
    
    参数:
    length: 验证码长度
    use_digits: 是否包含数字
    use_lowercase: 是否包含小写字母  
    use_uppercase: 是否包含大写字母
    """
    # 构建字符池
    char_pool = ""
    if use_digits:
        char_pool += string.digits
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_uppercase:
        char_pool += string.ascii_uppercase
    
    # 检查字符池是否为空
    if not char_pool:
        raise ValueError("至少选择一种字符类型！")
    
    # 生成验证码
    captcha = ''.join(random.choice(char_pool) for _ in range(length))
    return captcha

def generate_pro_captcha(length=4, exclude_similar=True):
    """
    生成专业验证码，可排除容易混淆的字符
    
    参数:
    length: 验证码长度
    exclude_similar: 是否排除容易混淆的字符 (0Oo1lI)
    """
    # 容易混淆的字符
    similar_chars = "0Oo1lI"
    
    # 基础字符池
    char_pool = string.digits + string.ascii_letters
    
    if exclude_similar:
        # 排除容易混淆的字符
        char_pool = ''.join(c for c in char_pool if c not in similar_chars)
    
    # 检查字符池长度
    if len(char_pool) < 4:
        raise ValueError("字符池太小，请减少排除的字符或关闭exclude_similar选项")
    
    # 生成验证码
    captcha = ''.join(random.choice(char_pool) for _ in range(length))
    return captcha

def generate_captcha_batch(count=5, length=4, mode="all"):
    """
    批量生成验证码
    
    参数:
    count: 生成验证码的数量
    length: 每个验证码的长度
    mode: 验证码类型 ("digits", "letters", "all")
    """
    captchas = []
    
    for _ in range(count):
        if mode == "digits":
            captcha = ''.join(random.choice(string.digits) for _ in range(length))
        elif mode == "letters":
            captcha = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        else:  # "all"
            captcha = generate_captcha(length)
        captchas.append(captcha)
    
    return captchas

# 综合测试
if __name__ == "__main__":
    print("=== 验证码生成器测试 ===")
    
    # 基础功能
    print("\n1. 基础验证码:")
    for i in range(3):
        print(f"  验证码 {i+1}: {generate_captcha(4)}")
    
    # 高级功能
    print("\n2. 高级验证码:")
    print(f"  纯数字: {generate_advanced_captcha(4, use_lowercase=False, use_uppercase=False)}")
    print(f"  数字+大写: {generate_advanced_captcha(4, use_lowercase=False)}")
    print(f"  完整版: {generate_advanced_captcha(8)}")
    
    # 专业版
    print("\n3. 专业验证码:")
    print(f"  包含混淆字符: {generate_pro_captcha(6, exclude_similar=False)}")
    print(f"  排除混淆字符: {generate_pro_captcha(6, exclude_similar=True)}")
    
    # 批量生成
    print("\n4. 批量验证码:")
    batch = generate_captcha_batch(5, 4, "all")
    for i, code in enumerate(batch, 1):
        print(f"  第{i}个: {code}")
    
    print("5个数字验证码:", generate_captcha_batch(5, 4, "digits"))
    print("3个字母验证码:", generate_captcha_batch(3, 6, "letters"))
    print("4个混合验证码:", generate_captcha_batch(4, 5, "all"))
~~~



输出结果：

```
=== 验证码生成器测试 ===

1. 基础验证码:
  验证码 1: 0VzZ
  验证码 2: gUCf
  验证码 3: wizp

2. 高级验证码:
  纯数字: 0103
  数字+大写: FG6Q
  完整版: Fq9NrTQW

3. 专业验证码:
  包含混淆字符: bQJFaf
  排除混淆字符: CnPVfN

4. 批量验证码:
  第1个: rz11
  第2个: m0jM
  第3个: 5dYH
  第4个: KUCu
  第5个: yob3
5个数字验证码: ['6683', '2858', '6894', '4709', '6463']
3个字母验证码: ['VtUuxM', 'nYpAte', 'VWbuFF']
4个混合验证码: ['vyL5P', 'H1Jkw', 'UvdC1', 'Ustl9']
```



##### 2.5.2.2 设定文件的后缀名

###### 案例1：设计一个函数返回给定文件的后缀名

> **说明**：文件名通常是一个字符串，而文件的后缀名指的是文件名中最后一个`.`后面的部分，也称为文件的扩展名，它是某些操作系统用来标记文件类型的一种机制，例如在Windows系统上，后缀名`exe`表示这是一个可执行程序，而后缀名`txt`表示这是一个纯文本文件。需要注意的是，在Linux和macOS系统上，文件名可以以`.`开头，表示这是一个隐藏文件，像`.gitignore`这样的文件名，`.`后面并不是后缀名，这个文件没有后缀名或者说后缀名为`''`

~~~python
def get_suffix(filename, ignore_dot=True):
    """获取文件名的后缀名
    
    :param filename: 文件名
    :param ignore_dot: 是否忽略后缀名前面的点
    :return: 文件的后缀名
    """
    # 从字符串中逆向查找.出现的位置
    pos = filename.rfind('.')
    # 通过切片操作从文件名中取出后缀名
    if pos <= 0:
        return ''
    return filename[pos + 1:] if ignore_dot else filename[pos:]
~~~



可以用下面的代码对上面的函数做一个简单的测验。

```
print(get_suffix('readme.txt'))       # txt
print(get_suffix('readme.txt.md'))    # md
print(get_suffix('.readme'))          #
print(get_suffix('readme.'))          #
print(get_suffix('readme'))           #
```

上面的`get_suffix`函数还有一个更为便捷的实现方式，就是直接使用`os.path`模块的`splitext`函数，这个函数会将文件名拆分成带路径的文件名和扩展名两个部分，然后返回一个二元组，二元组中的第二个元素就是文件的后缀名（包含`.`），如果要去掉后缀名中的`.`，可以做一个字符串的切片操作，代码如下所示。





```python
# 基础版本
def get_file_extension(filename):
    """
    获取文件后缀名
    
    参数:
    filename: 文件名或文件路径
    
    返回:
    文件后缀名（包含点号），如果没有后缀则返回空字符串
    """
    # 使用字符串的rpartition方法从右边分割
    _, dot, extension = filename.rpartition('.')
    
    if dot == '.':
        return dot + extension
    else:
        return ""
    
    
# 增强版本（推荐）    
import os

def get_file_extension_enhanced(filename, with_dot=True, to_lower=False):
    """
    获取文件后缀名（增强版）
    
    参数:
    filename: 文件名或文件路径
    with_dot: 是否包含点号
    to_lower: 是否转换为小写
    
    返回:
    文件后缀名
    """
    # 使用os.path.splitext获取后缀名
    _, ext = os.path.splitext(filename)
    
    # 处理是否包含点号
    if not with_dot and ext.startswith('.'):
        ext = ext[1:]
    
    # 处理大小写
    if to_lower:
        ext = ext.lower()
    
    return ext

# 安全版本（处理特殊情况）
import os

def get_file_extension_safe(filename, with_dot=True, to_lower=False, default=""):
    """
    安全获取文件后缀名
    
    参数:
    filename: 文件名或文件路径
    with_dot: 是否包含点号
    to_lower: 是否转换为小写
    default: 没有后缀时的默认返回值
    
    返回:
    文件后缀名或默认值
    """
    if not filename or not isinstance(filename, str):
        return default
    
    # 获取基础文件名（去掉路径）
    basename = os.path.basename(filename)
    
    # 分割文件名和后缀
    name, ext = os.path.splitext(basename)
    
    # 如果没有后缀或文件名以点开头（如 .gitignore）
    if not ext or (not name and ext):
        return default
    
    # 处理是否包含点号
    if not with_dot and ext.startswith('.'):
        ext = ext[1:]
    
    # 处理大小写
    if to_lower:
        ext = ext.lower()
    
    return ext

# 测试各种情况
if __name__ == "__main__":
    test_cases = [
        "document.pdf",
        "image.jpg",
        "script.py",
        "archive.tar.gz",  # 多重扩展
        "README",          # 无扩展名
        ".hidden",         # 隐藏文件
        "path/to/file.txt", # 包含路径
        "UPPERCASE.PNG",   # 大写
        "file.with.multiple.dots.txt",
        "",                # 空字符串
        "no_extension",    # 无扩展名
    ]
    
    print("=== 文件后缀名测试 ===")
    
    for filename in test_cases:
        # 基础版本
        ext1 = get_file_extension(filename)
        
        # 增强版本（推荐）
        ext2 = get_file_extension_enhanced(filename, with_dot=False)
        
        # 安全版本（处理特殊情况）
        ext3 = get_file_extension_safe(filename, with_dot=False)
        
        print(f"文件: {filename:30} | 基础版: {ext1:8} | 增强版: {ext2:8} | 安全版: {ext3:8}")    
```





##### 2.5.2.3 判断素数

设计一个判断给定的大于1的正整数是不是质数的函数。质数是只能被1和自身整除的正整数（大于1），如果一个大于 1 的正整数 N 是质数，那就意味着在 2 到 N−1 之间都没有它的因子。

> 在数学中，**"质数"** 和 **"素数"** 是同一个概念，只是叫法不同。



~~~python
def is_prime(num: int) -> bool:
    """
    判断一个正整数是不是质数
    :param num: 大于1的正整数
    :return: 如果num是质数返回True，否则返回False
    """
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
~~~

> **说明1**：上面`is_prime`函数的参数`num`后面的`: int`用来标注参数的类型，虽然它对代码的执行结果不产生任何影响，但是很好的增强了代码的可读性。同理，参数列表后面的`-> bool`用来标注函数返回值的类型，它也不会对代码的执行结果产生影响，但是却让我们清楚的知道，调用函数会得到一个布尔值，要么是`True`，要么是`False`。
>
> **说明2**：上面的循环并不需要从 2 循环到 N−1 ，因为如果循环进行到 N 时，还没有找到$\small{N}$的因子，那么 N 之后也不会出现 N 的因子，大家可以自己想一想这是为什么。



~~~python
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
~~~



输出结果：

```
=== 素数判断 ===
1 -> 合数
2 -> 素数
3 -> 素数
4 -> 合数
16 -> 合数
17 -> 素数
25 -> 合数
97 -> 素数
100 -> 合数
101 -> 素数

=== 1-100的素数 ===
共找到 25 个素数:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

=== 性能测试 ===
性能测试:
  2: 素数
  3: 素数
  17: 素数
  100: 合数
  101: 素数
  1009: 素数
  7919: 素数
  10007: 素数
  999983: 素数
总耗时: 0.000000秒
```



> 这是一个 **三元条件表达式**（Ternary Conditional Expression），是 Python 中的一种简洁的条件赋值语法。
>
> - [ ] 语法结构 
>
>   ```
>   value_if_true if condition else value_if_false
>   ```
>
> - [ ] 代码分析 
>
>   ```python
>   # 三元条件表达式
>   status = "素数" if result else "合数"
>   
>   # 等价于：
>   
>   if result == True:
>       status = "素数"
>   else:
>       status = "合数"
>   ```
>
> - [ ] 举例说明 
>
>   ```python
>   # 示例1：num = 5
>   result = is_prime(5)  # 返回 True
>   status = "素数" if True else "合数"  # status = "素数"
>   
>   # 示例2：num = 6  
>   result = is_prime(6)  # 返回 False
>   status = "素数" if False else "合数"  # status = "合数"
>   ```
>
>   



##### 2.5.2.4 最大公约数和最小公倍数

设计计算两个正整数最大公约数和最小公倍数的函数。 x 和 y 的最大公约数是能够同时整除 x 和 y 的最大整数，如果 x 和 y 互质，那么它们的最大公约数为 1； x 和 y 的最小公倍数是能够同时被 x 和 y 整除的最小正整数，如果 x 和 y 互质，那么它们的最小公倍数为 x×y 。需要提醒大家注意的是，计算最大公约数和最小公倍数是两个不同的功能，应该设计成两个函数，而不是把两个功能放到同一个函数中。

~~~python
def lcm(x: int, y: int) -> int:
    """求最小公倍数"""
    return x * y // gcd(x, y)


def gcd(x: int, y: int) -> int:
    """求最大公约数"""
    while y % x != 0:
        x, y = y % x, x
    return x
~~~





######  一、定义对比

| 概念           | 英文                          | 含义                         | 举例             |
| -------------- | ----------------------------- | ---------------------------- | ---------------- |
| **最大公约数** | GCD (Greatest Common Divisor) | 能同时整除两个数的最大整数   | GCD(12, 18) = 6  |
| **最小公倍数** | LCM (Least Common Multiple)   | 能被两个数同时整除的最小整数 | LCM(12, 18) = 36 |



######  二、举个例子：

以 **12 和 18** 为例：

1️⃣ 公约数（能同时整除的数）：

- 12 的约数：1, 2, 3, 4, 6, 12
- 18 的约数：1, 2, 3, 6, 9, 18
- 公约数：1, 2, 3, 6
   👉 最大公约数 = **6**

2️⃣ 公倍数（能被两者整除的数）：

- 12 的倍数：12, 24, 36, 48, 60, 72 …
- 18 的倍数：18, 36, 54, 72, 90 …
- 公倍数：36, 72, 108 …
   👉 最小公倍数 = **36**



3️⃣ 举例子

~~~python
## 🧑‍💻 Python 验证代码：

```python
import math

a, b = 12, 18
gcd = math.gcd(a, b)
lcm = a * b // gcd

print("GCD =", gcd)
print("LCM =", lcm)
~~~



###### 三、GCD 与 LCM 的关系公式

有一个非常重要的数学关系式：

$$
a \times b = GCD(a, b) \times LCM(a, b)
$$

所以：

$$
LCM(a, b) = \frac{a \times b}{GCD(a, b)}
$$




###### 四、Python 代码实现

Python 里其实自带函数：

```
import math

a, b = 12, 18

gcd = math.gcd(a, b)
lcm = a * b // gcd

print("最大公约数 GCD =", gcd)
print("最小公倍数 LCM =", lcm)
```

输出：

```
最大公约数 GCD = 6
最小公倍数 LCM = 36
```





###### 五、原理小结

| 名称           | 条件                     | 示例（12,18） | 结果   |
| -------------- | ------------------------ | ------------- | ------ |
| 最大公约数 GCD | 能整除两数的**最大数**   | 1,2,3,6       | 6      |
| 最小公倍数 LCM | 能被两数整除的**最小数** | 36,72,…       | 36     |
| 关系           | `a * b = GCD * LCM`      | 12×18 = 6×36  | ✅ 成立 |





###### 六、记忆小技巧：

> 🧠 “约”表示能**除尽**，所以最大公约数越大越整齐；
>  💡 “倍”表示能**被整除**，所以最小公倍数越小越方便。







##### 2.5.2.5 数据统计

假设样本数据保存一个列表中，设计计算样本数据描述性统计信息的函数。描述性统计信息通常包括：算术平均值、中位数、极差（最大值和最小值的差）、方差、标准差、变异系数等，计算公式如下所示。



**样本均值（Sample Mean）**
$$
\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n} = \frac{x_1 + x_2 + \cdots + x_n}{n}
$$

**样本方差（Sample Variance）**
$$
s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n - 1}
$$

**样本标准差（Sample Standard Deviation）**
$$
s = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n - 1}}
$$

**变异系数（Coefficient of Variation）**
$$
CV = \frac{s}{\bar{x}}
$$


~~~python
import numpy as np

# 示例数据
data = [12, 18, 25, 30, 15]

# 计算统计量
mean_val = np.mean(data)           # 均值
median_val = np.median(data)       # 中位数
range_val = np.ptp(data)           # 极差（最大值-最小值）
var_val = np.var(data, ddof=1)     # 样本方差，ddof=1 表示除以 n-1
std_val = np.std(data, ddof=1)     # 样本标准差
cv_val = std_val / mean_val        # 变异系数

# 输出描述性统计信息
print(f'均值: {mean_val}')
print(f'中位数: {median_val}')
print(f'极差: {range_val}')
print(f'方差: {var_val}')
print(f'标准差: {std_val}')
print(f'变异系数: {cv_val:.2f}')
~~~



> Downloading numpy-2.3.4-cp311-cp311-win_amd64.whl (13.1 MB)     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.1/13.1 MB 3.4 MB/s eta 0:00:00 Installing collected packages: numpy  WARNING: Failed to write executable - trying to use .deleteme logic ERROR: Could not install packages due to an OSError: [WinError 2] 系统找不到指定的文件。: 'C:\\Python311\\Scripts\\f2py.exe' -> 'C:\\Python311\\Scripts\\f2py.exe.deleteme'  [notice] A new release of pip available: 22.3.1 -> 25.2 [notice] To update, run: python.exe -m pip install --upgrade pip



###### 1️⃣ 升级 pip（推荐）

你当前 pip 版本较旧（22.3.1），升级到最新版本可以解决很多安装问题：

```
python -m pip install --upgrade pip
```

升级完成后，再尝试安装 numpy：

```
python -m pip install numpy
```





###### 2️⃣ 使用管理员权限

在 **PowerShell 或 CMD** 里：

1. 右键 → “以管理员身份运行”
2. 执行安装命令：

```
python -m pip install numpy
```



###### 3️⃣ 使用 `--user` 安装（安装到用户目录，避免权限问题）

```
python -m pip install --user numpy
```

安装完成后，Python 会自动在用户目录下查找库。





###### 4️⃣ 如果依然失败：创建虚拟环境安装（最安全）

```
# 在项目目录下
python -m venv venv

# 激活虚拟环境 (Windows)
venv\Scripts\activate

# 安装 numpy
pip install numpy
```





##### 2.5.2.6 双色球随机选号

我们用函数重构之前讲过的双色球随机选号的例子（《第09课：常用数据结构之列表-2》），将生成随机号码和输出一组号码的功能分别封装到两个函数中，然后通过调用函数实现机选`N`注号码的功能。

~~~python
"""
双色球随机选号程序

Author: 骆昊
Version: 1.3
"""
import random

RED_BALLS = [i for i in range(1, 34)]
BLUE_BALLS = [i for i in range(1, 17)]


def choose():
    """
    生成一组随机号码
    :return: 保存随机号码的列表
    """
    selected_balls = random.sample(RED_BALLS, 6)
    selected_balls.sort()
    selected_balls.append(random.choice(BLUE_BALLS))
    return selected_balls


def display(balls):
    """
    格式输出一组号码
    :param balls: 保存随机号码的列表
    """
    for ball in balls[:-1]:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    print(f'\033[034m{balls[-1]:0>2d}\033[0m')


n = int(input('生成几注号码: '))
for _ in range(n):
    display(choose())
~~~







双色球规则回顾：

- **红球**：从 1~35 中选 5 个（或 6 个，部分玩法不同，这里按 6 个）
- **蓝球**：从 1~17 中选 2 个（或 1 个，常规玩法是 1 个）
- 红球不能重复，蓝球也不能重复

~~~python
import random

def generate_double_color_ball():
    # 红球 1~33，选6个
    red_balls = random.sample(range(1, 34), 6)
    red_balls.sort()  # 排序更美观
    
    # 蓝球 1~16，选1个
    blue_ball = random.choice(range(1, 17))
    
    return red_balls, blue_ball

# 生成一注号码
red, blue = generate_double_color_ball()
print(f"红球: {red}, 蓝球: {blue}")
~~~



输出结果：

```
红球: [11, 13, 15, 16, 20, 22], 蓝球: 7
```



如果题目要求蓝球从 1~12 中选 2 个（自定义玩法）

~~~python
def generate_custom_double_color_ball():
    red_balls = random.sample(range(1, 34), 6)
    red_balls.sort()
    
    blue_balls = random.sample(range(1, 13), 2)
    blue_balls.sort()
    
    return red_balls, blue_balls

red, blue = generate_custom_double_color_ball()
print(f"红球: {red}, 蓝球: {blue}")
~~~





| 函数     | 返回结果 | 是否允许重复         | 用途       |
| -------- | -------- | -------------------- | ---------- |
| `choice` | 单个元素 | 可以重复（多次调用） | 随机抽一个 |
| `sample` | 列表     | 不重复               | 随机抽多个 |



##### 2.5.2.7 总结

在写代码尤其是开发商业项目的时候，一定要有意识的**将相对独立且重复使用的功能封装成函数**，这样不管是自己还是团队的其他成员都可以通过调用函数的方式来使用这些功能，减少工作中那些重复且乏味的劳动。



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



























































