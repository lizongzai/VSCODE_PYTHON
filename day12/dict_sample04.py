sentence = input('请输入一段话: ')
counter = {}
for ch in sentence:
    if ch.isalpha():  # 更Pythonic的判断方式
        ch_lower = ch.lower()  # 转换为小写
        counter[ch_lower] = counter.get(ch_lower, 0) + 1

for key, value in counter.items():
    print(f'字母{key}出现了{value}次.')