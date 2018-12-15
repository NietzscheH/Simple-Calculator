import re
import Simple_Calculator
number_str = ''

# 数的输入
def numberOne():
    global number_str
    number_str = number_str + '1'
    # 当输入数时，只显示上一个运算符后输入的数
    if re.search(r'(\D)', number_str):
        temp_list = re.findall(r'(\D)', number_str)
        last_non_num = temp_list[len(temp_list) - 1]
        last_non_num_index = number_str[::-1].index(last_non_num)
        Simple_Calculator.displayVar.set(number_str[::-1][0:last_non_num_index][::-1])
    else:
        Simple_Calculator.displayVar.set(number_str)
def numberTwo():
    global number_str
    number_str = number_str + '2'
    if re.search(r'(\D)', number_str):
        temp_list = re.findall(r'(\D)', number_str)
        last_non_num = temp_list[len(temp_list) - 1]
        last_non_num_index = number_str[::-1].index(last_non_num)
        Simple_Calculator.displayVar.set(number_str[::-1][0:last_non_num_index][::-1])
    else:
        Simple_Calculator.displayVar.set(number_str)
def numberThree():
    global number_str
    number_str = number_str + '3'
    if re.search(r'(\D)', number_str):
        temp_list = re.findall(r'(\D)', number_str)
        last_non_num = temp_list[len(temp_list) - 1]
        last_non_num_index = number_str[::-1].index(last_non_num)
        Simple_Calculator.displayVar.set(number_str[::-1][0:last_non_num_index][::-1])
    else:
        Simple_Calculator.displayVar.set(number_str)
def numberFour():
    global number_str
    number_str = number_str + '4'
    if re.search(r'(\D)', number_str):
        temp_list = re.findall(r'(\D)', number_str)
        last_non_num = temp_list[len(temp_list) - 1]
        last_non_num_index = number_str[::-1].index(last_non_num)
        Simple_Calculator.displayVar.set(number_str[::-1][0:last_non_num_index][::-1])
    else:
        Simple_Calculator.displayVar.set(number_str)
def numberFive():
    global number_str
    number_str = number_str + '5'
    if re.search(r'(\D)', number_str):
        temp_list = re.findall(r'(\D)', number_str)
        last_non_num = temp_list[len(temp_list) - 1]
        last_non_num_index = number_str[::-1].index(last_non_num)
        Simple_Calculator.displayVar.set(number_str[::-1][0:last_non_num_index][::-1])
    else:
        Simple_Calculator.displayVar.set(number_str)
def numberSix():
    global number_str
    number_str = number_str + '6'
    if re.search(r'(\D)', number_str):
        temp_list = re.findall(r'(\D)', number_str)
        last_non_num = temp_list[len(temp_list) - 1]
        last_non_num_index = number_str[::-1].index(last_non_num)
        Simple_Calculator.displayVar.set(number_str[::-1][0:last_non_num_index][::-1])
    else:
        Simple_Calculator.displayVar.set(number_str)
def numberSeven():
    global number_str
    number_str = number_str + '7'
    if re.search(r'(\D)', number_str):
        temp_list = re.findall(r'(\D)', number_str)
        last_non_num = temp_list[len(temp_list) - 1]
        last_non_num_index = number_str[::-1].index(last_non_num)
        Simple_Calculator.displayVar.set(number_str[::-1][0:last_non_num_index][::-1])
    else:
        Simple_Calculator.displayVar.set(number_str)
def numberEight():
    global number_str
    number_str = number_str + '8'
    if re.search(r'(\D)', number_str):
        temp_list = re.findall(r'(\D)', number_str)
        last_non_num = temp_list[len(temp_list) - 1]
        last_non_num_index = number_str[::-1].index(last_non_num)
        Simple_Calculator.displayVar.set(number_str[::-1][0:last_non_num_index][::-1])
    else:
        Simple_Calculator.displayVar.set(number_str)
def numberNine():
    global number_str
    number_str = number_str + '9'
    if re.search(r'(\D)', number_str):
        temp_list = re.findall(r'(\D)', number_str)
        last_non_num = temp_list[len(temp_list) - 1]
        last_non_num_index = number_str[::-1].index(last_non_num)
        Simple_Calculator.displayVar.set(number_str[::-1][0:last_non_num_index][::-1])
    else:
        Simple_Calculator.displayVar.set(number_str)
def numberZero():
    global number_str
    number_str = number_str + '0'
    if re.search(r'(\D)', number_str):
        temp_list = re.findall(r'(\D)', number_str)
        last_non_num = temp_list[len(temp_list) - 1]
        last_non_num_index = number_str[::-1].index(last_non_num)
        Simple_Calculator.displayVar.set(number_str[::-1][0:last_non_num_index][::-1])
    else:
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
    Simple_Calculator.displayVar.set(number_str[:len(number_str) - 1])

def minus():
    global number_str
    if number_str != '':
        number_str = str(eval(number_str))
        if int(float(number_str)) == float(number_str):
            number_str = str(int(float(number_str)))
        else:
            pass
        number_str = number_str + '-'
        Simple_Calculator.displayVar.set(number_str[:len(number_str) - 1])
    if number_str == '':
        number_str = number_str + '-'
        Simple_Calculator.displayVar.set(number_str[:len(number_str) - 1])

def multi():
    global number_str
    number_str = str(eval(number_str))
    if int(float(number_str)) == float(number_str):
        number_str = str(int(float(number_str)))
    else:
        pass
    number_str = number_str + '*'
    Simple_Calculator.displayVar.set(number_str[:len(number_str) - 1])

def divide():
    global number_str
    number_str = str(eval(number_str))
    if int(float(number_str)) == float(number_str):
        number_str = str(int(float(number_str)))
    else:
        pass
    number_str = number_str + '/'
    Simple_Calculator.displayVar.set(number_str[:len(number_str) - 1])

def equal():
    global number_str
    number_str = str(eval(number_str))
    if int(float(number_str)) == float(number_str):
        number_str = str(int(float(number_str)))
    else:
        pass
    Simple_Calculator.displayVar.set(number_str)
    number_str = ''

def redo():
    global number_str
    number_str = ''
    Simple_Calculator.displayVar.set(number_str)
