import random

def generate_double_color_ball():
    # 红球 1~33，选6个
    red_balls = random.sample(range(1, 34), 6)
    red_balls.sort()  # 排序更美观
    
    # 蓝球 1~16，选1个
    blue_ball = random.choice(range(1, 17))
    
    return red_balls, blue_ball

# 生成一注号码
red, blue = generate_double_color_ball()
print(f"红球: {red}, 蓝球: {blue}")
