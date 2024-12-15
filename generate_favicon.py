from PIL import Image, ImageDraw, ImageFont
import os

def create_favicon():
    # 创建一个正方形画布
    size = 256
    image = Image.new('RGB', (size, size), color='#2C3E50')  # 深蓝灰色背景
    draw = ImageDraw.Draw(image)

    # 加载等宽字体
    font_path = os.path.join(os.environ.get('WINDIR', 'C:/Windows'), 'Fonts', 'consola.ttf')
    font_large = ImageFont.truetype(font_path, 180)
    font_small = ImageFont.truetype(font_path, 80)

    # 计算文字居中
    def get_text_center(text, font):
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        x = (size - text_width) / 2
        y = (size - text_height) / 2 - 40  # 再往上调整
        return x, y

    # 绘制居中的 {Z}
    z_x, z_y = get_text_center("{Z}", font_large)
    draw.text((z_x, z_y), "{Z}", font=font_large, fill='#ECF0F1')  # 浅灰色字体

    # 绘制 "dev"
    dev_x, dev_y = get_text_center("dev", font_small)
    draw.text((dev_x, z_y + 150), "dev", font=font_small, fill='#3498DB')  # 亮蓝色

    # 保存不同尺寸的favicon
    sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128)]
    
    os.makedirs('c:/MyBase/Code/zachthinking.github.io/assets/images', exist_ok=True)
    
    for width, height in sizes:
        resized_image = image.resize((width, height), Image.LANCZOS)
        filename = f'c:/MyBase/Code/zachthinking.github.io/assets/images/favicon-{width}x{height}.png'
        resized_image.save(filename)

    # 生成.ico文件
    image.save('c:/MyBase/Code/zachthinking.github.io/favicon.ico', sizes=sizes)

if __name__ == '__main__':
    create_favicon()
    print("Favicon generated successfully!")
