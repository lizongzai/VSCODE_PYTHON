# 复合条件成员检查
vip_users = {"alice", "bob", "charlie"}
active_users = {"bob", "david", "eve"}
premium_users = {"charlie", "frank"}

# 检查用户是否满足多个条件
def is_elite_user(username):
    return (username in vip_users and 
            username in active_users and 
            username in premium_users)

print(is_elite_user("charlie"))  # False (不在active_users)
print(is_elite_user("bob"))      # False (不在premium_users)

# # 更简洁的写法
# def is_elite_user_v2(username):
#     return username in (vip_users & active_users & premium_users)

# print(is_elite_user_v2("charlie"))  # False