import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askyesno, showinfo
from picture_manipulator import Watermarker


class Interface(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.filename = None


    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World!\n" \
                                "Would you like\n"\
                                "to upload a picture\n" \
                                "and put a watermark\n" \
                                "on it with the help of \n" \
                                "this shitty application\n" \
                                "which time traveled from\n" \
                                "the early 90s directly in\n" \
                                "your face?\n" \
                                "(click me)"
        self.hi_there["command"] = self.uploadaction
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def confirm(self):
        answer = askyesno(title='confirmation',
                          message='Are you sure you want to convert?')
        if answer == False:
            self.uploadaction()


    def uploadaction(self):
        filepath = askopenfilename()
        if len(filepath) < 3:
            showinfo("No file?", "Please select a file")
            self.uploadaction()
        answer = askyesno(title='confirmation',
                          message='Are you sure you want to convert?')
        if answer:
            return Watermarker.watermark_text(filepath, 'test_watermarked.jpg', text="Jarmo's Python endeavour", pos=(0, 0))

        if answer == False:
            showinfo("Really?", "I am afraid you are a coward.")
            self.master.destroy
