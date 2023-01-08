from tkinter import *
from  tkinter.ttk import *

from time import strftime     #convert date/time objects to their string representation

root = Tk()
root.title("clock")


def time():
    string=strftime("%H,%M,%S")
    label.config(text=string)
    label.after(1000,time)

label=Label(root,font="lucida 30 bold",background="blue",foreground="cyan")
label.pack(anchor="center")

time()
mainloop()