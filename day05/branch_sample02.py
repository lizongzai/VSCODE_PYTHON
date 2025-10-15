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