import tkinter as tk
import datetime as da
import calendar as ca
from tkinter import messagebox

# 最初に設定情報を入力
WEEK = ['日', '月', '火', '水', '木', '金', '土']
WEEK_COLOUR = ['red', 'black', 'black', 'black', 'black', 'black', 'blue']

# 表示するカレンダーの生成
def disp(arg):   # argが-1なら先月、1なら翌月を表示
    global yer
    global mon

    mon[0] += arg

    # 年を跨ぐ処理と年月の表示
    if mon[0] < 1:
        mon[0], yer[0] = 12, yer[0] - 1   # 表示する月が0月の場合は12月へ変更し年もあわせる
    elif mon[0] > 12:
        mon[0], yer[0] = 1, yer[0] + 1   # 表示する月が13月の場合は1月へ変更し年もあわせる
    label['text'] = str(yer[0]) + '年' + str(mon[0]) + '月'

    # pythonのカレンダーの取得
    cal = ca.Calendar(firstweekday=6)   # 日曜日始まりのカレンダーを生成
    cal = cal.monthdayscalendar(yer[0], mon[0])   # 表示する年月のカレンダーを取得(いろんな種類があるみたい)
    # cal2 = ca.Calendar(firstweekday=6)
    # cal2 = cal2.monthdatescalendar(yer[0], mon[0])
    # cal2 = cal2.monthdays2calendar(yer[0], mon[0])
    # cal2 = cal2.monthdayscalendar(yer[0], mon[0])
    
    # フレーム上のウィジェットを削除
    for widget in frame.winfo_children():
        widget.destroy()

    # １行目に曜日を表示
    r = 0
    for i,x in enumerate(WEEK):
        label_day = tk.Label(frame,   # r=0で曜日のLabelウィジェットを生成
                            text=x,
                            font=('', 10),
                            width=3,
                            fg=WEEK_COLOUR[i])   # 曜日に合わせて色を変える
        label_day.grid(row=r, column=i, pady=1)

    # ２行目以降日付を表示
    r = 1
    for week in cal:
        for i,day in enumerate(week):
            day = ' ' if day == 0 else day   # 日付が0の日は数字を表示しないようにする  
            label_day = tk.Label(frame,   # 日付のラベルウィジェットを生成
                            text=day,
                            font=('', 10),
                            fg=WEEK_COLOUR[i],
                            borderwidth=1)
            if(yer[0], mon[0], today) == (yer[1], mon[1], day):
                label_day['relief'] = 'solid'   # 今日なら枠を表示する
            label_day.bind('<Button-1>', click)   # 左クリックに対応したイベントをbindする
            label_day.grid(row=r, column=i, padx=2, pady=1)
        r = r + 1

# カレンダーの日付がクリックされた時のイベント
def click(event):
    t = event.widget['text']
    event.widget['background'] = 'gray'
    messagebox.showinfo('メッセージ', str(t) + '日です。')

# ウィンドの生成
root = tk.Tk()
root.title('カレンダー')
root.geometry('220x200')
root.resizable(0,0)   # ウィジェットのリサイズをできなくする

# 現在の年月日の取得
yer = [da.date.today().year] * 2
mon = [da.date.today().month] * 2
today = da.date.today().day

# ウィンドウの幅に合わせて列を均等に三分割
for n in range(3):
    root.grid_columnconfigure(n, weight=1)

# ボタン　年月　ボタンの表示（一行目）
label = tk.Label(root, font=('', 10))
button_1 = tk.Button(root,
                    text='<',
                    font=('', 10),
                    command= lambda:disp(1))
button_1.grid(row=0, column=0, pady=10)
label.grid(row=0, column=1)
button_2 = tk.Button(root,
                    text='>',
                    font=('', 10),
                    command=lambda:disp(1))
button_2.grid(row=0, column=2)

# カレンダーの日付表示（二行目）
frame = tk.Frame(root)
frame.grid(row=1, column=0, columnspan=3)
disp(0)

root.mainloop()




