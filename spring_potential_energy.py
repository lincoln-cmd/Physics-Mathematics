# Elastic Potential Energy
import tkinter
from tkinter import *
import math

window = tkinter.Tk()
window.title('Elastic Potential Energy')
window.geometry('640x880+100+100')
window.resizable(True, True)

frame1 = Frame(window) # combobox which select the result
frame1.pack(expand = True, fill = 'both')

frame2 = Frame(window) # entry
frame2.pack(expand = True, fill = 'both')

frame3 = Frame(window) # result
frame3.pack(expand = True, fill = 'both')

label1 = Label(frame3, text = '')
label1.pack()

constant = ['Spring force constant(k)', 'Spring stretch length(Δx)', 'Spring potential energy(U)']

# U = 0.5kΔx^2
def equation(event):
    c = combobox.get()
    if c == constant[0]:
        input1 = Entry(frame2)
        input1.insert(0, 'Spring stretch length')
        input1.pack()
        input2 = Entry(frame2)
        input2.insert(0, 'Spring potential energy')
        input2.pack()
        
        def resolve():
            # k = 2U / Δx^2
            x = float(input1.get())
            u = float(input2.get())
            k = (2 * u) / x**2
            label1.config(text = 'Spring force constant : ' + str(k) + ' [N/m]')
            
        button = Button(frame2, text = 'resolve', command = resolve)
        button.pack()
    elif c == constant[1]:
        input1 = Entry(frame2)
        input1.insert(0, 'Spring force constant')
        input1.pack()
        input2 = Entry(frame2)
        input2.insert(0, 'Spring potential energy')
        input2.pack()
        
        def resolve():
            # x = (2U / k)^1/2
            k = float(input1.get())
            u = float(input2.get())
            x = math.sqrt(2 * u / k)
            label1.config(text = 'Spring stretch length : ' + str(x) + ' [m]')
            
        button = Button(frame2, text = 'resolve', command = resolve)
        button.pack()
    
    else:
        input1 = Entry(frame2)
        input1.insert(0, 'Spring force constant')
        input1.pack()
        input2 = Entry(frame2)
        input2.insert(0, 'Spring stretch length')
        input2.pack()
        
        def resolve():
            # U = 0.5kΔx^2
            k = float(input1.get())
            x = float(input2.get())
            u = 0.5 * k * x**2
            label1.config(text = 'Spring potential energy : ' + str(u) + ' [J]')
            
        button = Button(frame2, text = 'resolve', command = resolve)
        button.pack()
    
        
combobox = tkinter.ttk.Combobox(frame1, height = 15, values = constant)
combobox.pack()
combobox.set('Given')
combobox.bind('<<ComboboxSelected>>', equation)
        
        
        


window.mainloop()