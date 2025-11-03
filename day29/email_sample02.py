import smtplib
import getpass
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

def send_email():
    # 配置
    sender = 'lizongzai@qq.com'
    receivers = ['lizongzai@qq.com','lizongzai@gmail.com']
    
    # 创建邮件
    email = MIMEMultipart()
    email['From'] = formataddr(('李宗在', sender))
    email['To'] = ', '.join(receivers)
    email['Subject'] = Header('上半年工作情况汇报', 'utf-8')
    
    content = """据德国媒体报道，当地时间9日，德国火车司机工会成员进行了投票，
定于当地时间10日起进行全国性罢工，货运交通方面的罢工已于当地时间10日19时开始。
此后，从11日凌晨2时到13日凌晨2时，德国全国范围内的客运和铁路基础设施将进行48小时的罢工。"""
    
    email.attach(MIMEText(content, 'plain', 'utf-8'))
    
    try:
        # 获取授权码
        # auth_code = getpass.getpass("请输入QQ邮箱授权码：")
        
        # 发送邮件 - 使用更健壮的方式
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(sender, 'cwyubzqgeumqbjhe') # auth_code ='cwyubzqgeumqbjhe'
        server.sendmail(sender, receivers, email.as_string())
        
        # 尝试正常退出，如果失败就忽略
        try:
            server.quit()
        except:
            pass  # 忽略QUIT错误
        
        print("🎉 邮件发送成功！请检查QQ邮箱收件箱")
        return True
        
    except smtplib.SMTPAuthenticationError:
        print("❌ 认证失败：请检查授权码是否正确")
    except Exception as e:
        # 检查是否只是QUIT阶段的错误
        error_str = str(e)
        if "queued" in error_str or "250 OK" in error_str:
            print("🎉 邮件已成功发送！（连接关闭时的小问题，不影响邮件发送）")
            print("📧 请立即登录QQ邮箱查看收件箱")
            return True
        else:
            print(f"❌ 发送失败：{e}")
    
    return False

if __name__ == "__main__":
    send_email()