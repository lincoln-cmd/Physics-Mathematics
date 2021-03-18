# Friction

import tkinter
from tkinter import *

window = tkinter.Tk()
window.title('Friction')
window.geometry('640x800+100+100')
window.resizable(True, True)

frame1 = Frame(window)
frame1.pack(expand = True, fill = 'both')

frame2 = Frame(window)
frame2.pack(expand = True, fill = 'both')

frame3 = Frame(window)
frame3.pack(expand = True, fill = 'both')

label1 = Label(frame3, text = '')
label1.pack()

constant = ['Friction coefficient(μ)', 'Normal force[N]', 'Friction(F)']
inputlist = ['input1', 'input2']

def equation(event):
    c = combobox.get()
    if c == constant[0]:
        list2 = []
        for i in constant:
            if i != c:
                list2.append(i)
        for i in inputlist:
            j = i
            i = Entry(frame2)
            i.insert(0, list2[inputlist.index(j)])
            i.pack()
            print(i)
            
        def resolve():
            n = float(input1.get())
            f = float(input2.get())
            μ = f / n
            label1.config(text = 'μ : ' + str(μ))
        button = Button(frame2, text = 'resolve', command = resolve)
        button.pack()
        
combobox = tkinter.ttk.Combobox(frame1, height = 15, values = constant)
combobox.pack()
combobox.set('Given')
combobox.bind('<<ComboboxSelected>>', equation)
            
        

window.mainloop()