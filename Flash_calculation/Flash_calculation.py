import tkinter as tk
import random
import time

result=0

def Flash():
    for num in range(2):
        number = random.randint(1, 3)
        number_char = str(number)
        sum += number
        time.sleep(0.5)
        label_q['text']=str(number_char)
    message['text']=str(sum)


def AnswerComparison(result_a):
    return 0

#トップレベルウィンドウ
root = tk.Tk()
root.title('Flash_calcutation')
root.geometry('400x200')

#label
label_q = tk.Label(root, text='ここに問題が表示されます')
message = tk.Label(root, text='準備がよければstartを押してください') 

#button
button_start = tk.Button(root, text='start', command=Flash)
button_answer = tk.Button(root, text='answer', command=AnswerComparison)
#entry

entry_answer = tk.Entry(width=5)

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

