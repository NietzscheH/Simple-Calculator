import tkinter as tk
import Function_Cal

# 窗口
main_window = tk.Tk()
main_window.title('Simple Calculator')
main_window.geometry('500x600')

# 显示
displayVar = tk.StringVar()
display = tk.Label(main_window, textvariable = displayVar, font = ('Times New Roman', 16), width = 29, height = 2)
display.pack()
display.place(relx = 0.15, rely = 0.05)

# 按键
    # 1
number_one = tk.Button(main_window, text = '1', font = ('Times New Roman', 16), width = 4, height = 2, command = Function_Cal.numberOne)
number_one.pack()
number_one.place(relx = 0.15, rely = 0.8)
    # 2
number_two = tk.Button(main_window, text = '2', font = ('Times New Roman', 16), width = 4, height = 2, command = Function_Cal.numberTwo)
number_two.pack()
number_two.place(relx = 0.35, rely = 0.8)
    # 3
number_three = tk.Button(main_window, text = '3', font = ('Times New Roman', 16), width = 4, height = 2, command = Function_Cal.numberThree)
number_three.pack()
number_three.place(relx = 0.55, rely = 0.8)
    # 0
number_zero = tk.Button(main_window, text = '0', font = ('Times New Roman', 16), width = 4, height = 2, command = Function_Cal.numberZero)
number_zero.pack()
number_zero.place(relx = 0.75, rely = 0.5)
    # 4
number_four = tk.Button(main_window, text = '4', font = ('Times New Roman', 16), width = 4, height = 2, command = Function_Cal.numberFour)
number_four.pack()
number_four.place(relx = 0.15, rely = 0.65)
    # 5
number_five = tk.Button(main_window, text = '5', font = ('Times New Roman', 16), width = 4, height = 2, command = Function_Cal.numberFive)
number_five.pack()
number_five.place(relx = 0.35, rely = 0.65)
    # 6
number_six = tk.Button(main_window, text = '6', font = ('Times New Roman', 16), width = 4, height = 2, command = Function_Cal.numberSix)
number_six.pack()
number_six.place(relx = 0.55, rely = 0.65)
    # 7
number_seven = tk.Button(main_window, text = '7', font = ('Times New Roman', 16), width = 4, height = 2, command = Function_Cal.numberSeven)
number_seven.pack()
number_seven.place(relx = 0.15, rely = 0.5)
    # 8
number_eight = tk.Button(main_window, text = '8', font = ('Times New Roman', 16), width = 4, height = 2, command = Function_Cal.numberEight)
number_eight.pack()
number_eight.place(relx = 0.35, rely = 0.5)
    # 9
number_nine = tk.Button(main_window, text = '9', font = ('Times New Roman', 16), width = 4, height = 2, command = Function_Cal.numberNine)
number_nine.pack()
number_nine.place(relx = 0.55, rely = 0.5)
    # =
equal = tk.Button(main_window, text = '=', font = ('Times New Roman', 16), width = 4, height = 6, command = Function_Cal.equal)
equal.pack()
equal.place(relx = 0.75, rely = 0.65)
    # +
plus = tk.Button(main_window, text = '+', font = ('Times New Roman', 16), width = 4, height = 2, command = Function_Cal.plus)
plus.pack()
plus.place(relx = 0.15, rely = 0.35)
    # -
minus = tk.Button(main_window, text = '-', font = ('Times New Roman', 16), width = 4, height = 2, command = Function_Cal.minus)
minus.pack()
minus.place(relx = 0.35, rely = 0.35)
    # *
multi = tk.Button(main_window, text = '✖', font = ('Times New Roman', 16), width = 4, height = 2, command = Function_Cal.multi)
multi.pack()
multi.place(relx = 0.55, rely = 0.35)
    # /
divide = tk.Button(main_window, text = '➗', font = ('Times New Roman', 16), width = 4, height = 2, command = Function_Cal.divide)
divide.pack()
divide.place(relx = 0.75, rely = 0.35)
    # redo
redo = tk.Button(main_window, text = 'C', font = ('Times New Roman', 16), width = 29, height = 2, command = Function_Cal.redo)
redo.pack()
redo.place(relx = 0.15, rely = 0.2)

main_window.mainloop()
