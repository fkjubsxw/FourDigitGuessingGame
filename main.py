import tkinter
from tkinter import Label, messagebox
import random
from PIL import Image,ImageTk

#创建主窗口a1
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
#首窗口配图
img=tkinter.PhotoImage(file="01.png")
img1=img.subsample(3,3)
label=tkinter.Label(a1,image=img1)
label.place(x=400,y=10)
#首窗口关闭确认弹窗函数
def close():
    d1=messagebox.askokcancel('关闭', '确认关闭？')
    if d1:
        pass
        # 销毁窗口/组件
        a1.destroy()
    else:
        messagebox.showinfo('关闭', "请继续游戏吧！")
#记录猜测次数，给出评语
round_count=1
#提前写全局变量
note_text=None
#开始按钮函数
def start():
    global note_text
    global x,a,b,c,d
    #每次开启游戏窗口就重新随机生成一个四位数
    x = random.randint(1000, 9999)
    #为方便调试可以查看答案
    print(x)
    #将答案的四个位数分别存入a,b,c,d
    s = str(x)
    a, b, c, d = int(s[0]), int(s[1]), int(s[2]), int(s[3])
    #新建游戏窗口a3
    a3 = tkinter.Toplevel()
    a3.title('游戏')
    a3.geometry(f'{int(w / 2)}x{int(h / 2)}+{int(w / 3)}+{int(h / 4)}')
    a3.resizable(False, False)
    a3.iconbitmap("Logo.ICO")
    a3.configure(bg="#FFF0F5")
    #与游戏窗口同步打开演草纸窗口a6
    a6 = tkinter.Toplevel()
    a6.title('演草纸')
    a6.geometry(f'{int(w / 3)}x{int(h / 2)}+{0}+{0}')
    a6.resizable(False, False)
    a6.iconbitmap("Logo.ICO")
    a6.configure(bg="#FFF0F5")
    # 加滚动条
    scroll = tkinter.Scrollbar(a6)
    scroll.pack(side="right", fill="y")
    #多行文本框
    note_text=tkinter.Text(a6,font=('黑体', 16), width=35,height=18)
    note_text.pack(padx=20,pady=10,fill='both',expand=True)
    note_text.config(yscrollcommand=scroll.set)
    #配置滚动条的命令
    scroll.config(command=note_text.yview)

    #给游戏窗口提前设置好结果语标签，之后写入内容
    result_label=tkinter.Label(a3, text='', font=('Microsoft YaHei', 26), fg='black', bg='#FFF0F5')
    result_label.place(x=200, y=300)
    # 给游戏窗口加提示语
    tkinter.Label(a3, text='请输入你猜测的四位数字: ', font=('Microsoft YaHei', 26), fg='black', bg='#FFF0F5').place(x=100, y=100)
    #给游戏窗口加输入框，并获取用户输入的答案
    s1=tkinter.StringVar()
    entry=tkinter.Entry(a3, textvariable=s1, width=10, font=('黑体', 26), fg='#F0FFFF', bg='#F5DEB3')
    entry.place(x=350, y=200)
    entry.bind('<Return>',lambda event:ask())
    #查询按钮绑定的函数，判断是否猜对或猜对个数
    def ask():
        global round_count
        global cuo_img,cuo_img1
        global dui_img,dui_img1
        global hang_img,hang_img1
        global ding_img,ding_img1
        global ren_img,ren_img1
        global n_img,n_img1
        global la_img,la_img1
        #加载评级图片——夯
        hang_img = tkinter.PhotoImage(file="夯.png")
        hang_img1 = hang_img.subsample(3, 3)
        label_a3_hang = tkinter.Label(a3, image=hang_img1)
        label_a3_hang.image = hang_img1
        # 加载评级图片——顶
        ding_img = tkinter.PhotoImage(file="顶.png")
        ding_img1 = ding_img.subsample(3, 3)
        label_a3_ding = tkinter.Label(a3, image=ding_img1)
        label_a3_ding.image = ding_img1
        # 加载评级图片——人上人
        ren_img = tkinter.PhotoImage(file="人.png")
        ren_img1 = ren_img.subsample(3, 3)
        label_a3_ren = tkinter.Label(a3, image=ren_img1)
        label_a3_ren.image = ren_img1
        # 加载评级图片——NPC
        n_img = tkinter.PhotoImage(file="n.png")
        n_img1 = n_img.subsample(3, 3)
        label_a3_n = tkinter.Label(a3, image=n_img1)
        label_a3_n.image = n_img
        # 加载评级图片——拉
        la_img = tkinter.PhotoImage(file="拉.png")
        la_img1 = la_img.subsample(3, 3)
        label_a3_la = tkinter.Label(a3, image=la_img1)
        label_a3_la.image = la_img1

        #将用户输入储存到user_input
        user_input=s1.get()
        #判断输入是纯数字以及是四位的
        if user_input.isdigit() and len(user_input)==4 :
            #输入没问题则转换成int型存入y
            y=int(user_input)
            #判断是否猜对
            if y == x:
                result_label.config(text=" ")
                # 猜对提示图片
                dui_img = tkinter.PhotoImage(file="对号.png")
                dui_img1 = dui_img.subsample(2, 2)
                label_a3_dui = tkinter.Label(a3, image=dui_img1)
                label_a3_dui.image = dui_img1
                label_a3_dui.place(x=10, y=250)
                label_a3_dui.lift()

                #猜对了则弹出祝贺窗口a5
                a5 = tkinter.Toplevel()
                a5.title('成功')
                a5.geometry(f'{int(w / 4)}x{int(h / 4)}+{int(w / 2)}+{int(h / 4)}')
                a5.resizable(False, False)
                a5.iconbitmap("Logo.ICO")
                a5.configure(bg="#FFF0F5")
                #用pillow加载原图
                zhuhe_img_original = Image.open("祝贺.png")
                #更新窗口，为获取宽和高
                a5.update_idletasks()
                #将图片大小更改为窗口大小
                w5,h5=a5.winfo_width(),a5.winfo_height()
                zhuhe_img_resized=zhuhe_img_original.resize((w5,h5),Image.Resampling.LANCZOS)
                #再转成tkinter可用的PhotoImage
                zhuhe_img=ImageTk.PhotoImage(zhuhe_img_resized)
                #记作标签
                label_a5_zhuhe = tkinter.Label(a5, image=zhuhe_img)
                label_a5_zhuhe.image = zhuhe_img
                label_a5_zhuhe.place(x=0, y=0,relwidth=1,relheight=1)
                label_a5_zhuhe.lower()
                #根据猜测次数round_count打开不同的评级图片
                if round_count<=5:
                    label_a3_hang.place(x=0, y=200)
                    label_a3_hang.lift()
                    #result_label.config(text=f"一共猜了：{round_count}次\n夯爆了!")

                elif round_count<=10:
                    label_a3_ding.place(x=0, y=200)
                    label_a3_ding.lift()
                    #result_label.config(text=f"一共猜了：{round_count}次\n顶级!")

                elif round_count<=15:
                    label_a3_ren.place(x=0, y=200)
                    label_a3_ren.lift()
                    #result_label.config(text=f"一共猜了：{round_count}次\n人上人")

                elif round_count<=20:
                    label_a3_n.place(x=0, y=200)
                    label_a3_n.lift()
                    #result_label.config(text=f"一共猜了：{round_count}次\nNPC")

                else:
                    label_a3_la.place(x=10, y=200)
                    label_a3_la.lift()
                    #result_label.config(text=f"一共猜了：{round_count}次\n拉完了！")

                #祝贺窗口拜拜按钮绑定函数
                def bye():
                    a5.destroy()
                    a3.destroy()
                #祝贺窗口的拜拜按钮
                tkinter.Button(a5, command=bye, text='拜拜', font=('黑体', 26), width=5, bg='#FFF0F5').place(x=200,y=180)
                s1.set("")
            #如果没有一次猜对
            else:
                #将输入转换成字符串并分离位数
                s2 = str(user_input)
                g1, b1, c1, d1 = int(s2[0]), int(s2[1]), int(s2[2]), int(s2[3])
                flag = 0
                #分别比较每一位数并记录答对个数
                if a == g1:
                    flag += 1
                if b == b1:
                    flag += 1
                if c == c1:
                    flag += 1
                if d == d1:
                    flag += 1
                #将猜错的数字和正确个数自动写入演草纸
                note_text.insert("end",f"{y} : {flag}\n")
                note_text.see("end")
                #猜错提示图片
                cuo_img = tkinter.PhotoImage(file="错号.png")
                cuo_img1 = cuo_img.subsample(3, 3)
                label_a3_cuo= tkinter.Label(a3, image=cuo_img1)
                label_a3_cuo.image =cuo_img1
                label_a3_cuo.place(x=10, y=100)
                label_a3_cuo.lower()
                #猜对位数提示语
                result_label.config(text=f"你猜对了：{flag}个数字")
                round_count+=1
                s1.set("")

        else:
            #输入不是四位数字弹出的提示语
            messagebox.showwarning('输入不合法', '请输入四位纯数字')
            return
    #部署查询按钮
    tkinter.Button(a3, command=ask, text='查询', font=('黑体', 26), width=5, bg='#FFF0F5').place(x=300, y=400)

#help按钮绑定的函数
def help():
    #新建规则讲解窗口a4
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
    3. 系统会提示你猜对了几个数字,并在草稿纸上显示：你猜测的数字 ：猜对的个数；
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
