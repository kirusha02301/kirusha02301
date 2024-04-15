import copy
import tkinter as tk
from tkinter import *

window = tk.Tk() # создать окно
window.title("Крестики-Нолики") # изменить название окна
window.geometry("500x500") # размер окна

text = Text(width=25, height=5)
text.place(x=150, y=350)
#text.insert(1.0, "Крестики-Нолики")


import numpy as np #библиотека
nulSpis = [['.','.','.'], #игровое поле
          ['.','.','.'],
          ['.','.','.']]


#set window color
#window['background']='#856ff8'

def functionNul(nulSpis):
    for i in range(len(nulSpis)):  # проверяем строчки
        if nulSpis[i] == ['x', 'x', 'x']:
            return 'x'
        if nulSpis[i] == ['o', 'o', 'o']:
            return ('o')
    for j in range(len(nulSpis[0])):  # проверяем столбики
        x = 0
        o = 0
        for i in range(len(nulSpis)):
            if nulSpis[i][j] == 'x':
                x += 1
            if nulSpis[i][j] == 'o':
                o += 1
        if x == 3:
            return 'x'
        if o == 3:
            return 'o'
    if nulSpis[0][0] == 'x' and nulSpis[1][1] == 'x' and nulSpis[2][2] == 'x':  # проверяем две диагонали
        return 'x'
    if nulSpis[0][0] == 'o' and nulSpis[1][1] == 'o' and nulSpis[2][2] == 'o':
        return 'o'
    if nulSpis[0][-1] == 'x' and nulSpis[1][-2] == 'x' and nulSpis[2][-3] == 'x':
        return 'x'
    if nulSpis[0][-1] == 'o' and nulSpis[1][-2] == 'o' and nulSpis[2][-3] == 'o':
        return 'o'

    flag = 0

    for i in range(3):
        for j in range(3):
            if nulSpis[i][j] == '.':
                flag = 1
                break
    if flag == 0:
        return 'draw'
    return '-'

