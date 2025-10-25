"""
Version: 1.0
Author: ChatGPT
Description: 该脚本演示了如何使用contextlib.suppress来抑制集合操作中的异常。
1. 在列表操作中抑制索引越界异常。
2. 在集合操作中抑制元素不存在异常。
3. 在字典操作中抑制键不存在异常。
4. 继续处理后续操作而不因单个操作失败而中断。
5. 输出操作结果状态。
6. 适用于需要批量操作集合且不希望因单个操作失败而中断整个流程的场景。

Keyword arguments:
argument -- description
Return: return_description
"""

from contextlib import suppress

def collection_operations():
    """集合操作异常抑制"""
    
    print("=== 集合操作抑制 ===")
    
    # 1. 列表操作
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    with suppress(IndexError):
        item = my_list[12]  # 索引越界
        print(f"获取的元素: {item}")
    print("索引越界时继续执行")
    
    # 2. 集合操作
    my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    
    with suppress(KeyError):
        my_set.remove(11)  # 不存在的元素
        print("元素已移除")
    print("元素不存在时继续执行")
    
    # 3. 字典操作
    my_dict = {'name': 'Alice', 'age': 25}
    
    with suppress(KeyError):
        del my_dict['']  # 删除不存在的键
        print("键已删除")
    print("键不存在时继续执行")
    
    print("集合操作完成\n")


# 运行实际场景示例
if __name__ == "__main__":
    # 运行集合操作示例
    collection_operations()