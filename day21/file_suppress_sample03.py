"""
Version: 1.0
Author: ChatGPT
Date: 2025-10-24
Description: 该脚本演示了如何使用contextlib.suppress来抑制网络请求中的异常。
1. 通过requests库进行网络请求时抑制连接错误和HTTP错误异常。
2. 继续处理后续请求而不因单个请求失败而中断。
3. 输出请求结果状态。
4. 适用于需要批量请求多个URL且不希望因单个请求失败而中断整个流程的场景。
5. 需要安装requests库（pip install requests）。
6. 适合网络编程和异常处理学习者参考。

Keyword arguments:
argument -- description
Return: return_description
"""

import requests
from contextlib import suppress

def network_operations():
    """网络操作异常抑制"""
    
    print("=== 网络操作抑制 ===")
    
    urls = [
        'https://httpbin.org/status/200',
        'https://httpbin.org/status/404',
        'https://invalid-url-that-does-not-exist.com',
        'https://httpbin.org/status/500'
    ]
    
    for url in urls:
        print(f"\n尝试请求: {url}")
        
        # 抑制所有请求相关的异常
        with suppress(requests.exceptions.RequestException, requests.exceptions.HTTPError): # 抑制请求异常和HTTP错误, 如连接错误、超时等可以继续执行
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # 如果是4xx/5xx状态码会抛出HTTPError
            print(f"✓ 请求成功: 状态码 {response.status_code}")
        
        print("继续下一个请求...")
    
    print("所有网络请求尝试完成\n")

# 运行网络示例（需要安装requests: pip install requests）
network_operations()