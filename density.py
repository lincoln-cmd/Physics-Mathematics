# Density
import tkinter
from tkinter import *

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

frame2 = tkinter.Frame(window,)
frame2.pack(expand = True, fill = 'both')


input1 = Entry(frame1_1)
input1.insert(0, 'Weight/mass')
input1.pack()

label = Label(frame1_1, text = '[kg]')
label.pack()

input2 = Entry(frame1_2)
input2.insert(0, 'Volume')
input2.pack()

label = Label(frame1_2, text = '[m^3]')
label.pack()

label1 = Label(frame1, text = 'Density : 0 [kg/m^3]')
label1.pack(side = 'bottom')


def resolve():
    mas = float(input1.get())
    vol = float(input2.get())
    den = mas / vol
    label1.config(text = 'Density : ' + str(den) + ' [kg/m^3]')


window.mainloop()