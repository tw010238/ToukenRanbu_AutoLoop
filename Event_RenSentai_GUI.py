import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import toukenranbu_normal_stage_loop as tkrb
import pyautogui
import time
from moyooshimono_senriyokukakujuu import senriyokukakujuu_loop as event
def ERS_win():
    '''主畫面'''
    ERS_win = tk.Tk()
    ERS_win.title('tokenranbu_loop')
    ERS_win.geometry("180x750+0+220")
    ERS_win.iconbitmap(r'other_img\icon.ico')
    ERS_win.resizable(width=False,height=False)
    ERS_win.attributes('-topmost',True)


    '''簡介'''
    reminder = tk.Label(text='請登入至本丸畫面\n再啟動Loop\n-----------------------------',font=20)
    reminder.pack()

    '''返回戰場選擇'''
    reminder = tk.Label(text="催物 - 連戰隊",font=20)
    reminder.place(anchor='center',x=90,y=80)
    def return_BFC():
        ERS_win.destroy()


    switch_button = tk.Button(ERS_win, text='返回戰場選擇',command=return_BFC)
    switch_button.place(anchor='center',x=90,y=115)

    reminder = tk.Label(text='-----------------------------',font=20)
    reminder.place(x=0,y=131)



    '''下拉選單'''
    reminder = tk.Label(text = '周回設定',font=20)
    reminder.place(anchor='center',x=90,y=170)
    reminder = tk.Label(text = '--難度選擇--',font=20)
    reminder.place(anchor='center',x=90,y=200)
    box1 = ttk.Combobox(ERS_win,values=['難易度‧易','難易度‧普','難易度‧難','難易度‧超難'],width=15)
    box1.place(anchor='center',x=90,y=230)
    reminder = tk.Label(text = '--小判補充--',font=20)
    reminder.place(anchor='center',x=90,y=260)
    box2 = ttk.Combobox(ERS_win,values=['不補充','單個補充','三個補充','全部補充'],width=15)
    box2.place(anchor='center',x=90,y=290)
    reminder = tk.Label(text = '--部隊選擇--',font=20)
    reminder.place(anchor='center',x=90,y=320)
    box3 = ttk.Combobox(ERS_win,values=['一','二','三','四','五'],width=15)
    box3.place(anchor='center',x=90,y=350)
    divider = tk.Label(text= '-----------------------------------')
    divider.place(anchor='center',x=90,y=380)


    '''有限循環'''
    loop_time1= tk.Label(text='指定次數循環',font=16)
    loop_time1.place(anchor='center',x=90,y=410)
    loop_time2= tk.Label(text='請輸入循環次數(正整數)')
    loop_time2.place(anchor='center',x=90,y=440)

    inputbox = tk.Entry(width=18)
    inputbox.place(anchor='center',x=90,y=470)

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
    btn1.place(anchor='center',x=90,y=500)

    divider = tk.Label(text= '-----------------------------------')
    divider.place(anchor='center',x=90,y=530)

    '''無限循環'''
    infinite_loop_label = tk.Label(text='無限循環',font=16)
    infinite_loop_label.place(anchor='center',x=90,y=560)

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
    infinite_loop.place(anchor='center',x=90,y=590)

    divider = tk.Label(text= '-----------------------------------')
    divider.place(anchor='center',x=90,y=620)

    '''停止'''
    stop_label = tk.Label(text='網頁左上沒有DMM\n就會停止程式\n請以切螢幕的方式\n遮住網頁左上的DMM')
    stop_label.place(anchor='center',x=90,y=675)

    reminder = tk.Label(text='進關隊伍刀裝記得更改',foreground='red')
    reminder.place(anchor='center',x=90,y=730)

    ERS_win.mainloop()

# ERS_win()

