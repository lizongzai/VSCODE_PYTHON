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
