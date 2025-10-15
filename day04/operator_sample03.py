
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