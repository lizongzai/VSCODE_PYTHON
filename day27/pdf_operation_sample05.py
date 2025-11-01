"""
Version : 1.1
Author  : ChatGPT
Date    : 2025-11-01
Description :
    使用 pypdf 对 PDF 进行 128 位加密，并设置精细化权限控制。
    支持：
      ✓ 设置用户密码（限制访问）
      ✓ 设置所有者密码（不受权限限制）
      ✓ 控制打印、复制、注释、文本提取等权限
"""

from pypdf import PdfReader, PdfWriter
from pypdf.constants import UserAccessPermissions


def advanced_encryption(input_path, output_path, user_pwd, owner_pwd):
    """
    加密 PDF 文件并设置访问权限
    :param input_path: 输入 PDF 路径
    :param output_path: 输出加密后的 PDF 路径
    :param user_pwd: 用户密码（打开时需要输入）
    :param owner_pwd: 所有者密码（拥有全部权限）
    """
    # 读取原始 PDF
    reader = PdfReader(input_path)
    writer = PdfWriter()

    # 拷贝所有页面
    for page in reader.pages:
        writer.add_page(page)

    # 权限设置说明（位掩码可自由组合）
    # 可选权限示例：
    #   UserAccessPermissions.PRINT                       → 允许打印
    #   UserAccessPermissions.EXTRACT_TEXT_AND_GRAPHICS   → 允许复制文本和图像
    #   UserAccessPermissions.ADD_OR_MODIFY               → 允许修改或添加内容（如注释）
    #   UserAccessPermissions.FILL_FORM_FIELDS            → 允许填写表单
    #
    # 如果希望全部禁止，仅给阅读权限，可设置 perms = 0
    perms = (
        UserAccessPermissions.PRINT
        | UserAccessPermissions.EXTRACT_TEXT_AND_GRAPHICS
        | UserAccessPermissions.ADD_OR_MODIFY
        | UserAccessPermissions.FILL_FORM_FIELDS
    )

    # 执行加密
    writer.encrypt(
        user_pwd=user_pwd,      # PDF 打开密码
        owner_pwd=owner_pwd,    # 权限管理密码
        encryption_strength=128,   # 128 位 AES 加密（默认）
        permissions_flag=perms     # 控制用户权限
    )

    # 写入新 PDF
    with open(output_path, "wb") as f:
        writer.write(f)


# 使用示例
if __name__ == "__main__":
    advanced_encryption(
        "test.pdf",
        "test_secure.pdf",
        "user123",      # 打开密码
        "owner456"      # 管理密码
    )
