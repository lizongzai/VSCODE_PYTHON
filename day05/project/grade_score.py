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

# 读取 HTML 模板
with open("C:/Users/86181/Desktop/Vscode_python/day05/project/template.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# 替换占位符
html_content = html_content.replace("{{score}}", str(score))
html_content = html_content.replace("{{grade}}", grade)

# 保存生成的 HTML
html_file = "grade_result.html"
with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

# 打开浏览器
webbrowser.open(html_file)
