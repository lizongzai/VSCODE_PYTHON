students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78}
]

print("=== 排序前 ===")
for student in students:
    print(f"{student['name']}: {student['score']}")

# 排序操作
sorted_students = sorted(students, key=lambda x: x['score'])

print("\n=== 排序后 ===")
for student in sorted_students:
    print(f"{student['name']}: {student['score']}")