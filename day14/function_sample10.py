import os

def get_file_extension_safe(filename, with_dot=True, to_lower=False, default=""):
    """
    安全获取文件后缀名
    
    参数:
    filename: 文件名或文件路径
    with_dot: 是否包含点号
    to_lower: 是否转换为小写
    default: 没有后缀时的默认返回值
    
    返回:
    文件后缀名或默认值
    """
    if not filename or not isinstance(filename, str):
        return default
    
    # 获取基础文件名（去掉路径）
    basename = os.path.basename(filename)
    
    # 分割文件名和后缀
    name, ext = os.path.splitext(basename)
    
    # 如果没有后缀或文件名以点开头（如 .gitignore）
    if not ext or (not name and ext):
        return default
    
    # 处理是否包含点号
    if not with_dot and ext.startswith('.'):
        ext = ext[1:]
    
    # 处理大小写
    if to_lower:
        ext = ext.lower()
    
    return ext

# ✅ 定义 kwargs 字典, 可变参数补充形式
kwargs = {
    'with_dot': False,
    'to_lower': True
}

# ✅ 调用函数时使用 **kwargs 解包
print(get_file_extension_safe('readme.TXT', **kwargs))       # txt