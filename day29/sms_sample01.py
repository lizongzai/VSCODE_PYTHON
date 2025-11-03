import smtplib
from email.mime.text import MimeText

def send_sms_via_email(carrier_email, phone_number, message, smtp_config):
    """
    通过运营商邮箱网关发送短信（免费但有限制）
    运营商邮箱网关示例：
    - 中国移动: 13800138000@139.com
    - 中国联通: 13800138000@wo.com.cn
    - 中国电信: 13800138000@189.cn
    """
    sender_email = smtp_config['email']
    sender_password = smtp_config['password']
    smtp_server = smtp_config['smtp_server']
    smtp_port = smtp_config['smtp_port']
    
    # 构建收件人邮箱
    to_email = f"{phone_number}@{carrier_email}"
    
    msg = MimeText(message)
    msg['Subject'] = 'SMS'
    msg['From'] = sender_email
    msg['To'] = to_email
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print("短信发送成功！")
        return True
    except Exception as e:
        print(f"发送失败: {e}")
        return False

# 使用示例
smtp_config = {
    'email': 'your_email@gmail.com',
    'password': 'your_app_password',
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587
}

send_sms_via_email('139.com', '13800138000', '测试短信', smtp_config)