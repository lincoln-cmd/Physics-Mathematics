# Friction

import tkinter
from tkinter import *
from tkinter import ttk

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

label1 = Label(frame3, text = 'result')
label1.pack()

constant = ['Friction coefficient(μ)', 'Normal force[N]', 'Friction(F)']
inputlist = ['input1', 'input2']
entries = []

def equation(event):
    c = combobox.get()
    if c == constant[0]:
        list2 = []
        for i in constant:
            if i != c:
                list2.append(i)
        for i, text in enumerate(inputlist):
            text = Entry(frame2)
            text.insert(0, list2[i])
            text.pack()
            entries.append(text)
            
        def resolve():
            list3 = []
            for i in entries:
                list3.append(i.get())
            n = float(list3[0])
            f = float(list3[1])
            μ = f / n
            label1.config(text = 'Friction coefficient(μ) : ' + str(μ))
        button = Button(frame2, text = 'resolve', command = resolve)
        button.pack()
    
    if c == constant[1]:
        list2 = []
        for i in constant:
            if i != c:
                list2.append(i)
        for i, text in enumerate(inputlist):
            text = Entry(frame2)
            text.insert(0, list2[i])
            text.pack()
            entries.append(text)
            
        def resolve():
            list3 = []
            for i in entries:
                list3.append(i.get())
            μ = float(list3[0])
            f = float(list3[1])
            n = f / μ
            label1.config(text = 'Normal force(N) : ' + str(n) + ' [N]')
        button = Button(frame2, text = 'resolve', command = resolve)
        button.pack()
    if c== constant[2]:
        list2 = []
        for i in constant:
            if i != c:
                list2.append(i)
        for i, text in enumerate(inputlist):
            text = Entry(frame2)
            text.insert(0, list2[i])
            text.pack()
            entries.append(text)
            
        def resolve():
            list3 = []
            for i in entries:
                list3.append(i.get())
            μ = float(list3[0])
            n = float(list3[1])
            f = μ * n
            label1.config(text = 'Friction(F)' + str(f) + ' [N]')
        button = Button(frame2, text = 'resolve', command = resolve)
        button.pack()
            
        
combobox = tkinter.ttk.Combobox(frame1, height = 15, values = constant)
combobox.pack()
combobox.set('Given')
combobox.bind('<<ComboboxSelected>>', equation)
            
        

window.mainloop()