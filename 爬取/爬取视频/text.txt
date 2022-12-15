# url编码包
from urllib import parse

# 软件运行结果错误，就弹出提醒警告用户
import tkinter.messagebox as msgbox

# 专门做桌面编程的
import tkinter as tk

# 控制游览器的包，点击视频网址，自动打开游览器
import webbrowser

# 正则表达式
import re


class App:
    def __init__(self, width=500, height=300):
        self.w = width
        self.h = height

        self.title = '最牛的解析视频助手'
        self.root = tk.Tk(className=self.title)

        # vip视频播放地址
        self.url = tk.StringVar()

        # 定义播放源 整形类型
        self.v = tk.IntVar()
        # 默认选择第一个解析通道
        self.v.set(1)

        # 定义软件的UI以及布局 软件空间
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)

        # 控件内容设置
        group = tk.Label(frame_1, text='暂时只有一个视频通道：', padx=10, pady=10)
        tb = tk.Radiobutton(frame_1, text='唯一通道', variable=self.v, value=1, width=10, height=3)

        label = tk.Label(frame_2, text='请输入视频链接:')
        entry = tk.Entry(frame_2, textvariabl=self.url, highlightcolor='Fuchsia', highlightthickness=1, width=35)
        play = tk.Button(frame_2, text='播放', font=('楷体', 12), fg='Purple', width=2, height=1, command=self.video_play)


        # 控件布局
        frame_1.pack()
        frame_2.pack()

        # 确定我们声明的控件在软件中的位置 行row 列col
        group.grid(row=0, column=0)
        tb.grid(row=0, column=1)
        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        play.grid(row=0, column=2, ipadx=10, ipady=10)

    # 解析视频主要函数 类方法
    def video_play(self):
        # 视频解析网站地址：
        # port = 'http://www.wmxz.wang/video.php?url='
        port='http://jx.drgxj.com/?url='

        # 做判断 防止用户输入的播放地址不合法
        if re.match(r'^https?:/{2}\w.+$', self.url.get()):
            # ^((https|http|ftp|rtsp|mms)?:\/\/)[^\s]+
            # ^ https?: / {2}\w. +$

            # 拿到用户输入的视频网址
            ip = self.url.get()

            # 视频播放地址编码
            ip = parse.quote_plus(ip)

            # 自动打开游览器
            webbrowser.open(port + ip)
        else:
            webbrowser.showerror(title='错误', message='视频播放地址无效，请重新输入…')

    def loop(self):
        self.root.resizable(True, True)
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.loop()

    # pass
