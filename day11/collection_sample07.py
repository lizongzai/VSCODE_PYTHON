group1 = {"math", "physics", "chemistry"}
group2 = {"biology", "physics", "history"}

# 检查是否有共同元素
has_common = any(subject in group2 for subject in group1)
print(f"有共同科目: {has_common}")  # True

# 找到具体共同元素
common_subjects = {subject for subject in group1 if subject in group2}
print(f"共同科目: {common_subjects}")  # {'physics'}