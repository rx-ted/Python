'''
from PIL import Image

img_switch = Image.open("E:\\workers\\python项目\\项目实战\\图片缩小\\img.jpg") # 读取图片
img_deal = img_switch.resize((300,300),Image.ANTIALIAS) # 转化图片

img_deal = img_deal.convert('RGB') # 保存为.jpg格式才需要
img_deal.save("e:\\out_img.jpg")




size = (20000,20000)
        #print(size)
        #print(type(size))
img = Image.open('E:/workers/python项目/项目实战/图片缩小/img.jpg')
s = img.resize(size,Image.ADAPTIVE)
s= s.convert('RGB')
print('完毕')
s.save('e:/img1.jpg')

'''

import json
import os

try:
        path = os.path.dirname(__file__)  #显示当前文件的地址
           
        fp= open('{}/user.json'.format(path),'r+',encoding='utf-8')
        user = json.loads(fp.read())
except FileNotFoundError:
        fp = open('./user.json','r+',encoding='utf-8')
        user = json.loads(fp.read())

tmp = user["default"]['language']
user["default"]['language'] = "ZH"
fp.seek(0)  # rewind
json.dump(user, fp,ensure_ascii=False)
fp.truncate()