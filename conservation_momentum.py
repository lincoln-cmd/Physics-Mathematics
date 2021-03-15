# Conservation of Momentum(in collision)

import tkinter
from tkinter.ttk import Combobox
from tkinter import *

window = tkinter.Tk()
window.title('Conservation of momentum')
window.geometry('640x880+100+100')
window.resizable(True, True)

frame1 = Frame(window)
frame1.pack(expand = True, fill = 'both', ipady = 5, pady = 5)

frame1_1 = Frame(frame1) # collision type -> fill x axis -> combobox
frame1_1.pack(expand = True, fill = 'both', ipady = 5, pady = 5)

frame1_2 = Frame(frame1) # result value what I want to calculate -> listbox
frame1_2.pack(expand = True, ipady = 5, pady = 5)

elements = ['Mass1', 'Initial velocity(1)', 'Final velocity(1)', 'Mass2', 'Initial velocity(2)', 'Final velocity(2)']

scrollbar = tkinter.Scrollbar(frame1_2)

listbox = Listbox(frame1_2, yscrollcommand = scrollbar.set, selectmode = 'single')
for i in range(len(elements)):
    listbox.insert(i, str(elements[i]))


frame1_3 = Frame(frame1)# entry frame where I can insert the given values
frame1_3.pack(expand = True, fill = 'both')


frame2 = Frame(window) # Frame where the results show up
frame2.pack(expand = True, fill = 'both', ipady = 10, pady = 10)


# Inelastic collision : https://byjus.com/physics/inelastic-collision/
collisiontype = ['Perfect elastic', 'Partially elastic', 'Perfectly inelastic']
inputlist = ['input1', 'input2', 'input3', 'input4', 'input5']

    
combobox = tkinter.ttk.Combobox(frame1_1, height = 15, values = collisiontype)

def poll(event):
    scrollbar.pack(side = 'right', fill = 'y')
    listbox.pack()
    c = combobox.get()
    def libox(event2):
        selection = event2.widget.curselection() # selection is converted as int of tuple
        if c == collisiontype[0]:
            list2 = []
            for i in range(len(elements)):
                if i != selection[0]:
                    list2.append(elements[i])
            for i in range(len(inputlist)):
                inputlist[i] = Entry(frame1_3)
                inputlist[i].insert(0, list2[i])
                inputlist[i].pack()
            
                
    listbox.bind('<<ListboxSelect>>', libox)

def resovle():
    global selection
    i = selection[0]
    if i == elements[0]:
        u1 = input1.get() # initial velocity of object1
        v1 = input2.get() # final velocity of object1
        m2 = input3.get() # mass of object2
        u2 = input4.get() # initial velocity of object2
        v2 = input5.get() # final velocity of object2
        m1 = m2*(v2 - u2) / (u1 - v1) # mass of object1
        
        
        

combobox.pack()
combobox.set('Given')
combobox.bind('<<ComboboxSelected>>', poll)
listbox.bind('<<ListboxSelect>>', poll)            


window.mainloop()