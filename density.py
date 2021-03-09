# Density
import tkinter
from tkinter import *
from tkinter import messagebox

window = tkinter.Tk()
window.title('Density')
window.geometry('640x880+100+100')
window.resizable(True, True)


frame1 = tkinter.Frame(window)
frame1.pack(expand = True, fill = 'both')

frame1_1 = tkinter.Frame(frame1)
frame1_1.pack(fill = 'x')

frame1_2 = tkinter.Frame(frame1)
frame1_2.pack(fill = 'x')

frame2 = tkinter.Frame(window)
frame2.pack(expand = True, fill = 'both')

input1 = Entry(frame1_1)
input1.insert(0, 'Weight/mass [kg]')
input1.pack()
def wei():
    weight = input1.get()
    try:
        weight = float(input1.get())
        label1.config(text = 'Weight/mass : ' + str(weight) + ' [kg]')
    except:
        messagebox.showerror('Weight/mass error',
                            'The value of \'Weight/mass\' has to have float value')
    
button = Button(frame1_1, text = 'Weight/mass', command = wei)
button.pack()

input2 = Entry(frame1_2)
input2.insert(0, 'Volume [m^3]')
input2.pack()
def vol():
    vol = input2.get()
    try:
        volume = float(input2.get())
        label2.config(text = 'Volume : ' + str(volume) + ' [kg]')
    except:
        messagebox.showerror('Volume error', 'The value of \'Volume\' has to have float value')
button = Button(frame1_2, text = 'Volume', command = vol)
button.pack()


label1 = Label(frame1, text = 'Weight/mass : 0 [kg]')
label1.pack()
label2 = Label(frame1, text = 'Volume : 0 [m^3]')
label2.pack()
label3 = Label(frame1, text = 'Density : 0 [kg/m^3]')
label3.pack(side = 'bottom')
button = Button(frame1, text = 'resolve', command = resolve)
button.pack(side = 'bottom')


def resolve():
    mas = input1.get()
    vol = input2.get()
    try:
        mas = float(input1.get())
        vol = float(input2.get())
        den = mas / vol
        label3.config(text = 'Density : ' + str(den) + ' [kg/m^3]')
    except:
        try:
            mas = float(input1.get())
        except:
            messagebox.showerror('Weight/mass error','The value of \'Weight/mass\' has to have float value')
        try:
            vol = float(input2.get())
        except:
            messagebox.showerror('Volume error', 'The value of \'Volume\' has to have float value')
         

window.mainloop()