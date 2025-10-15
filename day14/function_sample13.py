import string
import random

def generate_captcha(length=4):
    """生成验证码"""
    # 创建字符池：数字 + 大小写字母
    characters = string.digits + string.ascii_letters
    
    print(f"使用的字符池: {characters}")
    print(f"字符池长度: {len(characters)}")  # 10数字 + 26小写 + 26大写 = 62个字符
    
    # 生成验证码
    captcha = ''.join(random.choice(characters) for _ in range(length))
    return captcha

# 测试
code = generate_captcha(6)
print(f"生成的验证码: {code}")