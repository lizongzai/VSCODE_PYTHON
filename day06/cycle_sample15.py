"""
彩数字小游戏
Version: 1.0
Author: 李小婕
Date: 2025-10-13
Description: 猜数字小游戏，用户有三次机会猜一个1到100之间的数字。
Keyword arguments:
argument -- description
Return: return_description
"""
import random
number_to_guess = random.randint(1, 100)
attempts = 3
print("欢迎来到猜数字小游戏！你有三次机会猜一个1到100之间的数字。")
for attempt in range(attempts):
    guess = int(input(f"第{attempt + 1}次猜测: "))
    if guess < number_to_guess:
        print("太小了！")
    elif guess > number_to_guess:
        print("太大了！")
    else:
        print("恭喜你，猜对了！")
        break
else:
    print(f"很遗憾，三次机会用完了。正确的数字是 {number_to_guess}。")