def bot(nulSpisok):

    nulSpisnol = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

    for k in range(2000):

        nulSpis = copy.deepcopy(nulSpisok)
        spis = []
        for i in range(len(nulSpis)):
            for j in range(len(nulSpis)):
                if nulSpis[i][j] == '.':
                    spis.append(i * 3 + j)
        np.random.shuffle(spis)

        while functionNul(nulSpis) == '-':
            for i in range(len(spis)):
                if i % 2 == 0:
                    nulSpis[spis[i] // 3][spis[i] % 3] = 'x'
                else:
                    nulSpis[spis[i] // 3][spis[i] % 3] = 'o'

                # nulSpis[spis[i]//3][spis[i]%3] = 'x'

                # print(np.array(nulSpis))
                # print(functionNul(nulSpis))
                if functionNul(nulSpis) == 'x' or functionNul(nulSpis) == 'o':
                    if functionNul(nulSpis) == 'x':
                        nulSpisnol[spis[0] // 3][spis[0] % 3] += 1
                    if functionNul(nulSpis) == 'o':
                        nulSpisnol[spis[0] // 3][spis[0] % 3] -= 1
                    break

    print(np.array(nulSpisnol))

    print(np.array(nulSpisnol).reshape(9))

    print(np.argmax(np.array(nulSpisnol).reshape(9)))

    print(np.max(np.array(nulSpisnol).reshape(9)))

    if np.argmax(np.array(nulSpisnol).reshape(9)) ==0:
        function_1()
    if np.argmax(np.array(nulSpisnol).reshape(9)) ==1:
        function_2()
    if np.argmax(np.array(nulSpisnol).reshape(9)) ==2:
        function_3()
    if np.argmax(np.array(nulSpisnol).reshape(9)) ==3:
        function_4()
    if np.argmax(np.array(nulSpisnol).reshape(9)) ==4:
        function_5()
    if np.argmax(np.array(nulSpisnol).reshape(9)) ==5:
        function_6()
    if np.argmax(np.array(nulSpisnol).reshape(9)) ==6:
        function_7()
    if np.argmax(np.array(nulSpisnol).reshape(9)) ==7:
        function_8()
    if np.argmax(np.array(nulSpisnol).reshape(9)) ==8:
        function_9()



flag_1 = 0
def function_1():
    global flag_1
    if flag_1 == 0:
        button_1.config(text = 'x', bg='#A877BA')#bg='green'
        flag_1 = 1
        nulSpis[0][0] = 'x'
        bot(nulSpis)
    else:
        button_1.config(text = 'o', bg='#08AABA')#bg='red'
        flag_1 = 0
        nulSpis[0][0] = 'o'
    if functionNul(nulSpis) == "x":
        text.insert(1.0, "Выиграли крестики")
    if functionNul(nulSpis) == "o":
        text.insert(1.0, "Выиграли нолики")

    print(functionNul(nulSpis))
    #bot(nulSpis)
button_1 = tk.Button(window, text = ".", bg='#54FA9B', width = 10, height = 5,
                     command = function_1)
button_1.place(x=50, y=50)

flag_1 = 0
def function_2():
    global flag_1
    if flag_1 == 0:
        button_2.config(text = 'x', bg='#A877BA')#bg='green'
        flag_1 = 1
        nulSpis[0][1] = 'x'
        bot(nulSpis)
    else:
        button_2.config(text = 'o', bg='#08AABA')#bg='red'
        flag_1 = 0
        nulSpis[0][1] = 'o'
    if functionNul(nulSpis) == "x":
        text.insert(1.0, "Выиграли крестики")
    if functionNul(nulSpis) == "o":
        text.insert(1.0, "Выиграли нолики")
    functionNul(nulSpis)
    print(functionNul(nulSpis))
    #bot(nulSpis)
button_2 = tk.Button(window, text = ".", bg='#54FA9B', width = 10, height = 5,
                     command = function_2)
button_2.place(x=150, y=50)

flag_1 = 0
def function_3():
    global flag_1
    if flag_1 == 0:
        button_3.config(text = 'x', bg='#A877BA')#bg='green'
        flag_1 = 1
        nulSpis[0][2] = 'x'
        bot(nulSpis)
    else:
        button_3.config(text = 'o', bg='#08AABA')#bg='red'
        flag_1 = 0
        nulSpis[0][2] = 'o'
    if functionNul(nulSpis) == "x":
        text.insert(1.0, "Выиграли крестики")
    if functionNul(nulSpis) == "o":
        text.insert(1.0, "Выиграли нолики")
    functionNul(nulSpis)
    print(functionNul(nulSpis))
    #bot(nulSpis)
button_3 = tk.Button(window, text = ".", bg='#54FA9B', width = 10, height = 5,
                     command = function_3)
button_3.place(x=250, y=50)

flag_1 = 0
def function_4():
    global flag_1
    if flag_1 == 0:
        button_4.config(text = 'x', bg='#A877BA')#bg='green'
        flag_1 = 1
        nulSpis[1][0] = 'x'
        bot(nulSpis)
    else:
        button_4.config(text = 'o', bg='#08AABA')#bg='red'
        flag_1 = 0
        nulSpis[1][0] = 'o'
    if functionNul(nulSpis) == "x":
        text.insert(1.0, "Выиграли крестики")
    if functionNul(nulSpis) == "o":
        text.insert(1.0, "Выиграли нолики")
    functionNul(nulSpis)
    print(functionNul(nulSpis))
    #bot(nulSpis)
button_4 = tk.Button(window, text = ".", bg='#54FA9B', width = 10, height = 5,
                     command = function_4)
button_4.place(x=50, y=150)

flag_1 = 0
def function_5():
    global flag_1
    if flag_1 == 0:
        button_5.config(text = 'x', bg='#A877BA')#bg='green'
        flag_1 = 1
        nulSpis[1][1] = 'x'
        bot(nulSpis)
    else:
        button_5.config(text = 'o', bg='#08AABA')#bg='red'
        flag_1 = 0
        nulSpis[1][1] = 'o'
    if functionNul(nulSpis) == "x":
        text.insert(1.0, "Выиграли крестики")
    if functionNul(nulSpis) == "o":
        text.insert(1.0, "Выиграли нолики")
    functionNul(nulSpis)
    print(functionNul(nulSpis))
    #bot(nulSpis)
button_5 = tk.Button(window, text = ".", bg='#54FA9B', width = 10, height = 5,
                     command = function_5)
button_5.place(x=150, y=150)

flag_1 = 0
def function_6():
    global flag_1
    if flag_1 == 0:
        button_6.config(text = 'x', bg='#A877BA')#bg='green'
        flag_1 = 1
        nulSpis[1][2] = 'x'
        bot(nulSpis)
    else:
        button_6.config(text = 'o', bg='#08AABA')#bg='red'
        flag_1 = 0
        nulSpis[1][2] = 'o'
    if functionNul(nulSpis) == "x":
        text.insert(1.0, "Выиграли крестики")
    if functionNul(nulSpis) == "o":
        text.insert(1.0, "Выиграли нолики")
    functionNul(nulSpis)
    print(functionNul(nulSpis))
    #bot(nulSpis)
button_6 = tk.Button(window, text = ".", bg='#54FA9B', width = 10, height = 5,
                     command = function_6)
button_6.place(x=250, y=150)

flag_1 = 0
def function_7():
    global flag_1
    if flag_1 == 0:
        button_7.config(text = 'x', bg='#A877BA')#bg='green'
        flag_1 = 1
        nulSpis[2][0] = 'x'
        bot(nulSpis)
    else:
        button_7.config(text = 'o', bg='#08AABA')#bg='red'
        flag_1 = 0
        nulSpis[2][0] = 'o'
    if functionNul(nulSpis) == "x":
        text.insert(1.0, "Выиграли крестики")
    if functionNul(nulSpis) == "o":
        text.insert(1.0, "Выиграли нолики")
    functionNul(nulSpis)
    print(functionNul(nulSpis))
    #bot(nulSpis)
button_7 = tk.Button(window, text = ".", bg='#54FA9B', width = 10, height = 5,
                     command = function_7)
button_7.place(x=50, y=250)

flag_1 = 0
def function_8():
    global flag_1
    if flag_1 == 0:
        button_8.config(text = 'x', bg='#A877BA')#bg='green'
        flag_1 = 1
        nulSpis[2][1] = 'x'
        bot(nulSpis)
    else:
        button_8.config(text = 'o', bg='#08AABA')#bg='red'
        flag_1 = 0
        nulSpis[2][1] = 'o'
    if functionNul(nulSpis) == "x":
        text.insert(1.0, "Выиграли крестики")
    if functionNul(nulSpis) == "o":
        text.insert(1.0, "Выиграли нолики")
    functionNul(nulSpis)
    print(functionNul(nulSpis))
    #bot(nulSpis)
button_8 = tk.Button(window, text = ".", bg='#54FA9B', width = 10, height = 5,
                     command = function_8)
button_8.place(x=150, y=250)

flag_1 = 0
def function_9():
    global flag_1
    if flag_1 == 0:
        button_9.config(text = 'x', bg='#A877BA')#bg='green'
        flag_1 = 1
        nulSpis[2][2] = 'x'
        bot(nulSpis)
    else:
        button_9.config(text = 'o', bg='#08AABA')#bg='red'
        flag_1 = 0
        nulSpis[2][2] = 'o'
    if functionNul(nulSpis) == "x":
        text.insert( "Выиграли крестики")
    if functionNul(nulSpis) == "o":
        text.insert( "Выиграли нолики")
    functionNul(nulSpis)
    print(functionNul(nulSpis))
    #bot(nulSpis)
button_9 = tk.Button(window, text = ".", bg='#54FA9B', width = 10, height = 5,
                     command = function_9)
button_9.place(x=250, y=250)



window.mainloop()
functionNul(nulSpis)
