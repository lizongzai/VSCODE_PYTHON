import random
import string

def generate_captcha(length=4):
    """生成指定长度的验证码（包含数字和大小写字母）"""
    # 定义字符池：数字 + 小写字母 + 大写字母
    characters = string.digits + string.ascii_letters
    # 随机选择指定长度的字符
    captcha = ''.join(random.choice(characters) for _ in range(length))
    return captcha

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

def generate_captcha_batch(count=5, length=4, mode="all"):
    """
    批量生成验证码
    
    参数:
    count: 生成验证码的数量
    length: 每个验证码的长度
    mode: 验证码类型 ("digits", "letters", "all")
    """
    captchas = []
    
    for _ in range(count):
        if mode == "digits":
            captcha = ''.join(random.choice(string.digits) for _ in range(length))
        elif mode == "letters":
            captcha = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        else:  # "all"
            captcha = generate_captcha(length)
        captchas.append(captcha)
    
    return captchas

# 综合测试
if __name__ == "__main__":
    print("=== 验证码生成器测试 ===")
    
    # 基础功能
    print("\n1. 基础验证码:")
    for i in range(3):
        print(f"  验证码 {i+1}: {generate_captcha(4)}")
    
    # 高级功能
    print("\n2. 高级验证码:")
    print(f"  纯数字: {generate_advanced_captcha(4, use_lowercase=False, use_uppercase=False)}")
    print(f"  数字+大写: {generate_advanced_captcha(4, use_lowercase=False)}")
    print(f"  完整版: {generate_advanced_captcha(8)}")
    
    # 专业版
    print("\n3. 专业验证码:")
    print(f"  包含混淆字符: {generate_pro_captcha(6, exclude_similar=False)}")
    print(f"  排除混淆字符: {generate_pro_captcha(6, exclude_similar=True)}")
    
    # 批量生成
    print("\n4. 批量验证码:")
    batch = generate_captcha_batch(5, 4, "all")
    for i, code in enumerate(batch, 1):
        print(f"  第{i}个: {code}")
    
    print("5个数字验证码:", generate_captcha_batch(5, 4, "digits"))
    print("3个字母验证码:", generate_captcha_batch(3, 6, "letters"))
    print("4个混合验证码:", generate_captcha_batch(4, 5, "all"))