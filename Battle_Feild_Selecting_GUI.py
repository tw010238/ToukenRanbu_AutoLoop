import tkinter as tk


BFS_win = tk.Tk()

def switch_NS_win():
    BFS_win.destroy()


NS_win_button = tk.Button(text='確定',font=16)
NS_win_button.config(command=switch_NS_win)
NS_win_button.pack()




BFS_win.mainloop()