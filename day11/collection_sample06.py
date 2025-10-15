set_x = {1, 2, 3}
set_y = {1, 2, 3, 4, 5}
set_z = {1, 2}

# 子集判断
print(set_z.issubset(set_x))    # False
print(set_z.issubset(set_y))    # True
print(set_z <= set_y)           # True