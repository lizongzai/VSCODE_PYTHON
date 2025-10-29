"""
Version: 1.0
Author: ChatGPT
Description: JavaScript JSON模块示例，获取国内新闻并显示新闻标题和链接。
Date: 2025-10-27

Keyword arguments:
argument -- description
Return: return_description
"""
import requests
response = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')

if response.status_code == 200:
    data = response.json()
    
    print("API返回信息:")
    print(f'状态码: {data["code"]}')
    print(f'消息: {data["msg"]}')
    print(f'提示: {data["tip"]}')
    
    if  data['code'] == 200:
        for news in data['newslist']:
            print(f"标题: {news['title']}")
            print(f"链接: {news['url']}\n")
    else:
        print("无法获取新闻数据")
else:
    print("API调度失败，请检查API key和网络连接")

