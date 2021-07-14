import tkinter as tk
import tkinter.ttk as ttk
import datetime


class TkinterGUI:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Stop thinking start typing")
        self.window.geometry('700x600')
        self.selected = tk.IntVar()

        #progess bar which should run from full to empty
        # progress bar
        self.bar = ttk.Progressbar(self.window, length=300)
        self.bar['value'] = 100
        self.bar.grid(column=0, row=0, columnspan=3)


        #labels to greet
        self.lbl = tk.Label(self.window, text="Are you ready to type?", font=("Futura", 50))
        self.lbl.grid(column=0, row=1, columnspan=3)
        self.lbl_2 = tk.Label(self.window, text="Please choose below the level of pressure you need", font=("Futura", 10))
        self.lbl_2.grid(column=1, row=2)
        self.lbl_3 = tk.Label(self.window, text="Don't forget to save your precious text", font=("Futura", 10))
        self.lbl_3.grid(column=0, row=6, columnspan=3)

        #radio buttons
        self.selected = tk.IntVar()
        self.rad1 = ttk.Radiobutton(self.window, text='5 seconds', value=5, variable=self.selected)
        self.rad2 = ttk.Radiobutton(self.window, text='10 seconds', value=10, variable=self.selected)
        self.rad3 = ttk.Radiobutton(self.window, text='15 seconds', value=15, variable=self.selected)
        self.rad1.grid(column=0, row=3)
        self.rad2.grid(column=1, row=3)
        self.rad3.grid(column=2, row=3)

        #normal buttons
        self.btn = tk.Button(self.window, text="Confirm time", command=self.update_screen)
        self.btn.grid(column=3, row=3)
        self.btn_stop = tk.Button(self.window, text="Stop Countdown and reset", command=lambda: self.countdown(run=False))
        self.btn_stop.grid(column=2, row=8)
        self.btn_save = tk.Button(self.window, text="Stop and Save", command=lambda: [self.countdown(run=False), self.save()])
        self.btn_save.grid(column=0, row=8)

        #textfield
        self.entered_text_label = tk.Text(height=20, width=50)
        self.entered_text_label.grid(row=5, column=0, columnspan=3)


    def update_screen(self):
        self.t = self.selected.get()
        self.t_org = self.t
        self.lbl.config(text=f"Your countdown runs for {self.t} seconds.", font=("Futura", 30))
        run = True
        self.countdown(run)


    def countdown(self, run):
        global job1
        if run == True:
            self.lbl_3.config(text=f"Don't forget to save your precious text")
            if self.t > 0:
                # call countdown again after 1000ms (1s)
                self.t -= 1
                print(self.t, self.t_org)
                self.bar.config(value=(self.t/self.t_org)*100)
                self.check_typing()
                if self.t == 0:
                    self.refresh()
                job1 = self.window.after(1000, self.countdown, run)
        else:
            self.window.after_cancel(job1)


    def check_typing(self):
        def key_pressed(event):
            self.t = self.t_org

        self.window.bind("<Key>", key_pressed)

    def refresh(self):
            self.entered_text_label.delete("1.0", "end")


    def save(self):
        with open('saved.txt', 'a') as f:
            f.write(f"{datetime.datetime.now()} '\n' {self.entered_text_label.get('1.0', 'end-1c')} '\n'")
            self.entered_text_label.delete("1.0", "end")
            self.lbl_3.config(text=f"Your text has been saved.")












