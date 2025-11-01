from pypdf import PdfReader, PdfWriter
# from pypdf.constants import Encryption

def encrypt_with_pypdf(input_path, output_path, user_pwd, owner_pwd):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    for page in reader.pages:
        writer.add_page(page)
    
    # pypdf有更好的常量支持
    writer.encrypt(
        user_password=user_pwd,
        owner_password=owner_pwd,
        use_128bit=True
    )
    
    with open(output_path, 'wb') as f:
        writer.write(f)
        
# 使用示例
if __name__ == "__main__":
    encrypt_with_pypdf('test.pdf', 'test_encrypt_with_pypdf.pdf', 'user123', 'owner456')