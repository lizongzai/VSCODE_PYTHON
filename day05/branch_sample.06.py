import webbrowser

score = int(input("请输入成绩（0-100）："))

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

html_content = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>成绩等级评定</title>
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
</style>
</head>
<body>
<div class="card">
<h2>成绩等级评定</h2>
<p>您的成绩分数为：{score}</p>
<p>您的成绩等级为：{grade}</p>
</div>
</body>
</html>
"""

with open("grade_result.html", "w", encoding="utf-8") as f:
    f.write(html_content)

webbrowser.open("grade_result.html")
