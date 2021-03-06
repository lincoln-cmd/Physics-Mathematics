# Acceleration

import tkinter
from tkinter import *
from tkinter import ttk

window = tkinter.Tk()
window.geometry('640x880+100+100')
window.title('Acceleration')
window.resizable(True, True)


acclist = []
value = ['Speed difference', 'Mass & Force', 'Distance traveled']
    

def equation(event):
    b = []
    c = combobox.get()
    if len(b) == 0: # 콤보박스 리스트 중 다른 요소 선택시 텍스트 필드 초기화
        frame = tkinter.Frame(window)
        frame.pack()    
        b.append(c)
    else:
        for widget in frame.winfo_children():
            widget.destroy()
        frame = tkinter.Frame(window)
        frame.pack()
        b[0] = c

        
    # speed difference
    if b[0] == value[0]:
        for widget in frame.winfo_children():
            widget.destroy()
        frame = tkinter.Frame(window)
        frame.pack()
        initialspeed = []
        finalspeed = []
        timelist = []
        
        input1 = Entry(frame)
        input1.pack()
        label1 = Label(frame, text = 'Initial speed : 0 [m/s]')
        label1.pack()
        label2 = Label(frame, text = 'Final spped : 0 [m/s]')
        label2.pack()
        label3 = Label(frame, text = 'Time : 0 [s]')
        label3.pack()
        def initial():
            v1 = float(input1.get())
            if len(initialspeed) == 0:
                initialspeed.append(v1)
            else:
                initialspeed[0] = v1
            label1.config(text = 'Initial speed : ' + str(initialspeed[0]) + ' [m/s]')
        button = Button(frame, text = 'Initial speed', command = initial)
        button.pack()
        def final():
            v2 = float(input1.get())
            if len(finalspeed) == 0:
                finalspeed.append(v2)
            else:
                finalspeed[0] = v2
            label2.config(text = 'Final speed : ' + str(finalspeed[0]) + ' [m/s]')
        button = Button(frame, text = 'Final speed', command = final)
        button.pack()
        def time():
            t = float(input1.get())
            if len(timelist) == 0:
                timelist.append(t)
            else:
                timelist[0] = t
            label3.config(text = 'Time : ' + str(t) + ' [s]')
        button = Button(frame, text = 'Time', command = time)
        button.pack()

        label = Label(frame, text = '\n')
        label.pack()        
        label4 = Label(frame, text = 'Acceleration : 0 [m/s^2]')
        label4.pack()
            

        def resolve():
            v1 = initialspeed[0]
            v2 = finalspeed[0]
            t = timelist[0]
            a = (v2 - v1) / t
            label4.config(text = 'Acceleration : ' + str(a) + ' [m/s^2]')
        
        button = Button(frame, text = 'resolve', command = resolve)
        button.pack()
        
    # mass and force
    if b[0] == value[1]:
        for widget in frame.winfo_children():
            widget.destroy()
        frame = tkinter.Frame(window)
        frame.pack()
        masslist = []
        forcelist = []
            
        input2 = Entry(frame)
        input2.pack()
        label1 = Label(frame, text = 'Mass : 0 [kg]')
        label1.pack()
        label2 = Label(frame, text = 'Force : 0 [N]')
        label2.pack()
        
        def mass():
            m = float(input2.get())
            if len(masslist) == 0:
                masslist.append(m)
            else:
                masslist[0] = m
            label1.config(text = 'Mass : ' + str(m) + ' [kg]')
        button = Button(frame, text = 'Mass', command = mass)
        button.pack()
        
        def force():
            f = float(input2.get())
            if len(forcelist) == 0:
                forcelist.append(f)
            else:
                forcelist[0] = f
            label2.config(text = 'Force : ' + str(f) + ' [N]')
        button = Button(frame, text = 'Force', command = force)
        button.pack()
        
        label = Label(frame, text = '\n')
        label.pack()
        label3 = Label(frame, text = 'Acceleration : 0 [m/s^2]')
        label3.pack()
        
        def resolve():
            m = masslist[0]
            f = forcelist[0]
            a = f / m
            label3.config(text = 'Acceleration : ' + str(a) + ' [m/s^2]')
        
        button = Button(frame, text = 'resolve', command = resolve)
        button.pack()
        
    
    # distance traveled
    if b[0] == value[2]:
        for widget in frame.winfo_children():
            widget.destroy()
        frame = tkinter.Frame(window)
        frame.pack()
        initialspeed = []
        distance = []
        timelist = []
        
        input3 = Entry(frame)
        input3.pack()
        label1 = Label(frame, text = 'Initial speed : 0 [m/s]')
        label1.pack()
        label2 = Label(frame, text = 'Distance : 0 [m]')
        label2.pack()
        label3 = Label(frame, text = 'Time : 0 [s]')
        label3.pack()
        
        def initial():
            v = float(input3.get())
            if len(initialspeed) == 0:
                initialspeed.append(v)
            else:
                initialspeed[0] = v
            label1.config(text = 'Initial speed : ' + str(v) + ' [m/s[')
        button = Button(frame, text = 'Initial speed', command = initial)
        button.pack()
        
        def dis():
            d = float(input3.get())
            if len(distance) == 0:
                distance.append(d)
            else:
                distance[0] = d
            label2.config(text = 'Distance : ' + str(d) + ' [m]')
        button = Button(frame, text = 'Distance', command = dis)
        button.pack()
        
        def time():
            t = float(input3.get())
            if len(timelist) == 0:
                timelist.append(t)
            else:
                timelist[0] = t
            label3.config(text = 'Time : ' + str(t) + ' [s]')
        button = Button(frame, text = 'Time', command = time)
        button.pack()
        
        label = Label(frame, text = '\n')
        label.pack()
        label4 = Label(frame, text = 'Acceleration : 0 [m/s^2]')
        label4.pack()
        
        def resolve():
            v = initialspeed[0]
            d = distance[0]
            t = timelist[0]
            a = 2*(d - v*t) / t**2
            label4.config(text = 'Acceleration : ' + str(a) + ' [m/s^2]')
            
        button = Button(frame, text = 'resolve', command = resolve)
        button.pack()
        



combobox = tkinter.ttk.Combobox(window, height = 15, values = value)
combobox.pack()
combobox.set('Given')
combobox.bind('<<ComboboxSelected>>', equation)




    




'''
def acc():
    a =  float(input1.get())
    if len(acclist) == 0:
        acclist.append(a)
    else:
        acclist[0] = a
        label4.config(text = 'Acceleration : ' + str(a) + ' [m/s^2]')
button = Button(window, text = 'acceleration', command = acc)
button.pack()
'''

window.mainloop()