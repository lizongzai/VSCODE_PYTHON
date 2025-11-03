from PIL import Image
import os

def connect_head_to_body(head_path, body_path, output_path, connection_y=None):
    """
    将头像与身体图像连接起来
    
    参数:
    head_path: 头像图片路径
    body_path: 身体图片路径
    output_path: 输出图片路径
    connection_y: 连接点的Y坐标(可选，自动计算如果为None)
    """
    try:
        # 打开头像和身体图片
        head_img = Image.open(r'C:\Users\86181\Desktop\Vscode_python\resources\blue.jpg')
        body_img = Image.open(r'C:\Users\86181\Desktop\Vscode_python\resources\guido.jpg')
        
        # 确保图片都是RGBA模式(支持透明度)
        if head_img.mode != 'RGBA':
            head_img = head_img.convert('RGBA')
        if body_img.mode != 'RGBA':
            body_img = body_img.convert('RGBA')
        
        # 获取图片尺寸
        head_width, head_height = head_img.size
        body_width, body_height = body_img.size
        
        # 计算连接点(如果未提供)
        if connection_y is None:
            # 假设连接点在头像底部和身体顶部
            connection_y = head_height
        
        # 创建新图像(宽度取两者最大值，高度为两者之和)
        new_width = max(head_width, body_width)
        new_height = head_height + body_height
        
        # 创建透明背景的新图像
        new_img = Image.new('RGBA', (new_width, new_height), (0, 0, 0, 0))
        
        # 计算头像和身体的位置(居中放置)
        head_x = (new_width - head_width) // 2
        body_x = (new_width - body_width) // 2
        
        # 将头像放在顶部
        new_img.paste(head_img, (head_x, 0), head_img)
        
        # 将身体放在头像下方
        new_img.paste(body_img, (body_x, head_height), body_img)
        
        # 保存结果
        new_img.save(output_path, 'PNG')
        print(f"图片已成功连接并保存到: {output_path}")
        
        return True
        
    except Exception as e:
        print(f"处理图片时出错: {str(e)}")
        return False

def find_connection_point(body_img_path):
    """
    尝试自动找到身体的连接点(颈部位置)
    这是一个简化的实现，实际应用中可能需要更复杂的算法
    """
    try:
        body_img = Image.open(body_img_path)
        body_width, body_height = body_img.size
        
        # 简化的算法: 假设颈部在身体顶部向下15%的位置
        # 实际应用中可能需要使用边缘检测或肤色检测等更精确的方法
        connection_y = int(body_height * 0.15)
        
        return connection_y
    except Exception as e:
        print(f"查找连接点时出错: {str(e)}")
        return None

# 使用示例
if __name__ == "__main__":
    # 请替换为您的实际文件路径
    head_image_path = "head.png"  # 头像图片路径
    body_image_path = "body.png"  # 身体图片路径
    output_image_path = "connected_character.png"  # 输出图片路径
    
    # 尝试自动找到连接点
    connection_point = find_connection_point(body_image_path)
    
    # 连接图片
    success = connect_head_to_body(
        head_image_path, 
        body_image_path, 
        output_image_path, 
        connection_point
    )
    
    if success:
        print("头像和身体连接成功!")
    else:
        print("连接失败，请检查文件路径和图片格式。")