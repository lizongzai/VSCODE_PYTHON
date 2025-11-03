import smtplib
import getpass
from email.mime.text import MIMEText
from email.header import Header
from jinja2 import Template
import os

class EmailWithJinjaTemplate:
    def __init__(self):
        self.sender = 'lizongzai@qq.com'
        self.receiver = 'lizongzai@qq.com'
        self.template_dir = 'email_templates'
        
        # 创建模板目录
        if not os.path.exists(self.template_dir):
            os.makedirs(self.template_dir)
            self.create_default_templates()
    
    def create_default_templates(self):
        """创建默认模板文件"""
        templates = {
            'work_report.html': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; }
        .header { background: #f4f4f4; padding: 20px; text-align: center; }
        .content { padding: 20px; }
        .section { margin-bottom: 20px; }
        .section-title { color: #333; border-bottom: 2px solid #007cba; padding-bottom: 5px; }
        .footer { background: #f4f4f4; padding: 10px; text-align: center; font-size: 12px; color: #666; }
    </style>
</head>
<body>
    <div class="header">
        <h1>{{ department }}{{ period }}工作情况汇报</h1>
    </div>
    
    <div class="content">
        <p>尊敬的{{ leader }}：</p>
        
        <div class="section">
            <h3 class="section-title">📊 工作完成情况</h3>
            <p>{{ completed_work|replace('\\n', '<br>')|safe }}</p>
        </div>
        
        <div class="section">
            <h3 class="section-title">⚠️ 存在问题</h3>
            <p>{{ existing_issues|replace('\\n', '<br>')|safe }}</p>
        </div>
        
        <div class="section">
            <h3 class="section-title">🎯 下一步计划</h3>
            <p>{{ next_plan|replace('\\n', '<br>')|safe }}</p>
        </div>
        
        {% if other_matters %}
        <div class="section">
            <h3 class="section-title">📝 其他事项</h3>
            <p>{{ other_matters|replace('\\n', '<br>')|safe }}</p>
        </div>
        {% endif %}
    </div>
    
    <div class="footer">
        <p>汇报人：{{ reporter }} | 日期：{{ date }}</p>
    </div>
</body>
</html>''',
            
            'simple_notice.txt': '''主题：{{ title }}

{{ content }}

{% if signature %}
{{ signature }}
{% endif %}

{{ date }}'''
        }
        
        for filename, content in templates.items():
            with open(os.path.join(self.template_dir, filename), 'w', encoding='utf-8') as f:
                f.write(content)
    
    def render_template(self, template_file, **context):
        """渲染模板"""
        template_path = os.path.join(self.template_dir, template_file)
        
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"模板文件不存在: {template_file}")
        
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()
        
        template = Template(template_content)
        return template.render(**context)
    
    def test_smtp_connection(self):
        """测试SMTP连接"""
        try:
            # 使用getpass安全输入授权码
            # auth_code = getpass.getpass("请输入QQ邮箱授权码：")
            
            print("正在连接QQ邮箱SMTP服务器...")
            server = smtplib.SMTP_SSL('smtp.qq.com', 465)
            server.set_debuglevel(1)  # 开启调试模式
            
            print("正在登录...")
            server.login(self.sender, 'cwyubzqgeumqbjhe')
            print("✅ 登录成功！")
            
            server.quit()
            return True
            
        except smtplib.SMTPAuthenticationError:
            print("❌ 认证失败：请检查邮箱地址和授权码是否正确")
        except smtplib.SMTPException as e:
            print(f"❌ SMTP错误：{e}")
        except Exception as e:
            print(f"❌ 连接失败：{e}")
        return False
    
    def send_email(self, template_file, subject, **template_vars):
        """使用Jinja2模板发送邮件"""
        try:
            # 渲染模板
            content = self.render_template(template_file, **template_vars)
            
            # 判断是HTML还是纯文本
            is_html = template_file.endswith('.html')
            
            # 创建邮件
            message = MIMEText(content, 'html' if is_html else 'plain', 'utf-8')
            message['From'] = Header(f'{self.sender}')
            message['To'] = Header(self.receiver)
            message['Subject'] = Header(subject, 'utf-8')
            
            # 发送邮件
            # auth_code = getpass.getpass("请输入QQ邮箱授权码：")
            
            with smtplib.SMTP_SSL('smtp.qq.com', 465) as server:
                server.login(self.sender, 'cwyubzqgeumqbjhe')
                server.sendmail(self.sender, [self.receiver], message.as_string())
            
            print(f"🎉 邮件发送成功！模板：{template_file}")
            return True
            
        except Exception as e:
            print(f"❌ 邮件发送失败：{e}")
            return False

# 使用示例
if __name__ == "__main__":
    email_system = EmailWithJinjaTemplate()
    
    # 先测试连接
    print("=== 测试SMTP连接 ===")
    if email_system.test_smtp_connection():
        print("\n=== 发送邮件 ===")
        # 发送HTML格式的工作报告
        email_system.send_email(
            template_file='work_report.html',
            subject='技术部2024年上半年工作情况汇报',
            department='技术部',
            period='2024年上半年',
            leader='王总',
            completed_work='''1. 完成了XX系统开发与上线
2. 数据库性能优化，响应时间提升40%
3. 组织团队技术培训4次，提升团队技能''',
            existing_issues='''1. 项目A进度延迟2周
2. 测试服务器配置需要升级
3. 部分文档需要完善''',
            next_plan='''1. 加快项目进度，确保按时交付
2. 申请测试服务器升级预算
3. 完善项目文档和用户手册''',
            other_matters='申请参加下月的技术大会',
            reporter='李宗在',
            date='2024年7月10日'
        )