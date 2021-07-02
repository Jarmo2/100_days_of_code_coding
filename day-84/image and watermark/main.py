from picture_manipulator import Watermarker
from gui import Interface
import tkinter as tk


root = tk.Tk()

app = Interface(master=root)

app.mainloop()
test = Watermarker.watermark_text(app.filename, 'test_watermarked.jpg', text="Jarmo's Python endeavour", pos=(0, 0))

