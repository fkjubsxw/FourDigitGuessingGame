import tkinter
from tkinter import Label, messagebox
import random
"""
x=random.randint(1000,9999)
print(x)

s=str(x)
a,b,c,d=int(s[0]),int(s[1]),int(s[2]),int(s[3])
"""

#创建窗口
a1=tkinter.Tk()
#创建窗口标题
a1.title("猜四位数小游戏")
#获取用户分辨率,据此决定窗口大小，获取的用户屏幕的（宽，高）
w,h=a1.maxsize()
#设置窗口大小,窗口打开位置
#这样即为在屏幕正中，宽和高均为一半
a1.geometry(f'{int(w/2)}x{int(h/2)}+{int(w/4)}+{int(h/4)}')
#设置窗口大小的锁定
a1.resizable(False,False)
#设置窗口图标,图片相对路径
a1.iconbitmap("Logo.ICO")
#设置窗口背景颜色:
a1.configure(bg="#FFF0F5")

def close():
    d1=messagebox.askokcancel('关闭', '确认关闭？')
    if d1:
        pass
        # 销毁窗口/组件
        a1.destroy()
    else:
        messagebox.showinfo('关闭', "请继续游戏吧！")
def start():
    global x,a,b,c,d
    x = random.randint(1000, 9999)
    #print(x)
    s = str(x)
    a, b, c, d = int(s[0]), int(s[1]), int(s[2]), int(s[3])
    a3 = tkinter.Toplevel()
    a3.title('游戏')
    a3.geometry(f'{int(w / 2)}x{int(h / 2)}+{int(w / 3)}+{int(h / 4)}')
    a3.resizable(False, False)
    a3.iconbitmap("Logo.ICO")
    a3.configure(bg="#FFF0F5")

    a6 = tkinter.Toplevel()
    a6.title('演草纸')
    a6.geometry(f'{int(w / 3)}x{int(h / 2)}+{0}+{0}')
    a6.resizable(False, False)
    a6.iconbitmap("Logo.ICO")
    a6.configure(bg="#FFF0F5")
    #多行文本框
    note_text=tkinter.Text(a6,font=('黑体', 16), width=35,height=18)
    note_text.pack(padx=20,pady=10,fill='both',expand=True)
    #加滚动条
    scroll = tkinter.Scrollbar(a6)
    scroll.pack(side="right", fill="y")
    note_text.config(yscrollcommand=scroll.set)
    scroll.config(command=note_text.yview)

    result_label=tkinter.Label(a3, text='', font=('Microsoft YaHei', 26), fg='black', bg='#FFF0F5')
    result_label.place(x=200, y=300)
    tkinter.Label(a3, text='请输入你猜测的四位数字: ', font=('Microsoft YaHei', 26), fg='black', bg='#FFF0F5').place(x=100, y=100)
    s1=tkinter.StringVar()
    tkinter.Entry(a3, textvariable=s1, width=10, font=('黑体', 26), fg='#F0FFFF', bg='#F5DEB3').place(x=350, y=200)
    def ask():
        user_input=s1.get()
        if user_input.isdigit() and len(user_input)==4 :
            y=int(user_input)
            if y == x:
                a5 = tkinter.Toplevel()
                a5.title('成功')
                a5.geometry(f'{int(w / 4)}x{int(h / 4)}+{int(w / 2)}+{int(h / 4)}')
                a5.resizable(False, False)
                a5.iconbitmap("Logo.ICO")
                a5.configure(bg="#FFF0F5")
                tkinter.Label(a5, text='YOU ARE RIGHT!', font=('Microsoft YaHei', 26), fg='black', bg='#FFF0F5').place(x=10, y=10)
                tkinter.Label(a5, text='Congratulations~', font=('Microsoft YaHei', 26), fg='black', bg='#FFF0F5').place(x=10, y=100)
                def bye():
                    a5.destroy()
                    a3.destroy()
                tkinter.Button(a5, command=bye, text='拜拜', font=('黑体', 26), width=5, bg='#F5DEB3').place(x=150,y=180)
            else:
                s2 = str(user_input)
                g1, b1, c1, d1 = int(s2[0]), int(s2[1]), int(s2[2]), int(s2[3])
                flag = 0
                if a == g1:
                    flag += 1
                if b == b1:
                    flag += 1
                if c == c1:
                    flag += 1
                if d == d1:
                    flag += 1
                result_label.config(text=f"你猜对了：{flag}个数字")

        else:
            messagebox.showwarning('输入不合法', '请输入四位纯数字')
            return
    tkinter.Button(a3, command=ask, text='查询', font=('黑体', 26), width=5, bg='#F5DEB3').place(x=300, y=400)


def help():
    a4 = tkinter.Toplevel()
    a4.title('规则讲解')
    a4.geometry(f'{int(w / 2)}x{int(h / 2)}+{int(w / 4)}+{int(h / 4)}')
    a4.resizable(False, False)
    a4.iconbitmap("Logo.ICO")
    a4.configure(bg="#FFF0F5")
    def helpover():
        a4.destroy()
    #规则界面标签组件
    tkinter.Label(a4, text='详细规则如下：',font=('Microsoft YaHei', 26), fg='black', bg='#FFF0F5').place(x=20, y=20)
    tkinter.Label(a4, text='''
    1. 系统随机生成一个四位数；
    2. 你输入四位数字进行猜测，点击查询；
    3. 系统会提示你猜对了几个数字；
    4. 全部猜对即为成功，可重新开始新一局；
    5. 只能输入四位纯数字，否则视为输入不合法;
    ''',justify='left',font=('Microsoft YaHei', 26), fg='black', bg='#FFF0F5').place(x=1, y=80)
    tkinter.Button(a4, command=helpover, text='I understand', font=('黑体', 26), width=20, bg='#F5DEB3').place(x=200, y=400)


#设置窗口关闭时执行的函数
a1.protocol('WM_DELETE_WINDOW',close)
#欢迎词标签组件
a2=tkinter.Label(a1,text='Number Puzzle',font=('Microsoft YaHei',26),fg='black',bg='#FFF0F5')
a2.place(x=100,y=100)
#开始游戏按钮组件
tkinter.Button(a1,command=start,text='start!',font=('Microsoft YaHei',26),fg='black',bg='#FFF0F5').place(x=300,y=300)
tkinter.Button(a1,command=help,text='help',font=('Microsoft YaHei',26),fg='black',bg='#FFF0F5').place(x=450,y=300)
#开启窗口/主循环
a1.mainloop()
