import operator

def calc(init_value, op_func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value
    print(f"初始值: {result}")
    
    for i, item in enumerate(items, 1):
        if type(item) in (int, float):
            old_result = result
            result = op_func(result, item)
            print(f"第{i}步: {old_result} + ({item}×{item}) = {result}")
    
    return result

if __name__ == "__main__":
    # 使用 lambda 表达式
    squared_sum = calc(0, lambda x, y: operator.add(x, operator.mul(y, y)), 1, 2, 3, 4)
    print(f"最终平方和: {squared_sum}")