import smtplib
import getpass
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

# 发件人和收件人配置
sender = 'lizongzai@qq.com'
sender_name = '李总在'
receivers = ['lizongzai@qq.com']  # 先只发给自己测试
subject = '上半年工作情况汇报'

# 创建邮件对象
email = MIMEMultipart()
email['From'] = formataddr((sender_name, sender))
email['To'] = ', '.join(receivers)
email['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
content = """测试邮件内容：
据德国媒体报道，当地时间9日，德国火车司机工会成员进行了投票，
定于当地时间10日起进行全国性罢工。"""

email.attach(MIMEText(content, 'plain', 'utf-8'))

try:
    print("正在准备发送邮件...")
    print(f"发件人: {sender}")
    print(f"收件人: {receivers}")
    
    # authorization_code = getpass.getpass("请输入QQ邮箱授权码：")
    
    print("正在连接QQ邮箱服务器...")
    
    # 启用调试信息
    with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp_obj:
        smtp_obj.set_debuglevel(1)  # 显示详细的调试信息
        
        print("正在登录...")
        smtp_obj.login(sender, 'cwyubzqgeumqbjhe')
        
        print("正在发送邮件...")
        smtp_obj.sendmail(sender, receivers, email.as_string())
    
    print("邮件发送成功！")
    
except smtplib.SMTPAuthenticationError as e:
    print(f"认证失败：{e}")
    print("请检查：")
    print("1. 邮箱地址是否正确")
    print("2. 是否使用了授权码（不是QQ密码）")
    print("3. 授权码是否已过期")
    
except smtplib.SMTPException as e:
    print(f"邮件发送失败：{e}")
    
except Exception as e:
    print(f"发生错误：{e}")