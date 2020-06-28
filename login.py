from tkinter import *
from tkinter import messagebox
import pickle


def login():
    # when clicked, check it correct or wrong
    # if it is correct, it pops up login message
    # if it is wrong, it pops up error message
    pass
def createAccount():
    global username, password, createAccount_screen
    username = StringVar()
    password = StringVar()
    createAccount_screen = Toplevel(main_screen)
    # focus on createAccount window
    createAccount_screen.focus_set()
    # do not accept any events from another windows.
    createAccount_screen.grab_set()
    createAccount_screen.resizable(width=False, height=False)
    createAccount_screen.title("Create Account")
    createAccount_screen.geometry("300x250")
    Label(createAccount_screen, text="Create your account").pack()
    Label(createAccount_screen, text="ID").pack()
    Entry(createAccount_screen, textvariable=username).pack()
    Label(createAccount_screen, text="PW").pack()
    Entry(createAccount_screen, textvariable=password).pack()
    Button(createAccount_screen, text="Create !", width=20, height=2, command=create_user).pack()

def create_user():
    status = True  # check duplication
    info_file = open("info.pickle", "rb")
    user_info = pickle.load(info_file)  # load data in info_file to user_info
    for id in user_info.keys():
        if username.get() == id:
            messagebox.showerror("Error", "Duplicated")
            status = False
    if status == True:
        user_info[username.get()] = password.get()
        info_file.close()
        msgbox = messagebox.askquestion("Conform", "Do you really create an account?")
        if msgbox == "yes":
            info_file = open("info.pickle", "wb")  # "wb" write binary
            pickle.dump(user_info, info_file)  # save user_info to info_file
            info_file.close()
            messagebox.showinfo("Notification", "You create an account")
            createAccount_screen.destroy()


def main():
    global main_screen
    main_screen = Tk()
    main_screen.title("Login Program")
    main_screen.geometry("300x250")
    # create label widgets
    id_label = Label(main_screen, text="ID")
    pw_label = Label(main_screen, text="PW")
    # create input boxes
    id_box = Entry(main_screen)
    pw_box = Entry(main_screen)
    # default value of boxes
    id_box.insert(0, "Enter your accocunt")
    pw_box.insert(0, "*******************")
    # create button objects
    loginbtn = Button(main_screen, text="Sign in", width=30, height=2, command=login)
    createbtn = Button(main_screen, text="Create new account", width=30, height=2, command=createAccount)
    # display components
    id_label.pack()
    pw_label.pack()
    id_box.pack()
    pw_box.pack()
    loginbtn.pack()
    createbtn.pack()


main()
main_screen.mainloop()