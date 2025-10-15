import random
import string

def generate_captcha(length=4):
    """生成指定长度的验证码（包含数字和大小写字母）"""
    # 定义字符池：数字 + 小写字母 + 大写字母
    characters = string.digits + string.ascii_letters
    # 随机选择指定长度的字符
    captcha = ''.join(random.choice(characters) for _ in range(length))
    return captcha

# 测试
print("默认长度验证码:", generate_captcha())           # 默认4位
print("6位验证码:", generate_captcha(6))              # 6位
print("8位验证码:", generate_captcha(8))              # 8位