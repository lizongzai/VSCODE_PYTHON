# 写入文件（覆盖）
with open('example.txt', 'w', encoding='utf-8') as file:
    file.write('Hello, World!\n')
    file.write('This is a new line.\n')

# 追加内容
with open('example.txt', 'a', encoding='utf-8') as file:
    file.write('This line is appended.\n')