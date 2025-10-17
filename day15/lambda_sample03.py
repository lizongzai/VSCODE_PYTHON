students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78}
]

# 按分数排序
sorted_students = sorted(students, key=lambda x: x['score'])
for student in sorted_students:
    print(f"{student['name']}: {student['score']}")