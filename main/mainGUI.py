from tkinter import *
from tkinter import ttk
import sv_ttk
from fileDialog import file_opener
def fileSelect():
    file_name = file_opener()
    print(file_name, "print from mainGUI")


root = Tk()
root.title("Stats GUI  Py")
mainframe = ttk.Frame(root, padding="3 3 12 12")
#replaces the root with a tinker themes frame consistent asthetics between this and sub widgets
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Button(mainframe, text="Select File", command=fileSelect).grid(column=1, row=1, sticky=N)
ttk.Button(mainframe, text="Box").grid(column=9, row=1, sticky=N)
ttk.Button(mainframe, text="Box2").grid(column=8, row=9, sticky=N)


ttk.Label(mainframe, text="").grid(column=2, row=2, sticky=(W, E))

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
#borrowed from feet to meters, automatically adds padding to all widgets in mainframe
sv_ttk.set_theme("light")
root.mainloop()
#closes the loop