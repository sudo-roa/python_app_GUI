import tkinter as tk
from tkinter import messagebox

# トップレベルウィンドウの生成
root = tk.Tk()
root.geometry('350x100')
root.title('Radiobuttonテスト')

# ラジオボタンを配置するフレーム
frame = tk.Frame(root)
for i in range(5):        
    frame.grid_columnconfigure(i, weight=1)   # 横に並ぶ5個のラジオボタンをフレーム内に均一に並べる

action = ['出社', 'テレワーク', '外回り', '出張', '休日']
var = tk.IntVar(value=1)   # 選択状態をint型で保持する(初期値は1)

# Radiobuttonウィジェットの生成と配置
for i, act in enumerate(action):
    radio = tk.Radiobutton(frame,   # フレームを親に
                            text=act,   # actを表示するテキストに指定
                            variable=var,   # IntVar関数で初期化した変数を設定
                            value=i)   # ラジオボタンの値
    radio.grid(row=0, column=i)
frame.grid(row=0, column=0, columnspan=2)

# ハンドラ関数
def click_get():
    messagebox.showinfo('message', action[var.get()])   # オンになってるラジオボタンの値を取得

def click_set():
    var.set(4)   # 5番目のラジオボタンをオンにする

# Buttonウィジェットの生成と配置
button_1 = tk.Button(root, text='get', command=click_get)
button_1.grid(row=1, column=0)
button_2 = tk.Button(root, text='set', command=click_set)
button_2.grid(row=1, column=1)

# トップレベルウィンドウの表示
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.mainloop()