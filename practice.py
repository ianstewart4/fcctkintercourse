from tkinter import *

root = Tk()

#creating label widget
myLabel1 = Label(root, text="Hello world!")
myLabel2 = Label(root, text="My name is Ian!")

myLabel1.grid(row=0, column=0)
myLabel1.grid(row=1, column=0)

root.mainloop()
