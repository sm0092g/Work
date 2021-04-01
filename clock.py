import time as tm
import tkinter as tk

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.clock_label=tk.Label(self.root, font="ariel 80", bg="black", fg="green")
        self.clock_label.grid(row=0, column=0)
        self.display_time()
    
    def display_time(self):
        self.current_time = tm.strftime("%H:%M:%S")
        self.clock_label["text"] = self.current_time
        self.root.after(200,self.display_time)

root = tk.Tk()
digital_clock = DigitalClock(root)
root.mainloop()