from collections import Counter

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
c = Counter(words)

print(c)           # Counter({'apple': 3, 'banana': 2, 'orange': 1})
print(c.most_common(2))  # [('apple', 3), ('banana', 2)]