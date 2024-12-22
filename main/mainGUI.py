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
    assesedValues = []
#a matrix that can be filled
    with open (file_name,'r',newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if is_row:
            for row in reader:
                assesedValues.append(float(row[bar]))
        else:
            for col in reader:
                assesedValues.append(float(col[bar]))
        print(assesedValues)
#selecting row/column by name
bar = StringVar()
def bar_entry_save():
    global bar
    bar = bar_entry.get()
    print("bar entry saved ", bar)

root = Tk()
root.title("Stats GUI  Py")
mainframe = ttk.Frame(root, padding="3 3 12 12")
#replaces the root with a tinker themes frame consistent asthetics between this and sub widgets
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Button(mainframe, text="Select File", command=fileSelect).grid(column=1, row=1, sticky=N)
ttk.Button(mainframe, text="Finalize Selection",command=confirmSelect).grid(column=9, row=1, sticky=N)


bar_entry = ttk.Entry(mainframe, width=25, textvariable=bar)
bar_entry.grid(column=3, row=2, sticky=(W, E))

bar_entry_confirm = ttk.Button(mainframe, text="Confirm Column Name",command=bar_entry_save)
bar_entry_confirm.grid(column=4, row=2, sticky=N)


#row or column toggle
is_row = True
 
# Define our switch function
def switch():
    global is_row
     
    # Determine col or row TRUE = row
    if is_row:
        bar_button.config(text = "Set to Column")
        is_row = False
        bar_name.config(text = "Row Title:")
        bar_entry_confirm.config(text = "Confirm Row Name")


    else:
       bar_button.config(text = "Set to Row") 
       is_row = True
       bar_name.config(text = "Column Title:")
       bar_entry_confirm.config(text = "Confirm Column Name")

 
# Create A Button
bar_button = ttk.Button(mainframe, text="Set to Row",command = switch)
bar_button.grid(column=3, row=1, sticky=(W, E))
# Button Description
bar_name = ttk.Label(mainframe, text="Column Title:")
bar_name.grid(column=2, row=2, sticky=(W, E))



for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
#borrowed from feet to meters, automatically adds padding to all widgets in mainframe
sv_ttk.set_theme("light")
root.mainloop()
#closes the loop