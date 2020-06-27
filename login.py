from tkinter import *

root = Tk()

def login():
    pass

def createAccount():
    pass

# create input boxes
id_box = Entry(root)
pw_box = Entry(root)
# display boxes
id_box.pack()
pw_box.pack()
# default value of boxes
id_box.insert(0, "Enter your accocunt")
pw_box.insert(0, "*******************")
# create button objects
loginbtn = Button(root, text = "Sign in", padx = 50, pady = 20, command = login())
createbtn = Button(root, text = "Create new account", padx = 50, pady = 20, command = createAccount())
# display buttons
loginbtn.pack()
createbtn.pack()
root.mainloop()