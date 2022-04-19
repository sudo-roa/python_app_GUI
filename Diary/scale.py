import tkinter as tk
from tkinter import messagebox

# トップレベルウィンドウの生成
root = tk.Tk()
root.geometry('300x100')
root.title('Scaleテスト')

# Scaleウィジェットの生成と配置
sclH = tk.Scale(root,
                orient=tk.HORIZONTAL,   # 水平のバーに設定
                from_ = 1,   # 開始の値を1にする
                length = 200)   # バーの長さを200にする
sclH.grid(row=0, column=0, columnspan=2)

# ハンドラ関数
def click_get():
    messagebox.showinfo('メッセージ', sclH.get())   # scaleウィジェットの値を取得

def click_set():
    sclH.set(50)   # ウィジェットの値を50にする

# Buttonウィジェットの生成と配置
button_1 = tk.Button(root, text='表示', command=click_get)
button_1.grid(row=1, column=0)

button_2 = tk.Button(root, text='設定', command=click_set)
button_2.grid(row=1, column=1)

# トップレベルウィンドウの表示
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.mainloop()
