from tkinter import *

root = Tk()

def printName():
    print("Hello my name is Khyron")

button_1 = Button(root, text="Print my name", command=printName)    #command runs the function you tell it
button_1.pack()

root.mainloop()