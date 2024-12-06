from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Stats GUI  Py")
mainframe = ttk.Frame(root, padding="3 3 12 12")
#replaces the root with a tinker themes frame consistent asthetics between this and sub widgets
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
#borrowed from feet to meters, automatically adds padding to all widgets in mainframe

root.mainloop()
#closes the loop