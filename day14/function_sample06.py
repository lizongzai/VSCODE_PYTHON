import random
import string

def generate_captcha_batch(count=5, length=4, char_type="all"):
    """
    批量生成验证码
    
    参数:
    count: 生成数量
    length: 每个验证码长度
    char_type: 字符类型 ('digits', 'letters', 'all')
    """
    # 定义字符池
    if char_type == "digits":
        char_pool = string.digits
    elif char_type == "letters":
        char_pool = string.ascii_letters
    else:  # all
        char_pool = string.digits + string.ascii_letters
    
    captchas = []
    for i in range(count):
        captcha = ''.join(random.choice(char_pool) for _ in range(length))
        captchas.append(captcha)
    
    return captchas

# 测试批量生成
print("5个数字验证码:", generate_captcha_batch(5, 4, "digits"))
print("3个字母验证码:", generate_captcha_batch(3, 6, "letters"))
print("4个混合验证码:", generate_captcha_batch(4, 5, "all"))