
from tkinter import *
from tkinter import ttk

# find out how to orient tkinter for graphing

root = Tk()

canvas = Canvas( width=500, height=400)

canvas.create_line(10,5, 200, 50)

root.mainloop()
