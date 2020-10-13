from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import Frame, Tk, Button, Label, Entry
from tkinter import ttk

def add():
    wght = float(Weight.get())
    hght = float(Height.get())
    rslts = wght / ((hght/100)**2)
    #Results.set(rslts)
    window.Height_Label.configure(text=round(rslts, 2)),"\n"
    if rslts<18.5:
        window.Height_Label.configure(text="Underweight")
    elif rslts>=18.5 and rslts<25:
         window.Height_Label.configure(text="Normal weight")
    elif rslts>=25 and rslts<30:
         window.Height_Label.configure(text="Overweight")
    elif rslts>30:
         window.Height_Label.configure(text="Obese")
    else:
         window.Height_Label.configure(text="unclassified")
    return rslts


window = tk.Tk()
window.title("My BMI")
window.config(bg="#CCE8F9", padx=5, pady=5)

framemcolour = "White"
padding = 7
framem = tk.Frame(window)
framem.config(bg=framemcolour, padx=10, pady=10)
framem.grid(column=0, row=0, padx=20, pady=10)


Heading1 = Label (framem, text="Calculate your BMI")
Heading1.grid(column=0, row = 0, columnspan = 4, pady = padding)
Heading1.config(width = 24, height = 2, bg = "#CCE8F9",font = ("Calibri bold", 24),fg = "black",)

weight_Label = StringVar
height_Label = StringVar
Results = StringVar

window.Weight_Label = Label (framem, text = "Enter your weight in kg \n to the right:")
window.Weight_Label.grid(column = 0, row = 2, columnspan = 2, pady = padding)
window.Weight_Label.config(width = 26, height = 2, bg ="#EDF7FD",
               fg = "black",
               font = ("Calibri bold", 14), justify = "center")


window.Height_Label = Label (framem, text = "  Enter your height in centimeters \n to the right:")
window.Height_Label.grid(column = 0, row = 4, columnspan = 2, pady = padding)
window.Height_Label.config(width = 26, height = 2, bg ="#EDF7FD",
               fg = "black",
               font = ("Calibri bold", 14), justify = "center")

#####################################################################
window.Height_Label1 = Label (framem, text = "Your BMI is:")
window.Height_Label1.grid(column = 0, row = 10, columnspan = 2, pady = padding)
window.Height_Label1.config(width = 26, height = 2, bg ="#EDF7FD",
               fg = "black",
               font = ("Calibri bold", 14), justify = "center")






Weight = Entry (framem)
Weight.grid(column = 3, row = 2, sticky="e")
Weight.config(width = 4, bg = "white", fg = "black",
            relief = "ridge", justify = "center",
            font = ("Calibri", 26))

Height = Entry (framem)
Height.grid(column = 3, row = 4, sticky = "e")
Height.config(width = 4, bg = "white", fg = "black",
            justify = "center",
            font = ("Calibri", 26))


Gender_Label = Label (framem, text = "  Enter your height in meters \n to the right:")
Gender_Label.grid(column = 0, row = 6, columnspan = 2, pady = padding)
Gender_Label.config(width = 26, height = 2, bg ="#EDF7FD",
               fg = "black",
               font = ("Calibri bold", 14), justify = "center")

PressMe=Button(framem, text = "Press to find \n your BMI", command=add)
PressMe.grid(row = 8, column = 1, columnspan = 2, pady = padding, sticky = "w")
PressMe.config(width = 19, height = 2, bg = "dark blue", fg = "white",
               bd = 3, relief = "ridge",
               font = ("Calibri bold", 14, "bold"))

v = IntVar()
Gender_Male = Radiobutton(framem, text="Male", variable=v, value=1)
Gender_Female = Radiobutton(framem, text="Female", variable=v, value=2)

Gender_Male.grid(column = 2, row = 6)
Gender_Male.config(width = 5, bg="White", fg = "black",
            justify = "center",
            font = ("Calibri", 12))

Gender_Female.grid(column = 3, row = 6)
Gender_Female.config(width = 5, bg="White", fg = "black",
            justify = "center",
            font = ("Calibri", 12))
v.set(1)

Convert = Label(framem, text = "")
Convert.grid(column = 0, row = 12, columnspan = 4, pady = padding, sticky = "nsew")
Convert.config(width = 0, height = 2, bg = "white", fg = "black",
               font = ("Calibri bold", 14, "bold"))



window.mainloop()
