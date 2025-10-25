from contextlib import suppress

def nested_suppress_example():
    """嵌套使用 suppress"""
    
    print("=== 嵌套抑制示例 ===")
    
    def risky_operation():
        # 内层抑制 ValueError
        with suppress(ValueError):
            result = int("not_a_number")
            return result
        
        # 外层抑制 TypeError  
        with suppress(TypeError):
            return "fallback_result"
    
    # 调用风险操作
    with suppress(Exception):
        result = risky_operation()
        print(f"操作结果: {result}")
    
    print("嵌套抑制完成\n")

# 运行嵌套示例
nested_suppress_example()