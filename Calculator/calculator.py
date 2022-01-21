import tkinter as tk
from tkinter import font

flag = 0
calcflag = 0

def input_number(num_char):
    global flag
    global num1
    global num2
    if(flag==0):
        label_screen["text"] = num_char
        flag = 1
        num1=int(label_screen["text"])
    elif(flag==1):
        label_screen["text"] = label_screen["text"]+num_char
        num1=int(label_screen["text"])
    if(flag==2):
        label_screen["text"] = num_char
        flag = 3
        num2=int(label_screen["text"])
    elif(flag==3):
        label_screen["text"] = label_screen["text"]+num_char
        num2=int(label_screen["text"])
    print("input_number")

def input_symbol(symbol):
    global flag

    flag=2
    print("input_symbol")
    calc(symbol)

def calc(symbol):
    global num1
    global num2
    global flag
    global calcflag
    print("calc_dayo")
    if(symbol=="+"):
        print("+dayo")
        calcflag=1
    elif(symbol=="-"):
        calcflag=2
        print("-dayo")
    elif(symbol=="*"):
        calcflag=3
        print("*dayo")
    elif(symbol=="/"):
        calcflag=4
        print("/dayo")
    elif(symbol=="="):
        flag = 0
        if(calcflag==1):
            label_screen["text"] = num1+num2
        elif(calcflag==2):
            label_screen["text"] = num1-num2
        elif(calcflag==3):
            label_screen["text"] = num1*num2
        elif(calcflag==4):
            label_screen["text"] = num1/num2
    elif(symbol=="CR"):
        flag=0
        label_screen["text"] = ""

#window
root = tk.Tk()
root.title("calculator")
root.geometry("600x600")

label_screen = tk.Label(root, text="", font=300)

#button
btn_0 = tk.Button(root, text='0', font=200, command=lambda:input_number("0"))
btn_1 = tk.Button(root, text='1', font=200, command=lambda:input_number("1"))
btn_2 = tk.Button(root, text='2', font=200, command=lambda:input_number("2"))
btn_3 = tk.Button(root, text='3', font=200, command=lambda:input_number("3"))
btn_4 = tk.Button(root, text='4', font=200, command=lambda:input_number("4"))
btn_5 = tk.Button(root, text='5', font=200, command=lambda:input_number("5"))
btn_6 = tk.Button(root, text='6', font=200, command=lambda:input_number("6"))
btn_7 = tk.Button(root, text='7', font=200, command=lambda:input_number("7"))
btn_8 = tk.Button(root, text='8', font=200, command=lambda:input_number("8"))
btn_9 = tk.Button(root, text='9', font=200, command=lambda:input_number("9"))

btn_plus = tk.Button(root, text='+', font=200, command=lambda:input_symbol("+"))
btn_minus = tk.Button(root, text='-', font=200, command=lambda:input_symbol("-"))
btn_multi = tk.Button(root, text='*', font=200, command=lambda:input_symbol("*"))
btn_div = tk.Button(root, text='/', font=200, command=lambda:input_symbol("/"))
btn_clear = tk.Button(root, text='CR', font=200, command=lambda:input_symbol("CR"))
btn_dot = tk.Button(root, text='.', font=200, command=lambda:input_symbol("."))
btn_equal = tk.Button(root, text='=', font=200, command=lambda:input_symbol("="))

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)

########################################
# [        ] [CR]
# [7] [8] [9] [+]
# [4] [5] [6] [-]
# [1] [2] [3] [*]
# [0] [.] [=] [/]

label_screen.grid(column=0, row=0, columnspan=3, sticky=tk.NSEW)
btn_clear.grid(column=3, row=0, sticky=tk.NSEW)
btn_7.grid(column=0, row=1, sticky=tk.NSEW)
btn_8.grid(column=1, row=1, sticky=tk.NSEW)
btn_9.grid(column=2, row=1, sticky=tk.NSEW)
btn_plus.grid(column=3, row=1, sticky=tk.NSEW)
btn_4.grid(column=0, row=2, sticky=tk.NSEW)
btn_5.grid(column=1, row=2, sticky=tk.NSEW)
btn_6.grid(column=2, row=2, sticky=tk.NSEW)
btn_minus.grid(column=3, row=2, sticky=tk.NSEW)
btn_1.grid(column=0, row=3, sticky=tk.NSEW)
btn_2.grid(column=1, row=3, sticky=tk.NSEW)
btn_3.grid(column=2, row=3, sticky=tk.NSEW)
btn_multi.grid(column=3, row=3, sticky=tk.NSEW)
btn_0.grid(column=0, row=4, sticky=tk.NSEW)
btn_dot.grid(column=1, row=4, sticky=tk.NSEW)
btn_equal.grid(column=2, row=4, sticky=tk.NSEW)
btn_div.grid(column=3, row=4, sticky=tk.NSEW)

root.mainloop()