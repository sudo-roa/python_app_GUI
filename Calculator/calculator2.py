import tkinter as tk
from tkinter import font

#初期化
# numflag
# num1の1文字目     0 
# num1の2文字目以降 1
# num2の1文字目     2
# num2の2文字目以降 3
numflag = 0

# zeroflag
# 0入力可能         0
# 0入力不可能       1
zeroflag = 0

# dotflag
# dot未入力         0
# dot入力済み       1
dotflag = 0

# opeflag
# clear後           0
# operation:+       1
# operation:-       2
# operation:*       3
# operation:/       4
opeflag = 0

num1 = 0
num2 = 0

#input number 
def input_number(num_char):
    global numflag
    global zeroflag
    global dotflag
    global opeflag
    global num1
    global num2
    if(numflag==0):
        numflag=1
        label_screen["text"] = num_char
        num1=int(label_screen["text"])
    elif(numflag==1):
        if(zeroflag == 0 and dotflag == 0):
            label_screen["text"] = label_screen["text"]+num_char
            num1=int(label_screen["text"])
        elif(zeroflag == 1):
            print("0の次に数字を入力できません")
        elif(dotflag == 1):
            label_screen["text"] = label_screen["text"]+num_char
            num1=float(label_screen["text"])
    elif(numflag==2):
        zeroflag = 0
        dotflag = 0
        numflag = 3
        label_screen["text"] = num_char
        num2=int(label_screen["text"])
    elif(numflag==3):
        if(zeroflag == 0 and dotflag == 0):
            label_screen["text"] = label_screen["text"]+num_char
            num2=int(label_screen["text"])
        elif(zeroflag == 1):
            print("0の次に数字を入力できません")
        elif(dotflag == 1):
            label_screen["text"] = label_screen["text"]+num_char
            num2=float(label_screen["text"])
    print("input_number")

# input number0
def input_number0(num_char):
    global numflag
    global zeroflag
    global dotflag
    global opeflag
    global num1
    global num2
    if(numflag==0):
        zeroflag=1
        numflag=1
        label_screen["text"] = num_char
        num1=int(label_screen["text"])
    elif(numflag==1):
        if(zeroflag == 0 and dotflag == 0):
            label_screen["text"] = label_screen["text"]+num_char
            num1=int(label_screen["text"])
        elif(zeroflag == 1):
            print("0の次に数字を入力できません")
        elif(dotflag == 1):
            label_screen["text"] = label_screen["text"]+num_char
            num1=float(label_screen["text"])
    elif(numflag==2):
        zeroflag = 1
        dotflag = 0
        numflag = 3
        label_screen["text"] = num_char
        num2=int(label_screen["text"])
    elif(numflag==3):
        if(zeroflag == 0 and dotflag == 0):
            label_screen["text"] = label_screen["text"]+num_char
            num2=int(label_screen["text"])
        elif(zeroflag == 1):
            print("0の次に数字を入力できません")
        elif(dotflag == 1):
            label_screen["text"] = label_screen["text"]+num_char
            num2=float(label_screen["text"])
    print("input_number0")

# input dot
def input_dot(dot):
    global dotflag
    global zeroflag
    if(dotflag==0):
        dotflag = 1
        zeroflag = 0
        label_screen["text"] = label_screen["text"]+dot
    elif(dotflag==1):
        print("もうdotは入力できません")
    print("input dot")

# input symbol
def input_symbol(symbol):
    global numflag
    global zeroflag
    global dotflag
    global opeflag
    global num1
    global num2
    if(symbol=="+"):
        opeflag=1
    elif(symbol=="-"):
        opeflag=2
    elif(symbol=="*"):
        opeflag=3
    elif(symbol=="/"):
        opeflag=4
    numflag = 2
    zeroflag = 0
    dotflag = 0
    
# input eq
def input_eq():
    global num1
    global num2
    print(opeflag)
    if(opeflag==1):
        num1 += num2
        label_screen["text"] = num1
    elif(opeflag==2):
        num1 -= num2
        label_screen["text"] = num1
    elif(opeflag==3):
        num1 *= num2
        label_screen["text"] = num1
    elif(opeflag==4):
        num1 /= num2
        label_screen["text"] = num1
    print("input eq")

# input cr
def input_cr():
    print("input cr")
    global numflag
    global zeroflag
    global dotflag
    global opeflag
    global num1
    global num2
    numflag = 0
    zeroflag = 0
    dotflag = 0
    opeflag = 0
    num1 = 0
    num2 = 0
    label_screen["text"] = ""

#############################################################################
#window
root = tk.Tk()
root.title("calculator")
root.geometry("600x600")

label_screen = tk.Label(root, text="", font=300)

#button
btn_0 = tk.Button(root, text='0', font=200, command=lambda:input_number0("0"))
#
btn_1 = tk.Button(root, text='1', font=200, command=lambda:input_number("1"))
btn_2 = tk.Button(root, text='2', font=200, command=lambda:input_number("2"))
btn_3 = tk.Button(root, text='3', font=200, command=lambda:input_number("3"))
btn_4 = tk.Button(root, text='4', font=200, command=lambda:input_number("4"))
btn_5 = tk.Button(root, text='5', font=200, command=lambda:input_number("5"))
btn_6 = tk.Button(root, text='6', font=200, command=lambda:input_number("6"))
btn_7 = tk.Button(root, text='7', font=200, command=lambda:input_number("7"))
btn_8 = tk.Button(root, text='8', font=200, command=lambda:input_number("8"))
btn_9 = tk.Button(root, text='9', font=200, command=lambda:input_number("9"))
#dotflagの変更,
btn_dot = tk.Button(root, text='.', font=200, command=lambda:input_dot("."))
#caltflagの変更dotflag->0
btn_plus = tk.Button(root, text='+', font=200, command=lambda:input_symbol("+"))
btn_minus = tk.Button(root, text='-', font=200, command=lambda:input_symbol("-"))
btn_multi = tk.Button(root, text='*', font=200, command=lambda:input_symbol("*"))
btn_div = tk.Button(root, text='/', font=200, command=lambda:input_symbol("/"))
#
btn_equal = tk.Button(root, text='=', font=200, command=input_eq)
#いつでも押していいボタン(flag,dotflag,calcflagの初期化)
btn_clear = tk.Button(root, text='CR', font=200, command=input_cr)

#4列
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

#5行
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)

############################
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