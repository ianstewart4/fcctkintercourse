from tkinter import *

root = Tk()

e = Entry(root, width="50")
e.pack()
e.insert(0, "Enter Your Name: ")


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Click Me!", padx=50, command=myClick)
myButton.pack()

# Creating label widget
# myLabel1 = Label(root, text="Hello world!")
# myLabel2 = Label(root, text="My name is Ian!")

# # Shoving it onto the screen
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=0)

root.mainloop()