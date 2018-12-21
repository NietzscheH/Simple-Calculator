import tkinter as tk
import re

# 窗口
main_window = tk.Tk()
main_window.title('Simple Calculator')
main_window.geometry('500x600')
main_window.config(background = 'light sky blue')

# 显示
displayVar = tk.StringVar()
display = tk.Label(main_window, textvariable = displayVar, anchor = 'e', background = 'light sky blue', font = ('Times New Roman', 20), width = 23, height = 2)
display.pack()
display.place(relx = 0.15, rely = 0.05)

# Function
number_str = ''
# 数的输入
def numberOne(event):
    global number_str
    number_str = number_str + '1'
    # 当输入数时，只显示上一个运算符后输入的数
    if re.search(r'(\D)', number_str):
        temp_list = re.findall(r'(\D)', number_str)
        last_non_num = temp_list[len(temp_list) - 1]
        last_non_num_index = number_str[::-1].index(last_non_num)
        displayVar.set(number_str[::-1][0:last_non_num_index][::-1])
    else:
        displayVar.set(number_str)
def numberTwo():
    global number_str
    number_str = number_str + '2'
    if re.search(r'(\D)', number_str):
        temp_list = re.findall(r'(\D)', number_str)
        last_non_num = temp_list[len(temp_list) - 1]
        last_non_num_index = number_str[::-1].index(last_non_num)
        displayVar.set(number_str[::-1][0:last_non_num_index][::-1])
    else:
        displayVar.set(number_str)
def numberThree():
    global number_str
    number_str = number_str + '3'
    if re.search(r'(\D)', number_str):
        temp_list = re.findall(r'(\D)', number_str)
        last_non_num = temp_list[len(temp_list) - 1]
        last_non_num_index = number_str[::-1].index(last_non_num)
        displayVar.set(number_str[::-1][0:last_non_num_index][::-1])
    else:
        displayVar.set(number_str)
def numberFour():
    global number_str
    number_str = number_str + '4'
    if re.search(r'(\D)', number_str):
        temp_list = re.findall(r'(\D)', number_str)
        last_non_num = temp_list[len(temp_list) - 1]
        last_non_num_index = number_str[::-1].index(last_non_num)
        displayVar.set(number_str[::-1][0:last_non_num_index][::-1])
    else:
        displayVar.set(number_str)
def numberFive():
    global number_str
    number_str = number_str + '5'
    if re.search(r'(\D)', number_str):
        temp_list = re.findall(r'(\D)', number_str)
        last_non_num = temp_list[len(temp_list) - 1]
        last_non_num_index = number_str[::-1].index(last_non_num)
        displayVar.set(number_str[::-1][0:last_non_num_index][::-1])
    else:
        displayVar.set(number_str)
def numberSix():
    global number_str
    number_str = number_str + '6'
    if re.search(r'(\D)', number_str):
        temp_list = re.findall(r'(\D)', number_str)
        last_non_num = temp_list[len(temp_list) - 1]
        last_non_num_index = number_str[::-1].index(last_non_num)
        displayVar.set(number_str[::-1][0:last_non_num_index][::-1])
    else:
        displayVar.set(number_str)
def numberSeven():
    global number_str
    number_str = number_str + '7'
    if re.search(r'(\D)', number_str):
        temp_list = re.findall(r'(\D)', number_str)
        last_non_num = temp_list[len(temp_list) - 1]
        last_non_num_index = number_str[::-1].index(last_non_num)
        displayVar.set(number_str[::-1][0:last_non_num_index][::-1])
    else:
        displayVar.set(number_str)
def numberEight():
    global number_str
    number_str = number_str + '8'
    if re.search(r'(\D)', number_str):
        temp_list = re.findall(r'(\D)', number_str)
        last_non_num = temp_list[len(temp_list) - 1]
        last_non_num_index = number_str[::-1].index(last_non_num)
        displayVar.set(number_str[::-1][0:last_non_num_index][::-1])
    else:
        displayVar.set(number_str)
def numberNine():
    global number_str
    number_str = number_str + '9'
    if re.search(r'(\D)', number_str):
        temp_list = re.findall(r'(\D)', number_str)
        last_non_num = temp_list[len(temp_list) - 1]
        last_non_num_index = number_str[::-1].index(last_non_num)
        displayVar.set(number_str[::-1][0:last_non_num_index][::-1])
    else:
        displayVar.set(number_str)
def numberZero():
    global number_str
    number_str = number_str + '0'
    if re.search(r'(\D)', number_str):
        temp_list = re.findall(r'(\D)', number_str)
        last_non_num = temp_list[len(temp_list) - 1]
        last_non_num_index = number_str[::-1].index(last_non_num)
        displayVar.set(number_str[::-1][0:last_non_num_index][::-1])
    else:
        displayVar.set(number_str)

# 运算符输入
def plus():
    global number_str
    number_str = str(eval(number_str)) # 先计算前面的值
    if int(float(number_str)) == float(number_str):
        number_str = str(int(float(number_str))) # 如果小数点后为0，省略之
    else:
        pass
    number_str = number_str + '+'
    displayVar.set(number_str[:len(number_str) - 1])

