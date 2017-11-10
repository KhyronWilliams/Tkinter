from tkinter import *

root = Tk()                    #creates blank window

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", bg="red")
button2 = Button(topFrame, text="Button 2", bg="green")
button3 = Button(topFrame, text="Button 3", fg="blue")
button4 = Button(bottomFrame, text="Button 4", fg="purple")

button1.pack()
button2.pack()
button3.pack()
button4.pack()



root.mainloop()                                  #makes the window constantly displays
