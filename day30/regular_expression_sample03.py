import re  # 导入正则表达式模块

def extract_china_mobile_numbers(text):
    """
    从文本中提取合法中国大陆手机号
    返回号码、起始位置、结束位置
    自动去重
    """

    # 定义正则表达式
    # (?<!\d)：手机号前面不能是数字（确保前边界）
    # 1[3-9]：以1开头，第二位匹配合法号段（3-9）
    # \d{9}：再跟9位数字，总计11位手机号
    # (?!\d)：手机号后面不能是数字（确保后边界）
    pattern = re.compile(r'(?<!\d)1[3-9]\d{9}(?!\d)')

    results = []  # 用来存储提取出的结果列表
    seen = set()  # 用 set 存储已出现手机号，实现去重

    # finditer() 函数返回所有匹配的迭代器
    for match in pattern.finditer(text):
        tel = match.group()  # 获取匹配的手机号字符串
        
        # 如果手机号未出现过，则进入分支
        if tel not in seen:
            results.append({
                "number": tel,       # 手机号
                "start": match.start(),  # 起始位置索引
                "end": match.end()       # 结束位置索引（不包含）
            })
            seen.add(tel)  # 标记该手机号已记录过，防止重复添加
    # print(seen)
    # print(results)
    return results  # 返回所有结果数据


# 主程序入口
if __name__ == "__main__":

    # 测试用文本，包括多个手机号与非手机号内容
    sentence = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也不是110或119，王大锤的手机号才是15600998765。'''

    # 调用提取手机号函数
    tels = extract_china_mobile_numbers(sentence)

    # 遍历结果，打印手机号和其在文本中的位置
    for item in tels:
        print(f"手机号: {item['number']} | 位置: {item['start']} - {item['end']}")
