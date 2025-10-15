from collections import defaultdict

sentence = input('请输入一段话: ')
counter = defaultdict(int)  # 默认值为0

for ch in sentence:
    if ch.isalpha():
        counter[ch] += 1  # 不需要get()方法了

for key, value in counter.items():
    print(f'字母{key}出现了{value}次.')