def minus():
    global number_str
    if number_str != '':
        number_str = str(eval(number_str))
        if int(float(number_str)) == float(number_str):
            number_str = str(int(float(number_str)))
        else:
            pass
        number_str = number_str + '-'
        displayVar.set(number_str[:len(number_str) - 1])
    if number_str == '':
        number_str = number_str + '-'
        displayVar.set(number_str[:len(number_str) - 1])

def multi():
    global number_str
    number_str = str(eval(number_str))
    if int(float(number_str)) == float(number_str):
        number_str = str(int(float(number_str)))
    else:
        pass
    number_str = number_str + '*'
    displayVar.set(number_str[:len(number_str) - 1])

def divide():
    global number_str
    number_str = str(eval(number_str))
    if int(float(number_str)) == float(number_str):
        number_str = str(int(float(number_str)))
    else:
        pass
    number_str = number_str + '/'
    displayVar.set(number_str[:len(number_str) - 1])

def equal():
    global number_str
    number_str = str(eval(number_str))
    if int(float(number_str)) == float(number_str):
        number_str = str(int(float(number_str)))
    else:
        pass
    displayVar.set(number_str)
    number_str = ''

def redo():
    global number_str
    number_str = ''
    displayVar.set(number_str)

# 按键
    # 1
number_one = tk.Button(main_window, text = '1', font = ('Times New Roman', 16), background = 'mint cream', width = 4, height = 2, command = numberOne)
number_one.pack()
number_one.place(relx = 0.15, rely = 0.8)
    # 2
number_two = tk.Button(main_window, text = '2', font = ('Times New Roman', 16), background = 'mint cream', width = 4, height = 2, command = numberTwo)
number_two.pack()
number_two.place(relx = 0.35, rely = 0.8)
    # 3
number_three = tk.Button(main_window, text = '3', font = ('Times New Roman', 16), background = 'mint cream', width = 4, height = 2, command = numberThree)
number_three.pack()
number_three.place(relx = 0.55, rely = 0.8)
    # 0
number_zero = tk.Button(main_window, text = '0', font = ('Times New Roman', 16), background = 'mint cream', width = 4, height = 2, command = numberZero)
number_zero.pack()
number_zero.place(relx = 0.75, rely = 0.5)
    # 4
number_four = tk.Button(main_window, text = '4', font = ('Times New Roman', 16), background = 'mint cream', width = 4, height = 2, command = numberFour)
number_four.pack()
number_four.place(relx = 0.15, rely = 0.65)
    # 5
number_five = tk.Button(main_window, text = '5', font = ('Times New Roman', 16), background = 'mint cream', width = 4, height = 2, command = numberFive)
number_five.pack()
number_five.place(relx = 0.35, rely = 0.65)
    # 6
number_six = tk.Button(main_window, text = '6', font = ('Times New Roman', 16), background = 'mint cream', width = 4, height = 2, command = numberSix)
number_six.pack()
number_six.place(relx = 0.55, rely = 0.65)
    # 7
number_seven = tk.Button(main_window, text = '7', font = ('Times New Roman', 16), background = 'mint cream', width = 4, height = 2, command = numberSeven)
number_seven.pack()
number_seven.place(relx = 0.15, rely = 0.5)
    # 8
number_eight = tk.Button(main_window, text = '8', font = ('Times New Roman', 16), background = 'mint cream', width = 4, height = 2, command = numberEight)
number_eight.pack()
number_eight.place(relx = 0.35, rely = 0.5)
    # 9
number_nine = tk.Button(main_window, text = '9', font = ('Times New Roman', 16), background = 'mint cream', width = 4, height = 2, command = numberNine)
number_nine.pack()
number_nine.place(relx = 0.55, rely = 0.5)
    # =
equal = tk.Button(main_window, text = '=', font = ('Times New Roman', 16), background = 'mint cream', width = 4, height = 6, command = equal)
equal.pack()
equal.place(relx = 0.75, rely = 0.65)
    # +
plus = tk.Button(main_window, text = '+', font = ('Times New Roman', 16), background = 'mint cream', width = 4, height = 2, command = plus)
plus.pack()
plus.place(relx = 0.15, rely = 0.35)
    # -
minus = tk.Button(main_window, text = '-', font = ('Times New Roman', 16), background = 'mint cream', width = 4, height = 2, command = minus)
minus.pack()
minus.place(relx = 0.35, rely = 0.35)
    # *
multi = tk.Button(main_window, text = '*', font = ('Times New Roman', 16), background = 'mint cream', width = 4, height = 2, command = multi)
multi.pack()
multi.place(relx = 0.55, rely = 0.35)
    # /
divide = tk.Button(main_window, text = '/', font = ('Times New Roman', 16), background = 'mint cream', width = 4, height = 2, command = divide)
divide.pack()
divide.place(relx = 0.75, rely = 0.35)
    # redo
redo = tk.Button(main_window, text = 'C', font = ('Times New Roman', 16), background = 'mint cream', width = 29, height = 2, command = redo)
redo.pack()
redo.place(relx = 0.15, rely = 0.2)

main_window.mainloop()
