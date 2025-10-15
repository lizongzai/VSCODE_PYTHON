import random
import string

def generate_advanced_captcha(length=4, use_digits=True, use_lowercase=True, use_uppercase=True):
    """
    生成高级验证码
    
    参数:
    length: 验证码长度
    use_digits: 是否包含数字
    use_lowercase: 是否包含小写字母  
    use_uppercase: 是否包含大写字母
    """
    # 构建字符池
    char_pool = ""
    if use_digits:
        char_pool += string.digits
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_uppercase:
        char_pool += string.ascii_uppercase
    
    # 检查字符池是否为空
    if not char_pool:
        raise ValueError("至少选择一种字符类型！")
    
    # 生成验证码
    captcha = ''.join(random.choice(char_pool) for _ in range(length))
    return captcha

# 测试各种组合
print("纯数字验证码:", generate_advanced_captcha(6, use_lowercase=False, use_uppercase=False))
print("纯小写字母:", generate_advanced_captcha(6, use_digits=False, use_uppercase=False))
print("纯大写字母:", generate_advanced_captcha(6, use_digits=False, use_lowercase=False))
print("数字+小写:", generate_advanced_captcha(6, use_uppercase=False))
print("完整验证码:", generate_advanced_captcha(8))