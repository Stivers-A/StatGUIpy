from tkinter import *
from tkinter import ttk
import sv_ttk
from fileDialog import file_opener
import csv
import pandas as pd
import statistics
file_name = ""
assesedValues = []
def output_print():
    global assesedValues
    #input assesedValues
    #output mean, median , mode & range
    #first up mean

    mean = statistics.mean(assesedValues)
    print("mean", mean)
    mean_rounded = round(mean,2)
    mean_output = str(mean_rounded)
    mean_display.config(text = ("Mean:", mean_output))
    #rounds mean then converts to string
    #mean get
    median = statistics.median(assesedValues)
    print("median", median)
    #median get
    mode = statistics.mode(assesedValues)
    print("mode",mode)
    #mode get
    min_val = min(assesedValues)
    max_val = max(assesedValues)
    #range is minimum and maximum
    print("range",min_val," to ", max_val)
    #range get
    standard_dev = statistics.stdev(assesedValues)
    print("Standard Deviation", standard_dev)

def fileSelect():
    global file_name 
    file_name = file_opener()
    print(file_name, "print from fileSelect")
    #uses file_opener in fileDialog to save the path to a file as file_name
def confirmSelect():
    global file_name
    global assesedValues
    print(file_name, "print from confirmSelect")
#a matrix that can be filled
    with open (file_name,'r',newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if is_row:
            for row in reader:
                assesedValues.append(float(row[bar]))
        else:
            print("string var", bar)
            int(bar)
            print("int", bar)
            df = pd.DataFrame({file_name})
            assesedValues = df.iloc[bar].tolist()
        print(assesedValues)
        output_print()
#selecting row/column by name
bar = StringVar()
def bar_entry_save():
    global bar
    bar = bar_entry.get()
    print("bar entry saved ", bar)
    #selects col name or row number

root = Tk()
root.title("Stats GUI  Py")
mainframe = ttk.Frame(root, padding="3 3 12 12")
#replaces the root with a tinker themes frame consistent asthetics between this and sub widgets
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Button(mainframe, text="Select File", command=fileSelect).grid(column=1, row=1, sticky=N)
ttk.Button(mainframe, text="Confirm Selection",command=confirmSelect).grid(column=9, row=1, sticky=N)


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
        bar_name.config(text = "Row Number:")
        bar_entry_confirm.config(text = "Confirm Row Number")


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

#Outputs
mean_display = ttk.Label(mainframe, text="mean_display")
mean_display.grid(column=1, row=5, sticky=(W, E))
#mean
median_display = ttk.Label(mainframe, text="median_display")
median_display.grid(column=2, row=5, sticky=(W, E))
#median
mode_display = ttk.Label(mainframe, text="mode_display")
mode_display.grid(column=3, row=5, sticky=(W, E))
#mode
range_display = ttk.Label(mainframe, text="range_display")
range_display.grid(column=4, row=5, sticky=(W, E))
#range
stdev_display = ttk.Label(mainframe, text="stdev_display")
stdev_display.grid(column=5, row=5, sticky=(W, E))
#standard deviation

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
#borrowed from feet to meters, automatically adds padding to all widgets in mainframe
sv_ttk.set_theme("light")
root.mainloop()
#closes the loop