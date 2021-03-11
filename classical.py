import tkinter
from tkinter import *

window = tkinter.Tk()
window.title('Classical mechanics')
window.geometry('640x880+100+100')
window.resizable(True, True)

label = Label(window, text = 'Classical mechanics', height = 5, fg = 'red', relief = 'solid')
label.pack(pady = 30)

def acc():
        # Acceleration
    
    import tkinter
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
        # destroy 안됨
            frame = tkinter.Frame(window)
            frame.pack()
            b.append(c)
        else:
            frame.destroy()
            frame = tkinter.Frame(window)
            frame.pack()
            b[0] = c
    
            
        # speed difference
        if b[0] == value[0]:
            if frame is True:
                frame.deestory()
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
            if frame is True:
                frame.deestory()
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
            if frame is True:
                frame.deestory()
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
    
def den():
        # Density
    import tkinter
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
             
    button = Button(frame1, text = 'resolve', command = resolve)
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

button1 = Button(window, text = 'Acceleration', relief = 'groove', command = acc)
button1.pack(fill = 'x')
button2 = Button(window, text = 'Density', relief = 'groove', command = den)
button2.pack(fill = 'x')



window.mainloop()