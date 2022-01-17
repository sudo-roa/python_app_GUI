import tkinter as tk
import random

# トップレベルウィンドウの生成
root = tk.Tk()
root.title('おみくじ')
root.geometry('400x200')

# ハンドラ関数
def omikuzi():
    luck = ['大吉', '中吉', '小吉', '吉', '小吉', '末吉', '凶', '大凶']
    unsei = random.choice(luck)
    label['text'] = unsei


# Labelウィジェットの生成と配置
# 生成
label = tk.Label(root,
                 text='今日の運勢は？',
                 padx=5,
                 pady=5,
                 relief=tk.SUNKEN,
                 foreground='red')
# 配置
label.pack(pady=50,fill=tk.BOTH)

# Buttonウィジェットの生成と配置
button = tk.Button(root,
                   text='クリックでおみくじを引く',
                   command=omikuzi,)
button.pack()

root.mainloop()