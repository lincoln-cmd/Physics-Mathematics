# Acceleration

import tkinter
from tkinter import *

window = tkinter.Tk()
window.geometry('640x880+100+100')
window.title('Acceleration')
window.resizable(True, True)

initialspeed = []
finalspeed = []
time = []
acc = []
value = ['Speed difference', 'Mass & Force', 'Distance traveled']

def equation(event):
    if combobox.get() == value[0]:
        input1 = Entry(window)
        input1.pack()
        label1 = Label(window, text = 'Initial speed : 0 [m/s]')
        label1.pack()
        label2 = Label(window, text = 'Final spped : 0 [m/s]')
        label2.pack()
        label3 = Label(window, text = 'Time : 0 [s]')
        label3.pack()
        label4 = Label(window, text = 'Acceleration : 0[m/s^2]')
        label4.pack()
        def initial():
            v1 = float(input1.get())
            if len(initialspeed) == 0:
                initialspeed.append(v1)
            else:
                initialspeed[0] = v1
            label1.config(text = 'Initial speed : ' + str(initialspeed[0]) + ' [m/s]')
        button = Button(window, text = 'Initial speed', command = initial)
        button.pack()
        def final():
            v2 = float(input1.get())
            if len(finalspeed) == 0:
                finalspeed.append(v2)
            else:
                finalspeed[0] = v2
            label2.config(text = 'Final speed : ' + str(finalspeed[0]) + ' [m/s]')
        button = Button(window, text = 'Final speed', command = final)
        button.pack()

combobox = tkinter.ttk.Combobox(window, height = 15, values = value)
combobox.pack()
combobox.set('Given')
combobox.bind('<<ComboboxSelected>>', equation)




window.mainloop()