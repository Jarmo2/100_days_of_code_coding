import tkinter
from tkinter import *
from text_module import TextMachine
import time
import config
from datetime import datetime

class Interface:

    def __init__(self, master):
        self.myframe = Frame(master)
        self.myframe.grid()

        self.canvas = Canvas(height=600, width=400)
        self.logo_img = PhotoImage(file="Computer_Workstation_Variables.png")
        self.canvas.create_image(200, 300, image=self.logo_img)
        self.canvas.grid(row=1, column=0)

        self.end_button = Button(master, text="Click here to submit your text.", command=lambda:[self.evaluate_the_text(),
                                                                                                self.end_countdown(), self.entered_text_label.config(state=tkinter.DISABLED), self.reset()])
        self.end_button.grid(row=3, column=2)

        self.start_button = Button(master, text="Click here to start your test", command=lambda: [self.start_count_down(),
                                                                                                  self.clock(), self.start(),
                                                                                                  self.entered_text_label.config(state=tkinter.NORMAL)])
        self.start_button.grid(row=2, column=1)

        self.entered_text_label = Label(text="Please type your text above")
        self.entered_text_label.grid(row=2, column=2)

        self.entered_text_label = Entry(width=35, state='disabled')
        self.entered_text_label.grid(row=1, column=2, columnspan=2, rowspan=5, ipady=20)
        self.entered_text_label.focus()

        self.heading_label = Label()
        self.heading_label.config(text="Ready to type like a Gottfried Benn?", font=("arial", 15, "bold"), fg="Green", bg="Yellow")
        self.heading_label.grid(column=2, row=0)

        self.result_text = "Your result will be shown here."
        self.result_label = Label()
        self.result_label.config(text=self.result_text, font=("arial", 10, "bold"), fg="BLACK", bg="GREEN")
        self.result_label.grid(column=1, row=0)

        self.text_to_type = Text()
        self.text_to_type.grid(column=1, row=1)
        self.selected_text = "Your text will appear here"
        self.text_to_type.insert(END, self.selected_text)

        self.start_time = 0
        self.end_time = 0
        self.time_lapsed = 0
        self.word_words_typed = 0

        self.timeFrame = LabelFrame(self.myframe, text='The tick of the clock')
        self.timeFrame.grid(row=1, column=2)
        self.show = Label(self.timeFrame, text='00:00:00', font=('Helvetica', 30))
        self.show.grid(row=1, column=2)
        self.counter = 0


    def evaluate_the_text(self):
        text_received = str(self.entered_text_label.get())
        TextMachine().check_words_typed(text_received)


    def start_count_down(self):
        self.start_time = time.time()
        self.text_to_type.delete(1.0, END)
        self.text_to_type.insert(END, TextMachine().choose_text())
        return self.start_time

    def end_countdown(self):

        self.time_lapsed = time.time() - self.start_time
        self.result_text = f"You typed this text in {self.time_lapsed} seconds. You typed {config.number_of_words_typed} words correctly." \
                            f"The original text contained {config.number_of_words} words."
        self.result_label.config(text=self.result_text)
        self.running = False


    def clock(self):
        self.running = False
        self.timer = [0, 0, 0]  # [minutes ,seconds, centiseconds]
        self.timeString = str(self.timer[0]) + ':' + str(self.timer[1]) + ':' + str(self.timer[2])
        self.update_time()


    def update_time(self):
        def count():
            if self.running == True:  # Clock is running
                tt = datetime.fromtimestamp(self.counter)
                string = tt.strftime("%H:%M:%S")
                display = string
                self.show.config(text=display)
                self.counter += 1
        count()
        self.myframe.after(1000, self.update_time)

    def start(self):  # Start the clock
        self.running = True


    def reset(self):  # Reset the clock
        self.start_button.config(text="Try another one?", command=lambda:[self.start_count_down(), self.clock(), self.start(),
                                 self.entered_text_label.config(state=tkinter.NORMAL), self.result_label.config(text="Your result will be shown here."),
                                self.entered_text_label.delete(0, 'end')])























