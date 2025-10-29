import requests

# 免费的公开API，无需注册
def free_json_api():
    try:
        # 免费的测试API
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        if response.status_code == 200:
            data = response.json()
            print(f"响应数据类型: {type(data)}")
            
            if isinstance(data, list):
                print("获取到的数据（前3条）:")
                for item in data[:3]:
                    print(f"用户ID: {item['userId']}")
                    print(f"标题: {item['title']}")
                    print(f"内容: {item['body'][:30]}...")
                    print("-" * 50)
    except Exception as e:
        print(f"错误: {e}")

# 运行
free_json_api()


