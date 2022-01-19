import tkinter as tk
import random
import time
import threading

####################内部処理####################
#ボタンのイベント内にいくつもの画面更新処理を入れると固まるので、Threadingでフリーズを回避
def start_clicked():
    thread1 = threading.Thread(target=Flash)
    thread1.start()

def Generate_randint():
    if scale_keta.get()==1:
        return random.randint(1, 9)
    elif scale_keta.get()==2:
        return random.randint(10,99)
    elif scale_keta.get()==3:
        return random.randint(100,999)
    elif scale_keta.get()==4:
        return random.randint(1000,9999)
    elif scale_keta.get()==5:
        return random.randint(10000,99999)
    elif scale_keta.get()==6:
        return random.randint(100000,999999)
    elif scale_keta.get()==7:
        return random.randint(1000000,9999999)
    elif scale_keta.get()==8:
        return random.randint(10000000,99999999)
    elif scale_keta.get()==9:
        return random.randint(100000000,999999999)



def Flash():
    global sum 
    global random_num
    random_num = [0,0,0,0,0,0,0,0,0,0]
    for i in range(0,scale_kazu.get()):
        random_num[i] = Generate_randint()
        label_q['text']=str(random_num[i])
        time.sleep(scale_speed.get())
    #tkinterはイベント内で自己代入ができない(sum = sum + numberのようなもの)
    sum = random_num[0]+random_num[1]+random_num[2]+random_num[3]+random_num[4]+random_num[5]+random_num[6]+random_num[7]+random_num[8]+random_num[9] 
    label_q['text']="答えを入力してanswerを押してください。"

def answer_clicked():
    answer = entry_answer.get()
    if int(answer) == sum:
        message['text']="正解です!!"
    else:
        message['text']="残念!!答えは",str(sum),"です。"

####################ウィンドウ####################
#トップレベルウィンドウ
root = tk.Tk()
root.title('Flash Calcutation')
root.geometry('400x300')

#label
label_q = tk.Label(root, text='ここに問題が表示されます')
message = tk.Label(root, text='準備がよければstartを押してください') 
label_speed = tk.Label(root, text='表示速度')
label_kazu = tk.Label(root, text='出題される数字の数')
label_keta = tk.Label(root, text='整数の桁数')

#button
button_start = tk.Button(root, text='start', command=start_clicked)
button_answer = tk.Button(root, text='answer', command=answer_clicked)

#entry
entry_answer = tk.Entry(width=5)

#scale
speed = tk.DoubleVar()
scale_speed = tk.Scale(root, 
            variable = speed, 
            orient=tk.HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
            length = 150,           # 全体の長さ
            width = 20,             # 全体の太さ
            sliderlength = 10,      # スライダー（つまみ）の幅
            from_ = 0.1,            # 最小値（開始の値）
            to = 2.1,               # 最大値（終了の値）
            resolution=0.1,         # 変化の分解能(初期値:1)
            tickinterval=1)        # 目盛りの分解能(初期値0で表示なし)

kazu = tk.IntVar()
scale_kazu = tk.Scale(root, 
            variable = kazu, 
            orient=tk.HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
            length = 150,           # 全体の長さ
            width = 20,             # 全体の太さ
            sliderlength = 10,      # スライダー（つまみ）の幅
            from_ = 1,            # 最小値（開始の値）
            to = 10,               # 最大値（終了の値）
            resolution=1,         # 変化の分解能(初期値:1)
            tickinterval=3)        # 目盛りの分解能(初期値0で表示なし)

keta = tk.IntVar()
scale_keta = tk.Scale(root, 
            variable = keta, 
            orient=tk.HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
            length = 150,           # 全体の長さ
            width = 20,             # 全体の太さ
            sliderlength = 10,      # スライダー（つまみ）の幅
            from_ = 1,            # 最小値（開始の値）
            to = 9,               # 最大値（終了の値）
            resolution=1,         # 変化の分解能(初期値:1)
            tickinterval=2)        # 目盛りの分解能(初期値0で表示なし)

#ウィンドウ内の配置
#########################
#        question       # 
#        [start]        #
#   [entry]  [answer]   #
#        message        #
#  speed  [scale_speed] #
#  kazu   [scale_kazu]  #
#  keta   [scale_keta]  #
#########################

#2列
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
#4行
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)

label_q.grid(column=0, row=0, columnspan=2)
button_start.grid(column=0, row=1, columnspan=2)
entry_answer.grid(column=0, row=2, sticky=tk.E)
button_answer.grid(column=1, row=2, sticky=tk.W)
message.grid(column=0, row=3, columnspan=2)
label_speed.grid(column=0, row=4, sticky=tk.E)
scale_speed.grid(column=1, row=4, sticky=tk.W)
label_kazu.grid(column=0, row=5, sticky=tk.E)
scale_kazu.grid(column=1, row=5, sticky=tk.W)
label_keta.grid(column=0, row=6, sticky=tk.E)
scale_keta.grid(column=1, row=6, sticky=tk.W)

root.mainloop()

