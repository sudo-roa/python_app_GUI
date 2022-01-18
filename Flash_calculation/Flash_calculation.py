import tkinter as tk
import random
import time
import threading

####################内部処理####################
#ボタンのイベント内にいくつもの画面更新処理を入れると固まるので、Threadingでフリーズを回避
def start_clicked():
    thread1 = threading.Thread(target=Flash)
    thread1.start()

def Flash():
    global sum 
    global random_num
    random_num = [0,0,0,0,0,0,0,0,0,0]
    for i in range(0,3):
        random_num[i] = random.randint(10,99)
        label_q['text']=str(random_num[i])
        time.sleep(0.5)
    #tkinterはイベント内で自己代入ができない(sum = sum + numberのようなもの)
    sum = random_num[0]+random_num[1]+random_num[2] 
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
root.geometry('400x200')

#label
label_q = tk.Label(root, text='ここに問題が表示されます')
message = tk.Label(root, text='準備がよければstartを押してください') 

#button
button_start = tk.Button(root, text='start', command=start_clicked)
button_answer = tk.Button(root, text='answer', command=answer_clicked)

#entry
entry_answer = tk.Entry(width=5)

#ウィンドウ内の配置
#     question
#     [start]
#  [entry]  [answer]
#     message
#2列
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
#4行
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)

label_q.grid(column=0, row=0, columnspan=2)
button_start.grid(column=0, row=1, columnspan=2)
entry_answer.grid(column=0, row=2, sticky=tk.E)
button_answer.grid(column=1, row=2, sticky=tk.W)
message.grid(column=0, row=3, columnspan=2)

root.mainloop()

