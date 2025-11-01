# pip install -U pypdf
from pypdf import PdfReader, PdfWriter
from pypdf.constants import UserAccessPermissions

def advanced_encryption(input_path, output_path, user_pwd, owner_pwd):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    # 组合需要的权限（按需修改）
    perms = (
        UserAccessPermissions.PRINT # 允许打印
        | UserAccessPermissions.EXTRACT_TEXT_AND_GRAPHICS
        | UserAccessPermissions.ADD_OR_MODIFY
        | UserAccessPermissions.FILL_FORM_FIELDS
    )

    writer.encrypt(
        user_password=user_pwd,      # 打开文件的用户密码
        owner_password=owner_pwd,    # 拥有者密码（可绕过限制）
        use_128bit=True,
        permissions_flag=perms
    )

    with open(output_path, "wb") as f:
        writer.write(f)

# 使用示例
advanced_encryption("test.pdf", "test_secure1.pdf", "user123", "owner456")
