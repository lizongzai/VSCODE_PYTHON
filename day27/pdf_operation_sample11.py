"""
Version : 3.1
Author  : ChatGPT
Date    : 2025-11-01
Description :
    批量为 PDF 添加文字水印（旋转/半透明/居中），支持可选加密。
    功能：
      - 自动生成文字水印 PDF
      - 批量处理指定目录下 PDF 文件
      - 可选加密（128-bit AES + 权限控制）
      - 输出到指定目录，避免覆盖原文件
"""

import os
from pypdf import PdfReader, PdfWriter
from pypdf.constants import UserAccessPermissions
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color


def create_text_watermark(watermark_path, text="机密 Confidential"):
    """
    创建文字水印 PDF（单页），支持中文
    :param watermark_path: 输出水印 PDF 文件路径
    :param text: 水印文字内容（支持中英文）
    """
    # 注册中文字体（需确保本地有此字体文件）
    # pdfmetrics.registerFont(TTFont('SimSun', 'SimSun.ttf'))  # 宋体
    
    # 使用本地字体文件路径
    font_path = r"C:\Windows\Fonts\simsun.ttc"  # 宋体
    pdfmetrics.registerFont(TTFont('SimSun', font_path))
    
    # 创建一个 PDF 画布，页面尺寸为 letter（可根据需要修改）
    c = canvas.Canvas(watermark_path, pagesize=letter)
    c.setFont("Helvetica", 50)  # 设置字体和字号
    # 设置半透明灰色
    c.setFillColor(Color(0, 0, 0, alpha=0.2))
    
    # 将原点移动到页面中心，方便旋转居中绘制
    c.saveState()  # 保存状态
    c.translate(300, 400)  # 页面中心位置，可根据实际调整
    c.rotate(45)            # 旋转 45 度
    c.drawCentredString(0, 0, text)  # 在中心绘制文字
    c.restoreState()        # 恢复状态，避免影响其他操作
    c.save()                # 保存 PDF


def add_watermark(input_pdf, watermark_pdf, output_pdf,
                  encrypt=False, user_pwd=None, owner_pwd=None):
    """
    为单个 PDF 添加水印，并可选加密
    :param input_pdf: 待处理 PDF 文件路径
    :param watermark_pdf: 水印 PDF 文件路径（单页）
    :param output_pdf: 输出 PDF 文件路径
    :param encrypt: 是否启用加密
    :param user_pwd: 用户密码（打开文件需要输入）
    :param owner_pwd: 所有者密码（绕过权限限制）
    """
    # 读取原 PDF
    reader = PdfReader(input_pdf)
    # 读取水印 PDF 的第一页
    watermark = PdfReader(watermark_pdf).pages[0]
    # 创建 PDF 写入对象
    writer = PdfWriter()

    # 遍历原 PDF 每页，将水印合并到每页
    for page in reader.pages:
        page.merge_page(watermark)  # 合并水印
        writer.add_page(page)       # 添加到写入对象

    # 如果启用加密，则设置权限
    if encrypt and user_pwd and owner_pwd:
        # 权限组合示例：
        # UserAccessPermissions.PRINT                      → 允许打印
        # UserAccessPermissions.EXTRACT_TEXT_AND_GRAPHICS  → 允许复制文本和图像
        perms = (
            UserAccessPermissions.PRINT
            | UserAccessPermissions.EXTRACT_TEXT_AND_GRAPHICS
        )
        # ⚡ 使用兼容旧版参数进行加密
        writer.encrypt(
            user_pwd,         # 用户密码
            owner_pwd,        # 所有者密码
            use_128bit=True,  # 128 位 AES
            permissions_flag=perms
        )

    # 写入输出 PDF 文件
    with open(output_pdf, "wb") as f:
        writer.write(f)


def batch_watermark(source_dir, watermark_pdf, output_dir,
                    encrypt=False, user_pwd=None, owner_pwd=None):
    """
    批量处理目录下所有 PDF 文件，添加水印并可选加密
    :param source_dir: 待处理 PDF 文件所在目录
    :param watermark_pdf: 水印 PDF 文件路径
    :param output_dir: 输出目录
    :param encrypt: 是否启用加密
    :param user_pwd: 用户密码
    :param owner_pwd: 所有者密码
    """
    # 确保输出目录存在，如果不存在则创建
    os.makedirs(output_dir, exist_ok=True)

    # 遍历目录下所有文件
    for filename in os.listdir(source_dir):
        if filename.lower().endswith(".pdf"):  # 只处理 PDF 文件
            input_path = os.path.join(source_dir, filename)
            # 输出文件名加上 _watermarked，避免覆盖原文件
            base, ext = os.path.splitext(filename)
            output_path = os.path.join(output_dir, f"{base}_watermarked{ext}")

            print(f"Processing: {input_path}")  # 打印处理进度

            # 调用单文件水印函数
            add_watermark(
                input_path,
                watermark_pdf,
                output_path,
                encrypt,
                user_pwd,
                owner_pwd
            )

    print("✅ 批量水印处理完成！")


# 使用示例
if __name__ == "__main__":
    # 1️⃣ 生成文字水印 PDF
    watermark_file = "watermark.pdf"
    create_text_watermark(watermark_file, text="机密 Confidential")

    # 2️⃣ 批量处理 input_pdfs 文件夹中的 PDF
    batch_watermark(
        source_dir="input_pdfs",       # 原 PDF 文件目录
        watermark_pdf=watermark_file,  # 刚生成的水印 PDF
        output_dir="output_pdfs",      # 输出目录
        encrypt=True,                  # 是否启用加密
        user_pwd="user123",            # 用户密码
        owner_pwd="owner456"           # 所有者密码
    )
