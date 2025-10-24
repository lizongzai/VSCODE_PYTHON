"""
Version: 1.0
Author: 李小婕
Description: 使用 contextlib.ExitStack 同时管理多个文件的打开与关闭

Keyword arguments:
argument -- description
Return: return_description
"""

from contextlib import ExitStack
import os

def process_multiple_files(files):
    """同时管理多个文件"""
    with ExitStack() as stack:
        file_objects = []
        
        # 打开所有文件
        for filename, mode in files:
            try:
                file_obj = stack.enter_context(open(filename, mode, encoding='utf-8'))
                file_objects.append(file_obj)
                print(f"成功打开文件: {filename} (模式: {mode})")
            except Exception as e:
                print(f"打开文件 {filename} 失败: {e}")
                continue
        
        # 所有文件都在这里保持打开状态，可以进行操作
        print(f"\n开始处理 {len(file_objects)} 个文件...")
        
        for file_obj in file_objects:
            print(f"\n处理文件: {file_obj.name}")
            
            # 根据打开模式进行不同的操作
            if 'r' in file_obj.mode:
                try:
                    content = file_obj.read()
                    print(f"读取到 {len(content)} 个字符")
                    
                    # 如果是配置文件，可以解析内容
                    if file_obj.name.endswith('.txt'):
                        lines = content.splitlines()
                        print(f"文件包含 {len(lines)} 行")
                        
                except Exception as e:
                    print(f"读取文件失败: {e}")
            
            if 'w' in file_obj.mode or 'a' in file_obj.mode:
                try:
                    file_obj.write(f"<!-- 处理时间: {os.times()} -->\n")
                    print("已写入数据")
                except Exception as e:
                    print(f"写入文件失败: {e}")
        
        print("\n文件处理完成，即将自动关闭所有文件...")
    
    # 退出 with 块时，所有文件会自动关闭
    print("所有文件已自动关闭")

def copy_file_with_metadata(source_file, target_file):
    """使用 ExitStack 复制文件并添加元数据"""
    with ExitStack() as stack:
        # 同时打开源文件（读）和目标文件（写）
        src = stack.enter_context(open(source_file, 'r', encoding='utf-8'))
        dst = stack.enter_context(open(target_file, 'w', encoding='utf-8'))
        
        # 复制内容
        content = src.read()
        dst.write(f"<!-- 源文件: {source_file} -->\n")
        dst.write(f"<!-- 复制时间: {os.times()} -->\n")
        dst.write(content)
        
        print(f"文件复制完成: {source_file} -> {target_file}")

def merge_multiple_files(input_files, output_file):
    """合并多个文件内容到一个文件"""
    with ExitStack() as stack:
        # 打开输出文件
        output = stack.enter_context(open(output_file, 'w', encoding='utf-8'))
        
        # 打开所有输入文件
        input_handles = []
        for input_file in input_files:
            try:
                input_handle = stack.enter_context(open(input_file, 'r', encoding='utf-8'))
                input_handles.append((input_file, input_handle))
                print(f"已打开用于合并的文件: {input_handles}")
            except Exception as e:
                print(f"无法打开文件 {input_file}: {e}")
        
        # 合并文件内容
        output.write("=== 合并文件 ===\n\n")
        
        for filename, handle in input_handles:
            output.write(f"--- {filename} ---\n")
            content = handle.read()
            output.write(content)
            output.write("\n\n")
            print(f"已合并: {filename}")
        
        print(f"文件合并完成，输出到: {output_file}")

# 创建测试文件
def create_test_files():
    """创建测试用的文件"""
    test_files = {
        'config.txt': '用户名: admin\n密码: 123456\n服务器: localhost',
        'data.txt': '这是数据文件\n包含一些重要的信息\n处理完成',
        'log.txt': '2024-01-01 10:00:00 系统启动\n2024-01-01 10:05:00 用户登录'
    }
    
    for filename, content in test_files.items(): # itmems() 方法返回键值对是什么内容，比如('config.txt', '用户名: admin\n密码: 123456\n服务器: localhost')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"创建测试文件: {filename}")

# 主程序
if __name__ == "__main__":
    print("=== ExitStack 多文件管理示例 ===\n")
    
    # 1. 创建测试文件
    print("1. 创建测试文件...")
    create_test_files()
    
    # 2. 处理多个文件（不同模式）
    print("\n2. 处理多个文件...")
    files_to_process = [
        ('config.txt', 'r'),      # 只读模式
        ('data.txt', 'r+'),       # 读写模式
        ('log.txt', 'a'),         # 追加模式
        ('output.txt', 'w'),      # 写入模式
        ('nonexistent.txt', 'r')  # 这个文件不存在，会失败
    ]
    
    process_multiple_files(files_to_process)
    
    # 3. 文件复制示例
    print("\n3. 文件复制示例...")
    copy_file_with_metadata('config.txt', 'config_backup.txt')
    
    # 4. 文件合并示例
    print("\n4. 文件合并示例...")
    input_files = ['config.txt', 'data.txt', 'log.txt']
    merge_multiple_files(input_files, 'merged_output.txt')
    
    # 5. 验证文件是否已关闭
    print("\n5. 验证文件状态...")
    test_files = ['config.txt', 'data.txt', 'log.txt', 'output.txt', 
                  'config_backup.txt', 'merged_output.txt']
    
    for file in test_files:
        if os.path.exists(file):
            try:
                # 尝试再次打开，如果文件未被正确关闭，这里可能会失败
                with open(file, 'r', encoding='utf-8') as f:
                    print(f"✓ {file} - 文件状态正常")
            except Exception as e:
                print(f"✗ {file} - 文件状态异常: {e}")
        else:
            print(f"- {file} - 文件不存在")
    
    print("\n=== 示例完成 ===")