import smtplib
import getpass
from email.mime.text import MIMEText
from email.header import Header
from string import Template
import datetime

class EmailWithTemplate:
    def __init__(self):
        self.sender = 'lizongzai@qq.com'
        self.receiver = 'lizongzai@qq.com'
        
    def load_template(self, template_name, **kwargs):
        """加载邮件模板"""
        templates = {
            'work_report': {
                'subject': '${department}${period}工作情况汇报',
                'content': Template('''尊敬的${leader}：

以下是${department}${period}的工作情况汇报：

**工作完成情况：**
${completed_work}

**存在问题：**
${existing_issues}

**下一步计划：**
${next_plan}

**其他事项：**
${other_matters}

汇报人：${reporter}
日期：${date}
                ''')
            },
            'meeting_notice': {
                'subject': '关于召开${meeting_topic}会议的通知',
                'content': Template('''各位同事：

根据工作安排，定于${meeting_time}在${meeting_place}召开${meeting_topic}会议。

**会议议题：**
${meeting_agenda}

**参会人员：**
${participants}

**注意事项：**
${notes}

请准时参加。

${department}
${date}
                ''')
            },
            'notification': {
                'subject': '${title}',
                'content': Template('''${content}

${signature}
${date}
                ''')
            }
        }
        
        if template_name not in templates:
            raise ValueError(f"模板 '{template_name}' 不存在")
            
        template_data = templates[template_name]
        subject_template = Template(template_data['subject'])
        content_template = template_data['content']
        
        # 添加默认日期
        kwargs.setdefault('date', datetime.datetime.now().strftime('%Y年%m月%d日'))
        
        return {
            'subject': subject_template.substitute(**kwargs),
            'content': content_template.substitute(**kwargs)
        }
    
    def send_email(self, template_name, **template_vars):
        """使用模板发送邮件"""
        try:
            # 加载模板
            template_result = self.load_template(template_name, **template_vars)
            
            # 创建邮件
            message = MIMEText(template_result['content'], 'plain', 'utf-8')
            message['From'] = Header('李宗在 <lizongzai@qq.com>')
            message['To'] = Header(self.receiver)
            message['Subject'] = Header(template_result['subject'], 'utf-8')
            
            # 发送邮件
            # auth_code = getpass.getpass("请输入QQ邮箱授权码：")
            
            with smtplib.SMTP_SSL('smtp.qq.com', 465) as server:
                server.login(self.sender, 'cwyubzqgeumqbjhe')
                server.sendmail(self.sender, self.receiver, message.as_string())
            
            print(f"🎉 邮件发送成功！模板：{template_name}")
            return True
            
        except Exception as e:
            print(f"❌ 邮件发送失败：{e}")
            return False

# 使用示例
if __name__ == "__main__":
    email_system = EmailWithTemplate()
    
    # 示例1：工作汇报模板
    email_system.send_email(
        'work_report',
        department='技术部',
        period='2024年上半年',
        leader='王总',
        completed_work='''1. 完成了XX系统开发
2. 优化了数据库性能
3. 团队技术培训4次''',
        existing_issues='''1. 项目进度略有延迟
2. 部分设备需要更新''',
        next_plan='''1. 加快项目进度
2. 申请设备更新预算
3. 准备下半年技术规划''',
        other_matters='无',
        reporter='李总在'
    )
    
    # 示例2：会议通知模板
    email_system.send_email(
        'meeting_notice',
        meeting_topic='2024年下半年工作计划',
        meeting_time='2024年7月15日 14:00',
        meeting_place='公司大会议室',
        meeting_agenda='''1. 总结上半年工作
2. 讨论下半年计划
3. 资源分配讨论''',
        participants='各部门负责人',
        notes='请携带相关材料',
        department='总经理办公室'
    )