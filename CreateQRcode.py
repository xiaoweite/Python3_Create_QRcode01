#!/user/bin/Python3
"""
@Lanson
@2019-11-02
"""

"""
需要安装的包：
    pip install pillow
    pip install numpy
    pip install imageio
    pip install qrcode
    pip install matplotlib
    pip install myqr
python版本：3.7+
"""
import qrcode
from PIL import Image
import matplotlib.pyplot as plt
from PIL import ImageDraw
from PIL import ImageFont
'''
【红色】：red 【橙色】：orange 【黄色】：yellow 【绿】：green 【 蓝】：blue【紫】：purple 
【灰色】：gray 【白色】：white 【粉红色】：pink 【黑色】：black【墨绿色】：dark green 【橙红色】：orange-red
'''
def getQRcode(strs, name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    # 添加数据
    qr.add_data(strs)
    # 填充数据
    qr.make(fit=True)
    # 生成图片
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.convert("CMYK")  # RGBA
    # 添加logo
    icon = Image.open("logo.jpg")
    # 获取图片的宽高
    img_w, img_h = img.size
    factor = 6
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    # 重新设置logo的尺寸
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)


    img.paste(icon, (w, h), None)
    # 显示图片
    # plt.imshow(img)
    # plt.show()
    img = img.convert('RGB')
    img.save(name)
    return img
def info(name,body,num):
    getQRcode(body, name)
    oriImg = Image.open("ditu.jpg")
    oriImg2 = Image.open(name)
    oriImg2 = oriImg2.resize((285, 290))#设置二维码大小
    oriImg.paste(oriImg2, (100, 95))#将二维码放在底图上
    draw = ImageDraw.Draw(oriImg)
    font = ImageFont.truetype('AdobeGothicStd-Bold.otf', 40)#设置字体
    draw.text((100, 425), '博主:'+num, (50, 51, 51), font=font)#把字添加到图片上
    oriImg = oriImg.convert('RGB')
    oriImg.save(name)
if __name__ == '__main__':
    info("qrcode_result.png","https://blog.csdn.net/xiaoweite1","Lansonli")
    print("自定义二维码生成成功!!!")