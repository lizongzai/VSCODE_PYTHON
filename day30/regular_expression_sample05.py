import re  # 导入正则表达式模块

# 原始诗句字符串
poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'

# 使用正则表达式 split，把字符串按中文标点符号“，”和“。”分割
sentences_list = re.split(r'[，。]', poem)

# 去掉分割后产生的空字符串（因为句末会多一个标点）
sentences_list = [sentence for sentence in sentences_list if sentence]

# 遍历列表并打印每一句诗
for sentence in sentences_list:
    print(sentence)
