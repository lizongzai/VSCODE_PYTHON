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

print(get_file_extension('readme.txt'))       # txt
print(get_file_extension('readme.txt.md'))    # md
print(get_file_extension('.readme'))          #.readme
print(get_file_extension('readme.'))          #.
print(get_file_extension('readme'))           #    