import math
import tkinter as tk
from tkinter import *

win = tk.Tk()
win.geometry("500x380")

eoutput = StringVar()
eoutput.set("Output goes here")

def calculate():
    a = e1.get()
    b = e2.get()
    c = e3.get()
    d = e4.get()
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    
    s = float(a + b + c) / 2
    if d == 0:
        answer = math.sqrt(s * (s - a) * (s - b) * (s - c))
        answer = str(answer)
    elif d !=0:
        answer = b * d / 2
        answer = str(answer)
    a_entry.delete(0,END)
    a_entry.insert(0,answer)


b1 = Button(win, text="Calculate!", command = calculate)
triphoto = PhotoImage(file="triangle.png")
l1 = Label(win, image=triphoto)
l2 = Label(win, text="Enter in as much information about the\ntriangle shown and I will calculate the area.\nIf you don't know the height, enter 0.")
a_entry = Entry(win, width=15, textvariable = eoutput)
e1 = Entry(win, width=4)
e2 = Entry(win, width=4)
e3 = Entry(win, width=4)
e4 = Entry(win, width=4)

l1.place(x=0,y=0)
l2.place(x=10,y=285)
b1.place(x=350,y=285)
a_entry.place(x=350,y=330)
e1.place(x=170,y=110)
e2.place(x=270,y=220)
e3.place(x=380,y=110)
e4.place(x=310,y=120)
win.mainloop()