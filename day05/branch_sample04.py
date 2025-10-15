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
