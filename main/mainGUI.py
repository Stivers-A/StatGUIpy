from tkinter import *
from tkinter import ttk
import sv_ttk
from fileDialog import file_opener
import csv


file_name = ""
def fileSelect():
    global file_name 
    file_name = file_opener()
    print(file_name, "print from fileSelect")
    #uses file_opener in fileDialog to save the path to a file as file_name
def confirmSelect():
    global file_name
    print(file_name, "print from confirmSelect")
        


root = Tk()
root.title("Stats GUI  Py")
mainframe = ttk.Frame(root, padding="3 3 12 12")
#replaces the root with a tinker themes frame consistent asthetics between this and sub widgets
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Button(mainframe, text="Select File", command=fileSelect).grid(column=1, row=1, sticky=N)
ttk.Button(mainframe, text="Confirm Selection",command=confirmSelect).grid(column=9, row=1, sticky=N)

bar = StringVar()
bar_entry = ttk.Entry(mainframe, width=25, textvariable=bar)
bar_entry.grid(column=3, row=2, sticky=(W, E))
#first creates a string for feet, then creates an entry text box that assigns its input to feet
ttk.Button(mainframe, text="Box2").grid(column=8, row=9, sticky=N)


ttk.Label(mainframe, text="Barname Name").grid(column=2, row=2, sticky=(W, E))

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
#borrowed from feet to meters, automatically adds padding to all widgets in mainframe
sv_ttk.set_theme("light")
root.mainloop()
#closes the loop