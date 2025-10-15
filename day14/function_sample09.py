import os

def get_file_extension(filename, with_dot=True, to_lower=False):
    """
    获取文件后缀名（增强版）
    
    参数:
    filename: 文件名或文件路径
    with_dot: 是否包含点号
    to_lower: 是否转换为小写
    
    返回:
    文件后缀名
    """
    # 使用os.path.splitext获取后缀名
    _, ext = os.path.splitext(filename)
    
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
print(get_file_extension('readme.TXT', **kwargs))       # txt
print(get_file_extension('readme.TXT', with_dot=False, to_lower=True))       # txt

print(get_file_extension('readme.txt.md', **kwargs))    # md
print(get_file_extension('.readme', **kwargs))          #.readme
print(get_file_extension('readme.', **kwargs))          #.
print(get_file_extension('readme', **kwargs))           #    