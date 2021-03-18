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

frame1_4 = Frame(frame1)

frame2 = Frame(window) # Frame where the results show up
frame2.pack(expand = True, fill = 'both', ipady = 10, pady = 10)

label1 = Label(frame2, text = '')
label1.pack()

# Inelastic collision : https://byjus.com/physics/inelastic-collision/
collisiontype = ['Perfectly elastic', 'Partially elastic', 'Perfectly inelastic']
inputlist = ['input1', 'input2', 'input3', 'input4', 'input5']

combobox = tkinter.ttk.Combobox(frame1_1, height = 15, values = collisiontype)

def poll(event):
    scrollbar.pack(side = 'right', fill = 'y')
    listbox.pack()
    c = combobox.get()
    frame1_3 = Frame(frame1)
    frame1_3.pack(expand = True, fill = 'both')
    
    def libox(event2):
        #selection = listbox.curselection() # selection is converted as int of tuple
        selectlist = []
        if c == collisiontype[0]:
            frame1_3 = Frame(frame1) # refresh the frame1_3 whenever the selected item in listbox is changed
            frame1_3.pack(expand = True, fill = 'both')
            list2 = []
            for i in range(len(elements)):
                selection = event2.widget.curselection()
                if len(selectlist) == 0:
                    selectlist.append(selection[0])
                else:
                    selectlist[0] = selection[0]
                if i != selection[0]:
                    list2.append(elements[i])
            for i in range(len(inputlist)):
                inputlist[i] = Entry(frame1_3)
                inputlist[i].insert(0, list2[i])
                inputlist[i].pack()
                print(inputlist[i])
      
        def resolve():
            i = selectlist[0]
            print(i)
            if i == elements.index('Mass1'):
                u1 = float(input1.get()) # initial velocity of object1
                v1 = float(input2.get()) # final velocity of object1
                m2 = float(input3.get()) # mass of object2
                u2 = float(input4.get()) # initial velocity of object2
                v2 = float(input5.get()) # final velocity of object2
                m1 = m2*(v2 - u2) / (u1 - v1) # mass of object1
                label1.config(text = 'Mass1 : ' + str(m1) + ' [kg]')

        button = Button(frame1_3, text = 'resolve', command = resolve)
        button.pack()
        
        
    listbox.bind('<<ListboxSelect>>', libox)



combobox.pack()
combobox.set('Given')
combobox.bind('<<ComboboxSelected>>', poll)
listbox.bind('<<ListboxSelect>>', poll)            


window.mainloop()