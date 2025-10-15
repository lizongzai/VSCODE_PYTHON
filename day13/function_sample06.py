def correct_order(required1, required2, *args, default1="默认1", default2="默认2", **kwargs):
    """展示正确的参数顺序"""
    print(f"必需参数: {required1}, {required2}")
    print(f"可变位置参数 *args: {args}")
    print(f"默认参数: {default1}, {default2}")
    print(f"可变关键字参数 **kwargs: {kwargs}")
    print("-" * 40)
    
correct_order("值1", "值2", default1="新默认1", default2="新默认2")
correct_order("值1", "值2", name="张三", age=25, city="北京")
correct_order("值1", "值2", "额外A", "额外B",  default1="覆盖默认", name="李四", age=30)