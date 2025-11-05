# 学生名单
names = ['关羽', '张飞', '赵云', '马超', '黄忠']

# 课程名单
courses = ['语文', '数学', '英语']

# 创建一个二维列表，用于存储每个学生每门课程的成绩
# 使用列表推导式保证每一行都是独立的列表，避免共享引用
# scores = [[None] * len(courses)] * len(names) # 这种写法是有问题

# scores = [[None] * len(courses) for i in range(len(names))]
scores = [[None] * len(courses) for _ in range(len(names))]

# 遍历每个学生的索引和姓名
for row, name in enumerate(names):
    # 遍历每门课程的索引和课程名
    for col, course in enumerate(courses):
        # 提示用户输入当前学生当前课程的成绩，并转换为浮点数
        scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
        # 打印当前二维列表的状态，方便调试和观察输入的变化
        print(scores)
