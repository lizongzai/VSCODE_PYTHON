def f(x):
    if x > 1:
        return 3 * x - 5
    elif -1 <= x <= 1:
        return x + 2
    else:
        return 5 * x + 3
    
for x in [-2, 0, 2]:
    print(f"x={x}, y={f(x)}")