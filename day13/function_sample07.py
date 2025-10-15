def send_email(to, subject, *attachments, cc=None, bcc=None, **headers):
    """发送邮件函数"""
    print(f"收件人: {to}")
    print(f"主题: {subject}")
    print(f"附件: {attachments}")
    print(f"抄送: {cc}")
    print(f"密送: {bcc}")
    print(f"其他头信息: {headers}")

# 使用示例
send_email("user@example.com", "测试邮件", "file1.pdf", "file2.jpg",
           cc="boss@example.com", priority="high", reply_to="admin@example.com")