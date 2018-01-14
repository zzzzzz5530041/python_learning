'''
使用 Python 生成字母验证码图片

'''
from PIL import Image, ImageDraw, ImageFont
import random
import string


def generate():
    # 生成随机字符'
    code = ''.join([random.choice(string.ascii_letters) for i in range(4)])
    # 设置图片大小
    width = 100;
    height = 40;
    im = Image.new("RGB", (width, height), (255, 255, 255))
    # 画图
    dr = ImageDraw.Draw(im);
    font = ImageFont.load_default().font
    for i in range(4):
        dr.text((5 + i * 20, 5), code[i], (random.randint(0, 0), random.randint(0, 0), random.randint(0, 255)),
               font )
    del dr;

    # 背景图
    for x in range(width):
        for y in range(height):
            if im.getpixel((x, y)) == (255, 255, 255):
                im.putpixel((x, y), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    im.save('t1.png')


if __name__ == "__main__":
    generate()
