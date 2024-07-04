from toukenranbu_GUI import NS_win
import tkinter as tk
from tkinter import ttk

def BFC():
    # 建立視窗
    main_win = tk.Tk()
    main_win.title('TouKenLoop')
    main_win.geometry("300x180+0+220")
    main_win.iconbitmap(r'other_img\icon.ico')
    main_win.resizable(width=False,height=False)
    main_win.attributes('-topmost',True)
    # 標題
    reminder = tk.Label(text='戰場選擇',font=20)
    reminder.place(anchor='center',x=150,y=25)
    #戰場選擇
    BFC_box = ttk.Combobox(main_win,values=['合戰場','催物','異化'],width=15)
    BFC_box.place(anchor='center',x=150,y=55)

    # 前往戰場(功能)
    def choose_battlefield():
        if BFC_box.get() == '合戰場':
            main_win.destroy()
            NS_win()

    # 前往戰場(按鍵)
    switch_button = tk.Button(main_win, text='戰場選擇',command=choose_battlefield)
    switch_button.place(anchor='center',x=150,y=95)

    # 關閉視窗(功能)
    def close_win():
        global close
        close = True
        main_win.destroy()
    # 關閉視窗(按鍵)
    close_button = tk.Button(main_win, text='關閉',command=close_win)
    close_button.place(anchor='center',x=150,y=135)

    main_win.mainloop()

# 不能互相引用，所以用loop
close = False
while True:
    BFC()
    if close:
        break