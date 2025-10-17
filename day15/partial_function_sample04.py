from functools import partial

def make_request(url, method='GET', timeout=30, headers=None):
    print(f"执行 make_request:")
    print(f"  URL: {url}")
    print(f"  方法: {method}")
    print(f"  超时: {timeout}秒")
    print(f"  头部: {headers}")
    print("---")
    # 实际网络请求逻辑...

# 创建偏函数
api_get = partial(make_request, method='GET', timeout=60)
api_post = partial(make_request, method='POST')

print("=== 调用 api_get ===")
api_get('https://api.example.com/users')

print("=== 调用 api_post ===")
api_post('https://api.example.com/users', timeout=10)

print("=== 调用 api_get 并覆盖参数 ===")
api_get('https://api.example.com/data', timeout=5, headers={'Auth': 'token'})