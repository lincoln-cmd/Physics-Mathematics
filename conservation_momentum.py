# Conservation of Momentum(in collision)

import tkinter
from tkinter import *

window = tkinter.Tk()
window.title('Conservation of momentum')
window.geometry('640x880+100+100')
window.resizable(True, True)

frame1 = Frame(window, bg = 'red')
frame1.pack(expand = True, fill = 'both', ipady = 5, pady = 5)

frame1_1 = Frame(frame1, bg = 'green') # collision type -> fill x axis -> combobox
frame1_1.pack(expand = True, fill = 'both', ipady = 5, pady = 5)

frame1_2 = Frame(frame1, bg = 'white') # result value what I want to calculate -> listbox
frame1_2.pack(expand = True, ipady = 5, pady = 5)
scrollbar = tkinter.Scrollbar(frame1_2)
scrollbar.pack(side = 'right', fill = 'y')
listbox = Listbox(frame1_2, yscrollcommand = scrollbar.set, selectmode = 'single')
for i in range(len(elements)):
    listbox.insert(i, str(elements[i]))


frame1_3 = Frame(frame1, bg = 'yellow') # entry frame where I can insert the given values
frame1_3.pack(expand = True, fill = 'both')


frame2 = Frame(window, bg = 'blue') # Frame where the results show up
frame2.pack(expand = True, fill = 'both', ipady = 10, pady = 10)


# Inelastic collision : https://byjus.com/physics/inelastic-collision/
collisiontype = ['Perfect elastic', 'Partially elastic', 'Perfectly inelastic']
elements = ['Mass1', 'Initial velocity(1)', 'Final velocity(1)', 'Mass2', 'Initial velocity(2)', 'Final velocity(2)']



def poll(event):
    listbox.pack()
    c = combobox.get()
    def libox(event):
        selection = event.widget.curselection()
        if c == collisiontype[0]:
            list2 = []
            for i in elements:
                list2.append(i)
                if i == selection:
                    pass
            for i in list2:
                input1 = Entry(frame1_3)
                input1.insert(0, i)
                input1.pack()
        
        

combobox = tkinter.ttk.Combobox(frame1_1, height = 15, values = collisiontype)
combobox.pack()
combobox.set('Given')
combobox.bind('<<ComboboxSelected>>', poll)
listbox.bind('<<ListboxSelect>>', poll)
            


window.mainloop()