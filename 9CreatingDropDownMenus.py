from tkinter import *

def doNothing():
    print("Ok i wont")

root = Tk()

themenu = Menu(root)
root.config(menu=themenu)

subMenu = Menu(themenu)
themenu.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="New Project......", command=doNothing)
subMenu.add_command(label="New......", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(themenu)
themenu.add_cascade(label="Edit", menu = editMenu)
editMenu.add_command(label = "Redo", command = doNothing)

root.mainloop()