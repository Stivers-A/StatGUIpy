import tkinter as tk
from tkinter import filedialog
window = tk.Tk()
window.wm_attributes('-topmost', 1) 
window.withdraw()   # this supress the tk window

file_name = filedialog.askopenfilename(
    parent=window,
    initialdir="",
    title="Select A File",
    #this automatically closes after opening the file finder gui of the OS
    filetypes = (("Read Me", "*.md"), ("All files", "*")))
    #This dictates the files that show up
# window.wm_attributes('-topmost', 1) and "parent=window" argument help open the dialog box on top of other windows
print(file_name)