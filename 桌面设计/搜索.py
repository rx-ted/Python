import tkinter
# 创建窗口
root = tkinter.Tk()
# 设置最大化、最小化界面
root.minsize(400, 400)
root.maxsize(400, 400)

# 设置窗口标题
root.title("测试")

# 搜索标题、创建输入框
label = tkinter.Label(root, text='搜索',
                      bg='white', fg='black',  #bg为背景色，fg为前景色
                      font=("华文行楷", 20),
                      # wraplength=150,  # 设置多少单位后开始换行
                      anchor='w'
                      )
label.pack(expand=1)
# 创建按钮
label1 = tkinter.Entry(root)
label1.place(relx=0.12, rely=0.20, width=300, height=30,
              )
button = tkinter.Button(root, text="搜索")
button.place(relx=0.4, rely=0.75, width=80)
# a = tkinter.Button()

# 算法
def sousuo():
    sousuo = label1.get()
    print(sousuo)
button.bind("<ButtonRelease-1>",sousuo)

root.mainloop()