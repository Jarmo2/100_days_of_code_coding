
from tkinter import *
from gui import Interface


window = Tk()

window.title('Typing counter')

window.config(padx=50, pady=50)

e = Interface(window)

window.mainloop()
