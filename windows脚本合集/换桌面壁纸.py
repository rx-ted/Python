from tkinter import filedialog
import tkinter as tk
import win32con
import win32gui
import win32api


def desktop_img(bmp_path):
    root = tk.Tk()
    filename = filedialog.askopenfilename()
    print('选择的壁纸路径是：', filename)
    # 打开windows HKEY_CURRENT_USER 注册表 并设置属性
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # 在HKEY_CURRENT_USER注册表中写入属性值 0 桌面壁纸居中 2 拉伸适应桌面
    win32api.RegSetValueEx(k, "wapaperstyle", 0, win32con.REG_SZ, "2")
    win32api.RegSetValueEx(k, "tilewallpaper", 0, win32con.REG_SZ, "0")

    # 刷新桌面
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, filename, win32con.SPIF_SENDWININICHANGE)


desktop_img('bmp_path')
