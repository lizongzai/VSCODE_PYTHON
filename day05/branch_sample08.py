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
