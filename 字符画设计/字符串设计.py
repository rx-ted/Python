from PIL import Image  # 操作图像
chars = "$$$$$BBBBB8888EEEEHHHHDDDDUUUUYYYYYY1111111LLLLLLL>>>>>>-------......__       "

im = Image.open('a梦.png')   # type:Image.Image

# print(im.getpixel((152, 150)))

# print(im.mode)  # 默认RGBA
# 将RGB图像转为灰色图
om = im.convert('L')
# om.show()   # 打开图片

width, height = om.size  # 获取图像大小
with open('a梦.txt','w')as f:
    for y in range(height):
        # y:控制行数
        for x in range(width):
            # y:控制行数
            px = om.getpixel((x, y))
            index = px*len(chars)/256
            # print(chars[int(index)],end='')
            f.write(chars[int(index)])
        f.write('\n')


# print(im.getpixel((152, 150)))