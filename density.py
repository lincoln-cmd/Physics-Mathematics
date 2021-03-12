# Density
import tkinter
from tkinter import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

'''crawlling'''
'''
import requests
from bs4 import BeautifulSoup

res = requests.get('https://en.wikipedia.org/wiki/Density')

soup = BeautifulSoup(res.content, 'html.parser')

material = []
density = []

for i in range(2, 72):
    data = soup.select('#mw-content-text > div.mw-parser-output > table:nth-child(55) > tbody > tr:nth-child({0}) > td:nth-child(1) > a'.format(i))
    data2 = soup.select('#mw-content-text > div.mw-parser-output > table:nth-child(55) > tbody > tr:nth-child({0}) > td:nth-child(2)'.format(i))
    for i in data:
        material.append(i.get_text())
    for i in data2:
        density.append(i.get_text())

newden = []

for i in density:
    a = i.replace(',', '')
    newden.append(a)

    
print(material)
print(density)
'''
'''crawlling'''

window = tkinter.Tk()
window.title('Density')
window.geometry('640x880+100+100')
window.resizable(True, True)


frame1 = tkinter.Frame(window)
frame1.pack(expand = True, fill = 'both', ipady = 60, pady = 30)

frame1_1 = tkinter.Frame(frame1)
frame1_1.pack(fill = 'x')

frame1_2 = tkinter.Frame(frame1)
frame1_2.pack(fill = 'x')

frame2 = tkinter.Frame(window)
frame2.pack(expand = True, fill = 'both', ipady = 60, pady = 30)

input1 = Entry(frame1_1)
input1.insert(0, 'Weight/mass [kg]')
input1.pack()
def wei():
    weight = input1.get() # input the weight/mass
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
    vol = input2.get() # input the vlume
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
        except: # if the value of the weight/mass is not defined, alarm the error message
            messagebox.showerror('Weight/mass error','The value of \'Weight/mass\' has to have float value')
        try:
            vol = float(input2.get())
        except: # if the value of the volume is not defined, alarm the error message
            messagebox.showerror('Volume error', 'The value of \'Volume\' has to have float value')
         
button = Button(frame1, text = 'resolve', command = resolve)
# even though the weight/mass and volume button are not put, if those values are inserted in Entry, the density value can be resolved because the function(definition) 'resolve' can get the values of weight/mass and volume from directly from the entry by utilizing the get() methode
button.pack(side = 'bottom')

material = ['Hydrogen', 'Helium', 'Aerographite', 'Metallic microlattice', 'Aerogel', 'Air', 'Tungsten hexafluoride', 'Liquid hydrogen', 'Styrofoam', 'Cork', 'Pine', 'Lithium', 'Wood', 'Oak', 'Potassium', 'Ice', 'Cooking oil', 'Sodium', 'Water(fresh)', 'Water(salt)', 'Liquid oxygen', 'Nylon', 'Plastics', 'Glycerol', 'Tetrachloroethene', 'Sand', 'Magnesium', 'Beryllium', 'Concrete', 'Glass', 'Silicon', 'Quartzite', 'Granite', 'Gneiss', 'Aluminium', 'Limestone', 'Basalt', 'Diiodomethane', 'Diamond', 'Titanium', 'Selenium', 'Vanadium', 'Antimony', 'Zinc', 'Chromium', 'Tin', 'Manganese', 'Iron', 'Niobium', 'Brass', 'Cadmium', 'Cobalt', 'Nickel', 'Copper', 'Bismuth', 'Molybdenum', 'Silver', 'Lead', 'Thorium', 'Rhodium', 'Mercury', 'Tantalum', 'Uranium', 'Tungsten', 'Gold', 'Plutonium', 'Rhenium', 'Platinum', 'Iridium', 'Osmium']
density = ['0.0898', '0.179', '0.2', '0.9', '1.0', '1.2', '12.4', '70', '75', '240', '373', '535', '700', '710', '860', '916.7', '920', '970', '1000', '1030', '1141', '1150', '1175', '1261', '1622', '1600', '1740', '1850', '2400', '2500', '2330', '2600', '2700', '2700', '2700', '2750', '3000', '3325', '3500', '4540', '4800', '6100', '6690', '7000', '7200', '7310', '7325', '7870', '8570', '8600', '8650', '8900', '8900', '8940', '9750', '10220', '10500', '11340', '11700', '12410', '13546', '16600', '18800', '19300', '19320', '19840', '21020', '21450', '22420', '22570']



frame2_1 = tkinter.Frame(frame2)
frame2_1.pack()

g = 9.8
label4 = Label(frame2_1, text = 'Density : 0 [kg/m^3]')
label5 = Label(frame2_1, text = 'Pressure : 0 [Pa]')
label6 = Label(frame2_1, text = 'Volume : 0 [m^3]')
label7 = Label(frame2_1, text = 'Force : 0 [kg]')

scrollbar = tkinter.Scrollbar(frame2_1)
scrollbar.pack(side = 'right', fill = 'y')
listbox = Listbox(frame2_1, yscrollcommand = scrollbar.set, selectmode = 'single')
for i in range(len(material)):
    listbox.insert(i, str(material[i]))
listbox.pack(side = 'left')

def poll(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        d = density[index]
        p = g * float(d)
        v = 1 / float(d)
        m = float(d) * g
        label4.config(text = 'Density : ' + str(d) + ' [kg/m^3]')
        label5.config(text = 'Pressure : ' + str(p) + ' [Pa]')
        label6.config(text = 'Volume : ' + str(v) + ' [m^3]')
        label7.config(text = 'Force : ' + str(m) + ' [N]')
listbox.bind('<<ListboxSelect>>', poll)
label4.pack()
label5.pack()
label6.pack()
label7.pack()

label = Label(frame2, text = '* The Pressure is estimated in the situation when the "height" is 1[m] \n and the "gravitiona acceleration" is 9.8[m/s^2]. (P = pgh)')
label.pack(ipady = 10)
label = Label(frame2, text = '* The Volume is 1kg of the selected matter accounts for. (V = m / p)')
label.pack(ipady = 10)
label = Label(frame2, text = '* The Force is the weight of the selected matter which \n accounts for 1m^3 of volume in Earth. (m = pV, g = 9.8 [m/s^2])')
label.pack()

window.mainloop()