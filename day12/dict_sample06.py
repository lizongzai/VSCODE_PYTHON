sentence = input('请输入一段话: ')
counter = {}
for ch in sentence:
    if ch.isalpha():
        counter[ch] = counter.get(ch, 0) + 1

# 按字母顺序排序输出
for key in sorted(counter.keys()):
    print(f'字母{key}出现了{counter[key]}次.')