# # example
# a = '5'
# b = [1, 5]
#
#
# def s(a, *b):
#     sum = a + str(b[0])
#     print(sum)
#
#
# s(a,*b)
import os
import imghdr

# print(imghdr.what('d:/图片/龙《Smite神之浩劫》4k游戏壁纸3840x2160.jpg'))
# print(imghdr.what('d:/图片/冬季躺在雪地的女孩 玫瑰花 小狗 4k高清壁纸.jpg'))
# os.remove('d:/图片/冬季躺在雪地的女孩 玫瑰花 小狗 4k高清壁纸.jpg')
# print()

path = 'd:/图片/黎明 风景 女子 后背 唯美插画 4k动漫壁纸.jpg'
code = imghdr.what(path)
print(code)
if code is None:
    os.remove(path)
    print('ok')
else:
    print('?')
