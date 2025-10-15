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
