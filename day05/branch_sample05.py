import webbrowser

# 获取成绩
score = int(input("请输入成绩（0-100）："))

# 计算等级
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

# 生成 HTML 内容
html_content = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>成绩等级评定</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
        }}
        #result {{
            font-size: 20px;
            color: #007acc;
        }}
    </style>
</head>
<body>
    <h2>成绩等级评定</h2>
    <div id="result">
        <p>您的成绩分数为：{score}</p>
        <p>您的成绩等级为：{grade}</p>
    </div>
</body>
</html>
"""

# 保存为 HTML 文件
html_file = "grade_result.html"
with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

# 自动在默认浏览器中打开
webbrowser.open(html_file)
