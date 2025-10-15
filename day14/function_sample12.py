import os

def get_file_extension(filename):
    """
    获取文件后缀名
    
    参数:
    filename: 文件名或文件路径
    
    返回:
    文件后缀名（包含点号），如果没有后缀则返回空字符串
    """
    # 使用字符串的rpartition方法从右边分割
    _, dot, extension = filename.rpartition('.')
    
    if dot == '.':
        return dot + extension
    else:
        return ""

def get_file_extension_enhanced(filename, with_dot=True, to_lower=False):
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

def print_file_info(filename):
    """
    打印文件的完整路径信息
    """
    print(f"\n=== 文件分析: {filename if filename else '(空字符串)'} ===")
    
    # 获取绝对路径（如果可能）
    if filename and os.path.isabs(filename):
        abs_path = filename
    elif filename:
        try:
            abs_path = os.path.abspath(filename)
        except:
            abs_path = "无法获取绝对路径"
    else:
        abs_path = "无路径"
    
    # 获取目录名和文件名
    dir_name = os.path.dirname(filename) if filename else "无目录"
    base_name = os.path.basename(filename) if filename else "无文件名"
    
    print(f"原始输入: {filename}")
    print(f"绝对路径: {abs_path}")
    print(f"目录部分: {dir_name}")
    print(f"文件部分: {base_name}")
    
    # 获取各个版本的后缀名
    ext_basic = get_file_extension(filename)
    ext_enhanced = get_file_extension_enhanced(filename, with_dot=False)
    ext_safe = get_file_extension_safe(filename, with_dot=False)
    
    print(f"基础版后缀: '{ext_basic}'")
    print(f"增强版后缀: '{ext_enhanced}'")
    print(f"安全版后缀: '{ext_safe}'")

# 测试代码
if __name__ == "__main__":
    test_cases = [
        "document.pdf",
        "image.jpg", 
        "script.py",
        "archive.tar.gz",  # 多重扩展
        "README",          # 无扩展名
        ".hidden",         # 隐藏文件
        "path/to/file.txt", # 包含路径
        "UPPERCASE.PNG",   # 大写
        "file.with.multiple.dots.txt",
        "",                # 空字符串
        "no_extension",    # 无扩展名
        "/usr/local/bin/python3",  # 完整路径
        "C:\\Windows\\System32\\cmd.exe",  # Windows路径
    ]
    
    print("=" * 60)
    print("文件后缀名详细分析")
    print("=" * 60)
    
    # 详细分析每个文件
    for filename in test_cases:
        print_file_info(filename)
    
    print("\n" + "=" * 60)
    print("汇总表格")
    print("=" * 60)
    
    # 汇总表格（保持原有格式）
    print(f"{'文件':40} | {'基础版':8} | {'增强版':8} | {'安全版':8} | {'路径信息'}")
    print("-" * 90)
    
    for filename in test_cases:
        ext1 = get_file_extension(filename)
        ext2 = get_file_extension_enhanced(filename, with_dot=False)
        ext3 = get_file_extension_safe(filename, with_dot=False)
        
        # 简化的路径信息
        dir_part = os.path.dirname(filename) if filename else ""
        base_part = os.path.basename(filename) if filename else ""
        path_info = f"{dir_part}/[{base_part}]" if dir_part else f"[{base_part}]"
        
        print(f"{filename:40} | {ext1:8} | {ext2:8} | {ext3:8} | {path_info}")