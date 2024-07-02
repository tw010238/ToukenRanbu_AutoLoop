import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import toukenranbu_normal_stage_loop as tkrb
import pyautogui
import time
from moyooshimono_senriyokukakujuu import senriyokukakujuu_loop as event
'''主畫面'''
win = tk.Tk()
win.title('tokenranbu_loop')
win.geometry("180x750+0+200")
win.iconbitmap(r'other_img\icon.ico')
win.resizable(width=False,height=False)
win.attributes('-topmost',True)


'''簡介'''
reminder = tk.Label(text='請登入至本丸畫面\n再啟動Loop\n-----------------------------',font=20)
reminder.pack()

'''合戰場/催物 切換'''
reminder = tk.Label(text="戰場選擇",font=16)
reminder.pack()
BattleField = tk.StringVar()
radio_btn1 = tk.Radiobutton(win, text='合戰場',variable=BattleField, value=1)
radio_btn1.place(x=0,y=90,width=85,height=30)
radio_btn1.select()  # 搭配 select() 方法選取 radio_btn1

radio_btn2 = tk.Radiobutton(win, text='催物',variable=BattleField, value=2)
radio_btn2.place(x=90,y=90,width=85,height=30)

reminder = tk.Label(text='-----------------------------',font=20)
reminder.place(x=0,y=115)


'''下拉選單'''
reminder = tk.Label(text = '合戰場 周回設定',font=20)
reminder.place(anchor='center',x=90,y=155)
reminder = tk.Label(text = '--時代選擇--',font=20)
reminder.place(anchor='center',x=90,y=185)
box1 = ttk.Combobox(win,values=['一','二','三','四','五','六','七','八'],width=15)
box1.place(anchor='center',x=90,y=215)
reminder = tk.Label(text = '--地域(難度)選擇--',font=20)
reminder.place(anchor='center',x=90,y=245)
box2 = ttk.Combobox(win,values=['一','二','三','四'],width=15)
box2.place(anchor='center',x=90,y=275)
reminder = tk.Label(text = '--部隊選擇--',font=20)
reminder.place(anchor='center',x=90,y=305)
box3 = ttk.Combobox(win,values=['一','二','三','四','五'],width=15)
box3.place(anchor='center',x=90,y=335)
divider = tk.Label(text= '-----------------------------------')
divider.place(anchor='center',x=90,y=365)


'''有限循環'''
loop_time1= tk.Label(text='指定次數循環',font=16)
loop_time1.place(anchor='center',x=90,y=395)
loop_time2= tk.Label(text='請輸入循環次數(正整數)')
loop_time2.place(anchor='center',x=90,y=425)

inputbox = tk.Entry(width=18)
inputbox.place(anchor='center',x=90,y=455)

def limited_loop():
    if box1.get() == "" or box2.get() == "" or box3.get() == "":
        loop_time2.config(text='請先完成周回設定', foreground='red')
        return
    time.sleep(2)
    try:
        limit = int(inputbox.get())
        count = 0
        while limit > count:
            loop_time2.config(text=f'已完成：{count}/{limit}')
            tkrb.loop(box1.get(),box2.get(),box3.get())
            try:
                pyautogui.locateOnScreen(r'button\DMM GAMES.PNG')
                count += 1
            except:
                break
            try:
                pyautogui.locateOnScreen(r'button\warnning1.PNG', confidence=0.9, grayscale=True)
                tkinter.messagebox.showwarning(title='刀劍重傷警告!!',
                                               message='刀劍重傷，繼續行軍可能造成刀劍破壞，周回功能強制結束。')
                break
            except:
                pass
        loop_time2.config(text='請輸入循環次數(正整數)')
    except:
        loop_time2.config(text='輸入錯誤，請輸入正整數',foreground='red')


btn1 = tk.Button(text='確定',font=16)
btn1.config(command=limited_loop)
btn1.place(anchor='center',x=90,y=485)

divider = tk.Label(text= '-----------------------------------')
divider.place(anchor='center',x=90,y=515)

'''無限循環'''
infinite_loop_label = tk.Label(text='無限循環',font=16)
infinite_loop_label.place(anchor='center',x=90,y=545)

infinite_loop = tk.Button(text= '開始',font=16)
def infinite_loop_start():
    time.sleep(2)
    count = 0
    while True:
        infinite_loop_label.config(text =f'無限循環(完成{count})',font=16)
        tkrb.loop(box1.get(), box2.get(), box3.get())
        try:
            pyautogui.locateOnScreen(r'button\DMM GAMES.PNG')
            count += 1
        except:
            break
        try:
            pyautogui.locateOnScreen(r'button\warnning1.PNG', confidence=0.9, grayscale=True)
            tkinter.messagebox.showwarning(title='刀劍重傷警告!!', message='刀劍重傷，繼續行軍可能造成刀劍破壞，周回功能強制結束。')
            break
        except:
            pass
    infinite_loop_label.config(text='無限循環',font=16)

infinite_loop.config(command=infinite_loop_start)
infinite_loop.place(anchor='center',x=90,y=575)

divider = tk.Label(text= '-----------------------------------')
divider.place(anchor='center',x=90,y=605)

'''停止'''
stop_label = tk.Label(text='網頁左上沒有DMM\n就會停止程式\n請以切螢幕的方式\n遮住網頁左上的DMM')
stop_label.place(anchor='center',x=90,y=660)


#
win.mainloop()