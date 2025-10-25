"""
Version: 1.0.0
Author: ChatGPT
Description: 该脚本演示了如何在实际应用场景中使用contextlib.suppress来抑制文件操作中的异常。
1. 在文件删除操作中抑制文件不存在异常。
2. 在文件备份操作中抑制文件不存在和同名文件异常。
3. 在资源清理操作中抑制关闭资源时的异常。
4. 继续处理后续操作而不因单个操作失败而中断。
5. 输出操作结果状态。
6. 适用于需要批量处理文件且不希望因单个操作失败而中断整个流程的场景。
Keyword arguments:
argument -- description
Return: return_description
"""


from pdb import main
import shutil
from contextlib import suppress
from pathlib import Path

def practical_scenarios():
    """实际应用场景"""
    
    print("=== 实际应用场景 ===")
    
    # 场景1：清理临时文件（文件可能不存在）
    temp_files = ['temp1.txt', 'temp2.log', 'cache.dat']
    
    for temp_file in temp_files:
        with suppress(FileNotFoundError):
            Path(temp_file).unlink() # 删除文件, 如果文件不存在则抑制异常
            print(f"已删除: {temp_file}")
    
    print("临时文件清理完成")
    
    # 场景2：安全地创建备份
    source_file = 'important_data.txt'
    backup_file = 'important_data.txt.bak'
    
    # 创建测试文件
    with open(source_file, 'w') as f:
        f.write("重要数据内容")
    
    with suppress(FileNotFoundError, shutil.SameFileError):
        shutil.copy2(source_file, backup_file)
        print("备份创建成功")
    
    # 场景3：安全地关闭资源
    file_handles = []
    
    # 模拟一些文件操作
    try:
        f1 = open('file1.txt', 'w')
        file_handles.append(f1)
        f1.write("内容1")
        
        f2 = open('file2.txt', 'w') 
        file_handles.append(f2)
        f2.write("内容2")
        
    finally:
        # 安全关闭所有文件句柄
        for handle in file_handles:
            with suppress(OSError, ValueError):
                handle.close()
                print("文件句柄已关闭")
    
    print("资源清理完成\n")

# 运行实际场景示例
if __name__ == "__main__":
    practical_scenarios()