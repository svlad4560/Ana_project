from tkinter import *
#what is TK
root = Tk()

def myClick():
    myLabel = Label(root, text = "your fucked")
    myLabel.pack()


myButton = Button(root, text = "click me", pady = 50, command = myClick)
myButton.pack()

root.mainloop()
