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
win.geometry("180x540+0+470")
win.iconbitmap(r'other_img\icon.ico')
win.resizable(width=False,height=False)
win.attributes('-topmost',True)


'''簡介'''
reminder = tk.Label(text='請登入至本丸畫面\n再啟動Loop\n-----------------------------',font=20)
reminder.pack()


'''下拉選單'''
reminder = tk.Label(text = '周回設定',font=20)
reminder.pack()
reminder = tk.Label(text = '--時代選擇--',font=20)
reminder.pack()
box1 = ttk.Combobox(win,values=['一','二','三','四','五','六','七','八','異去','催物'])
box1.pack()
reminder = tk.Label(text = '--地域(難度)選擇--',font=20)
reminder.pack()
box2 = ttk.Combobox(win,values=['一','二','三','四','其他'])
box2.pack()
reminder = tk.Label(text = '--部隊選擇--',font=20)
reminder.pack()
box3 = ttk.Combobox(win,values=['一','二','三','四','五'])
box3.pack()
divider = tk.Label(text= '-----------------------------------')
divider.pack()


'''有限循環'''
loop_time1= tk.Label(text='指定次數循環',font=16)
loop_time1.pack()
loop_time2= tk.Label(text='請輸入循環次數(正整數)')
loop_time2.pack()

inputbox = tk.Entry()
inputbox.pack()

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
            if box1.get() == "催物":
                event(box2.get(),box3.get())    # 這裡的函式根據遊戲目前活動，在最上面要import不同函式
            elif box1.get() == "異去":        # 待開發
                break
            else:
                tkrb.loop(box1.get(),box2.get(),box3.get())
            try:
                pyautogui.locateOnScreen(r'button\DMM GAMES.PNG')
                count += 1
            except:
                break
            try:
                pyautogui.locateOnScreen(r'button\warnning1.PNG', confidence=0.8, grayscale=True)
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
btn1.pack()

divider = tk.Label(text= '-----------------------------------')
divider.pack()

'''無限循環'''
infinite_loop_label = tk.Label(text='無限循環',font=16)
infinite_loop_label.pack()

infinite_loop = tk.Button(text= '開始',font=16)
def infinite_loop_start():
    time.sleep(2)
    count = 0
    while True:
        infinite_loop_label.config(text =f'無限循環(完成{count})',font=16)
        if box1.get() == "催物":
            event(box2.get(), box3.get())  # 這裡的函式根據遊戲目前活動，在最上面要import不同函式
        elif box1.get() == "異去":  # 待開發
            break
        else:
            tkrb.loop(box1.get(), box2.get(), box3.get())
        try:
            pyautogui.locateOnScreen(r'button\DMM GAMES.PNG')
            count += 1
        except:
            break
        try:
            pyautogui.locateOnScreen(r'button\warnning1.PNG', confidence=0.8, grayscale=True)
            tkinter.messagebox.showwarning(title='刀劍重傷警告!!', message='刀劍重傷，繼續行軍可能造成刀劍破壞，周回功能強制結束。')
            break
        except:
            pass
    infinite_loop_label.config(text='無限循環',font=16)

infinite_loop.config(command=infinite_loop_start)
infinite_loop.pack()

divider = tk.Label(text= '-----------------------------------')
divider.pack()

'''停止'''
stop_label = tk.Label(text='網頁左上沒有DMM\n就會停止程式')
stop_label.pack()


win.mainloop()