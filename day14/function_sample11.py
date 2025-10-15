
# 基础版本
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
    
    
# 增强版本（推荐）    
import os

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

# 安全版本（处理特殊情况）
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

# 测试各种情况
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
    ]
    
    print("=== 文件后缀名测试 ===")
    
    for filename in test_cases:
        # 基础版本
        ext1 = get_file_extension(filename)
        
        # 增强版本（推荐）
        ext2 = get_file_extension_enhanced(filename, with_dot=False)
        
        # 安全版本（处理特殊情况）
        ext3 = get_file_extension_safe(filename, with_dot=False)
        
        print(f"文件: {filename:30} | 基础版: {ext1:8} | 增强版: {ext2:8} | 安全版: {ext3:8}")    