import re  # 导入 Python 的正则表达式处理库

# 要进行敏感词过滤的原始文本
sentence = 'Oh, shit! 你是傻逼吗? Fuck you.'

# 使用 re.sub() 执行替换：
# 1. 'fuck|shit' → 匹配英文敏感词 fuck 或 shit
# 2. [傻煞沙][比笔逼叉缺吊碉雕] → 匹配中文脏话 "傻逼"/"煞笔"/"沙雕" 等
#    解释：两个字符构成
#    第一个字符集合：[傻 煞 沙]
#    第二个字符集合：[比 笔 逼 叉 缺 吊 碉 雕]
#    → 任意组合皆视为辱骂词
# flags=re.IGNORECASE → 忽略大小写，Fuck、FUCK、fuck 都能匹配
purified = re.sub(
    'fuck|shit|[傻煞沙][比笔逼叉缺吊碉雕]',
    '*',
    sentence,
    flags=re.IGNORECASE
)

# 打印过滤后的结果
print(purified)  # 输出：Oh, *! 你是*吗? * you.
