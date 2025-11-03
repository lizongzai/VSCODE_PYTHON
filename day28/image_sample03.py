import random  # 导入随机数模块，用于生成随机颜色
from PIL import Image, ImageDraw, ImageFont  # 导入Pillow库的图像处理模块

# 定义一个生成随机颜色的函数
def random_color():
    """生成随机颜色"""
    red = random.randint(0, 255)    # 随机生成红色分量
    green = random.randint(0, 255)  # 随机生成绿色分量
    blue = random.randint(0, 255)   # 随机生成蓝色分量
    return red, green, blue          # 返回一个 RGB 三元组

# 定义图像的宽和高
width, height = 800, 600

# 创建一个800*600的白色背景图像
image = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))

# 创建一个可以在图像上绘图的对象
drawer = ImageDraw.Draw(image)

# 设置文字字体和大小
# font = ImageFont.truetype('Kongxin.ttf', 32)  # 自定义字体（注释掉）
# font = ImageFont.truetype(r"C:\Users\86181\Desktop\Vscode_python\resources\Kongxin.ttf", 32)  # 自定义路径字体（注释掉）
font = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 32)   # 使用系统自带 Arial 字体，大小32

# 在图像上绘制文字
drawer.text(
    (300, 50),          # 文字左上角坐标
    'Hello, world!',    # 要绘制的文字
    fill=(255, 0, 0),   # 文字颜色为红色
    font=font            # 使用上面定义的字体
)

# 绘制两条蓝色对角线
drawer.line((0, 0, width, height), fill=(0, 0, 255), width=2)       # 左上到右下
drawer.line((width, 0, 0, height), fill=(0, 0, 255), width=2)       # 右上到左下

# 计算矩形的左上角和右下角坐标（中心为图像中心，边长120）
xy = width // 2 - 60, height // 2 - 60, width // 2 + 60, height // 2 + 60

# 在图像中心绘制矩形
drawer.rectangle(xy, outline=(255, 0, 0), width=2)  # 红色边框，宽度2

# 绘制4个椭圆，每个椭圆颜色随机
for i in range(4):
    left, top = 150 + i * 120, 220         # 左上角坐标
    right, bottom = 310 + i * 120, 380     # 右下角坐标
    drawer.ellipse(
        (left, top, right, bottom),        # 椭圆边界框
        outline=random_color(),            # 随机颜色
        width=8                             # 边框宽度
    )

# 显示生成的图像
image.show()

# 保存图像到文件
image.save('result.png')
