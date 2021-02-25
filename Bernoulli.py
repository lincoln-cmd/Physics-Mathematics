# Bernoulli Equation

# P + 0.5pv^2 + pgh = constant
# P1 + 0.5pv_1^2 + pgh_1 = P2 + 0.5pv_2^2 + pgh_2

# set g, p -> constant

# potential result values : P1, P2, v_1, v_2, h_1, h_2
# P = F / A
# W = Fx = PAx = PV (=nRT)
# if V = constant, P2V - P1V = (P2 - P1)V = dW

# choice box, radiobutton

import tkinter
from tkinter import *

glist = []
plist = []
P1list = []
P2list = []
v1list = []
v2list = []
h1list = []
h2list = []
commandlist = []

window = tkinter.Tk()
window.title('Bernoulli Equation')
window.geometry('640x880+100+100')
window.resizable(True, True)

label = Label(window, text = 'the result what you wnat to resovle :')
label.pack()

#result = ['Pressure1', 'Pressure2', 'Velocity1', 'Velocity2', 'height1', 'height2']
radiovariety_1 = IntVar()
#deflist = ['P1', 'P2', 'v1', 'v2', 'h1', 'h2']
#for i in range(len(result)):
 #   radio = Radiobutton(window, text = result[i], value = i, variable = radiovariety_1, command = deflist[i])
  #  radio.pack()
    
    
radio1 = Radiobutton(window, text = 'Pressure1', value = 1, variale = radiovariety_1, command = P1)
radio1.pack()
radio2 = Radiobutton(window, text = 'Pressure2', value = 2, variale = radiovariety_1, command = P2)
radio2.pack()
radio3 = Radiobutton(window, text = 'Velocity1', value = 3, variale = radiovariety_1, command = v1)
radio3.pack()
radio4 = Radiobutton(window, text = 'Velocity2', value = 4, variale = radiovariety_1, command = v2)
radio4.pack()
radio5 = Radiobutton(window, text = 'Height1', value = 5, variale = radiovariety_1, command = h1)
radio5.pack()
radio6 = Radiobutton(window, text = 'Height2', value = 6, variale = radiovariety_1, command = h2)
radio6.pack()


input1 = Entry(window)
input1.pack()

button = Button(window, text = 'Gravitional acceleration')
button.pack()
button = Button(window, text = 'Density')
button.pack()
for i in result:
    button = Button(window, text = i)
    button.pack()

label7 = Label(window, text = '\n\n' + 'Gravitional acceleration : 0[m/s^2]')
label7.pack()
label8 = Label(window, text = 'Density : 0[kg/m^3]')
label8.pack()
label1 = Label(window, text = 'Pressure1 : 0[Pa]')
label1.pack()
label2 = Label(window, text = 'Pressure2 : 0[Pa]')
label2.pack()
label3 = Label(window, text = 'Velocity1 : 0[m/s]')
label3.pack()
label4 = Label(window, text = 'Velocity2 : 0[m/s]')
label4.pack()
label5 = Label(window, text = 'Height1 : 0[m]')
label5.pack()
label6 = Label(window, text = 'Height2 : 0[m]')
label6.pack()

def P1():
    if commandlist[0] == 'P1':
        g = glist[0]
        p = plist[0]
        P2 = P2list[0]
        v1 = v1list[0]
        v2 = v2list[0]
        h1 = h1list[0]
        h2 = h2list[0]
    

window.mainloop()