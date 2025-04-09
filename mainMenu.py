#libraries
from tkinter import *
from tkinter import font as tkFont

def show_login():
    #main window
    main = Tk()
    main.title("Login")

    width = str(int(main.winfo_screenwidth()/2)-150)
    height = str(int(main.winfo_screenheight()/2)-300)
    main.geometry("400x500+"+width+'+'+height)

    bfont = tkFont.Font(family='Helvetica', size=16, weight=tkFont.BOLD)
    wfont = tkFont.Font(family='Helvetica', size=22, weight=tkFont.BOLD)

    welcome = Label(main, text="Welcome!", font=wfont)
    welcome.place(x=130, y=30)

    pls = Label(main, text="Please enter your", font=wfont)
    pls.place(x=80, y=80)
    pls2 = Label(main, text="username and password", font=wfont)
    pls2.place(x=30, y=120)

    username = Label(main, text="Username", font=bfont)
    username.place(x=150, y=190)
    username_input = Entry(width=30)
    username_input.place(x=110, y=250)

    password = Label(main, text="Password", font=bfont)
    password.place(x=150, y=290)
    password_input = Entry(width=30)
    password_input.place(x=110, y=350)

    #button to get rid of window
    def login():
        main.destroy()
        import todolist
        todolist.show_todolist()

    login_button = Button(main, text="Login", command=login)
    login_button.place(x=175, y=400)

    main.mainloop()