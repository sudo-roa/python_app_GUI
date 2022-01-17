import tkinter as tk

def calcBMI(weight, height):
    return weight/(height**2)

def check(bmi):
    if bmi<18.5:
        result = '低体重'
    elif bmi<25.0:
        result = '普通体重'
    elif bmi<30.0:
        result = '肥満度１'
    elif bmi<35.0:
        result = '肥満度２'
    elif bmi<40.0:
        result = '肥満度３'
    else:
        result = '肥満度４'
    return result

#トップレベルウィンドウ
root = tk.Tk()
root.title('BMIcalculator')
root.geometry('400x200')

label_w = tk.Label(root, text='体重')
label_kg = tk.Label(root, text='kg')
label_h = tk.Label(root, text='身長')
label_m = tk.Label(root, text='m')
message = tk.Label(root, text='体重と身長を入力してください')

entry_w = tk.Entry(width=5)
entry_h = tk.Entry(width=5)

def BMIresult():
    w = float(entry_w.get())
    h = float(entry_h.get())
    result= check(calcBMI(w,h))
    message['text']=str(result)

button = tk.Button(root, text='BMIを判定', command=BMIresult)

#3列
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
#4行
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)

# 体重   [w]   kg
# 身長   [h]   m 
#     [button]
# [    message    ]

label_w.grid(column=0, row=0, sticky=tk.E)
entry_w.grid(column=1, row=0)
label_kg.grid(column=2, row=0, sticky=tk.W)

label_h.grid(column=0, row=1, sticky=tk.E)
entry_h.grid(column=1, row=1)
label_m.grid(column=2, row=1, sticky=tk.W)

#columnの指定の仕方->0から3マス分
button.grid(column=0, row=2, columnspan=3)

message.grid(column=0, row=3, columnspan=3)

root.mainloop()

