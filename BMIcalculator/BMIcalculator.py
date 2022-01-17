import tkinter as tk

def calcBMI(weight, height):
    height = height/100
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
label_cm = tk.Label(root, text='cm')
message = tk.Label(root, text='体重と身長を入力し、BMIを判定を押してください')


entry_w = tk.Entry(width=5)
entry_h = tk.Entry(width=5)

def BMIresult():
    w = float(entry_w.get())
    h = float(entry_h.get())
    label_input_kg =tk.Label(root, text=w)
    label_input_cm =tk.Label(root, text=h)
    BMI = round(calcBMI(w,h),2)
    result= check(BMI)
    message['text']="BMIは",BMI,"で",str(result),"です。"
    entry_w.grid_remove()
    entry_h.grid_remove()
    label_input_kg.grid(column=1, row=0)
    label_input_cm.grid(column=1, row=1)


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
# 身長   [h]   cm 
#     [button]
# [    message    ]

label_w.grid(column=0, row=0, sticky=tk.E)
entry_w.grid(column=1, row=0)
label_kg.grid(column=2, row=0, sticky=tk.W)

label_h.grid(column=0, row=1, sticky=tk.E)
entry_h.grid(column=1, row=1)
label_cm.grid(column=2, row=1, sticky=tk.W)

#columnの指定の仕方->0から3マス分
button.grid(column=0, row=2, columnspan=3)

message.grid(column=0, row=3, columnspan=3)

root.mainloop()

