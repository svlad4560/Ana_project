from tkinter import *
#what is TK
root = Tk()
# this is a label that will be created
myLabel1 = Label(root, text = "sup").grid(row=0, column=0)
myLabel2 = Label(root, text = "sup everybody").grid(row=1, column=0)
# this puts label on the screan
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=0)
#this puts my screan up
root.mainloop()
