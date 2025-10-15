import random
import string

def generate_pro_captcha(length=4, exclude_similar=True):
    """
    生成专业验证码，可排除容易混淆的字符
    
    参数:
    length: 验证码长度
    exclude_similar: 是否排除容易混淆的字符 (0Oo1lI)
    """
    # 容易混淆的字符
    similar_chars = "0Oo1lI"
    
    # 基础字符池
    char_pool = string.digits + string.ascii_letters
    
    if exclude_similar:
        # 排除容易混淆的字符
        char_pool = ''.join(c for c in char_pool if c not in similar_chars)
    
    # 检查字符池长度
    if len(char_pool) < 4:
        raise ValueError("字符池太小，请减少排除的字符或关闭exclude_similar选项")
    
    # 生成验证码
    captcha = ''.join(random.choice(char_pool) for _ in range(length))
    return captcha

# 测试
print("普通验证码:", generate_pro_captcha(6, exclude_similar=False))
print("排除混淆字符:", generate_pro_captcha(6, exclude_similar=True))