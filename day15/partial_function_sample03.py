from functools import partial

# 网络请求函数
def make_request(url, method='GET', timeout=30, headers=None):
    print(f"请求: {method} {url}, 超时: {timeout}秒")
    # 实际网络请求逻辑...

# 创建特定配置的请求函数
api_get = partial(make_request, method='GET', timeout=60)
api_post = partial(make_request, method='POST')

# 使用简化后的函数
api_get('https://api.example.com/users')
api_post('https://api.example.com/users', timeout=10)



