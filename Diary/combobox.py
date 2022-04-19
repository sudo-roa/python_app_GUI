import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

# リスト項目の作成（config）
weather = ('快晴', '晴れ', '曇り', '雨', '雪', '台風', '晴れのち曇り', 
            '晴れのち雨', '晴れのち雪', '曇りのち晴れ', '曇りのち雨', 
            '曇りのち雪', '雨のち晴れ', '雨のち曇り', '雨のち雪', 
            '雪のち晴れ', '雪のち曇り', '雪のち雨')


# トップレベルウィンドウの生成
root = tk.Tk()
root.geometry('300x100')
root.title('Comboboxのテスト')

# Comboboxウィジェットの生成と配置
combo = ttk.Combobox(root,
                    state='readonly',
                    values=weather)
combo.current(1)
combo.grid(row=0, column=0, columnspan=2)

# ハンドラ関数
def click_get():
    messagebox.showinfo('message', combo.get())

def click_set():
    combo.current(5)

# Buttonウィジェットの生成と配置
button_1 = tk.Button(root, text='show', command=click_get)
button_1.grid(row=1, column=0)
button_2 = tk.Button(root, text='set', command=click_set)
button_2.grid(row=1, column=1)

# トップレベルウィンドウの表示
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.mainloop()