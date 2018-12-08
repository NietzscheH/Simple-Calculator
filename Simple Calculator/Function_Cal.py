import Simple_Calculator
import tkinter as tk
number_str = ''

# 数的输入
def numberOne():
    global number_str
    number_str = number_str + '1'
    Simple_Calculator.displayVar.set(number_str)
def numberTwo():
    global number_str
    number_str = number_str + '2'
    Simple_Calculator.displayVar.set(number_str)
def numberThree():
    global number_str
    number_str = number_str + '3'
    Simple_Calculator.displayVar.set(number_str)
def numberFour():
    global number_str
    number_str = number_str + '4'
    Simple_Calculator.displayVar.set(number_str)
def numberFive():
    global number_str
    number_str = number_str + '5'
    Simple_Calculator.displayVar.set(number_str)
def numberSix():
    global number_str
    number_str = number_str + '6'
    Simple_Calculator.displayVar.set(number_str)
def numberSeven():
    global number_str
    number_str = number_str + '7'
    Simple_Calculator.displayVar.set(number_str)
def numberEight():
    global number_str
    number_str = number_str + '8'
    Simple_Calculator.displayVar.set(number_str)
def numberNine():
    global number_str
    number_str = number_str + '9'
    Simple_Calculator.displayVar.set(number_str)
def numberZero():
    global number_str
    number_str = number_str + '0'
    Simple_Calculator.displayVar.set(number_str)

# 运算符输入
def plus():
    global number_str
    number_str = str(eval(number_str)) # 先计算前面的值
    if int(float(number_str)) == float(number_str):
        number_str = str(int(float(number_str))) # 如果小数点后为0，省略之
    else:
        pass
    number_str = number_str + '+'
    Simple_Calculator.displayVar.set(number_str)

def minus():
    global number_str
    number_str = str(eval(number_str))
    if int(float(number_str)) == float(number_str):
        number_str = str(int(float(number_str)))
    else:
        pass
    number_str = number_str + '-'
    Simple_Calculator.displayVar.set(number_str)

def multi():
    global number_str
    number_str = str(eval(number_str))
    if int(float(number_str)) == float(number_str):
        number_str = str(int(float(number_str)))
    else:
        pass
    number_str = number_str + '*'
    Simple_Calculator.displayVar.set(number_str)

def divide():
    global number_str
    number_str = str(eval(number_str))
    if int(float(number_str)) == float(number_str):
        number_str = str(int(float(number_str)))
    else:
        pass
    number_str = number_str + '/'
    Simple_Calculator.displayVar.set(number_str)

def equal():
    global number_str
    number_str = str(eval(number_str))
    if int(float(number_str)) == float(number_str):
        number_str = str(int(float(number_str)))
    else:
        pass
    Simple_Calculator.displayVar.set(number_str)

def redo():
    global number_str
    number_str = ''
    Simple_Calculator.displayVar.set(number_str)
