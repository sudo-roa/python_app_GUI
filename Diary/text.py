import tkinter as tk
from tkinter import messagebox

# トップレベルウィンドウの生成
root = tk.Tk()
root.geometry('250x150')
root.title('Textテスト')

# Textウィジェットの生成と配置
text = tk.Text(root, width=30, height=6)
text.grid(row=0, column=0, columnspan=2)

# ハンドラ関数
def click_get():
    messagebox.showinfo('message', text.get('1.0', 'end'))
def click_set():
    text.delete('1.0', 'end')
    text.insert('1.0', 'あいうえお\nかきくけこ\nさしすせそ')

# Buttonウィジェットの生成と配置
button_1 = tk.Button(root, text='get', command=click_get)
button_1.grid(row=1, column=0)
button_2 = tk.Button(root, text='set', command=click_set)
button_2.grid(row=1, column=1)

# トップレベルウィンドウの表示 
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.mainloop()