import json
import random

def mock_news_api():
    """模拟新闻API返回数据"""
    mock_news = {
        "code": 200,
        "msg": "success",
        "newslist": [
            {
                "title": "科技创新推动数字经济高质量发展",
                "url": "https://example.com/news/1",
                "ctime": "2024-01-15 10:30:00",
                "description": "近年来，我国数字经济规模持续扩大，创新能力显著提升。"
            },
            {
                "title": "绿色发展理念深入实施，生态环境持续改善", 
                "url": "https://example.com/news/2",
                "ctime": "2024-01-15 09:15:00",
                "description": "各地积极推进生态文明建设，取得明显成效。"
            },
            {
                "title": "文化产业发展迎来新机遇",
                "url": "https://example.com/news/3", 
                "ctime": "2024-01-15 08:45:00",
                "description": "传统文化与现代科技融合，文化产业焕发新活力。"
            }
        ]
    }
    
    for news in mock_news['newslist']:
        print(f"标题: {news['title']}")
        print(f"时间: {news['ctime']}")
        print(f"链接: {news['url']}")
        print(f"摘要: {news['description']}")
        print("-" * 60)

# 运行模拟API
mock_news_api()