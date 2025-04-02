#libraries
from tkinter import *
from tkinter import font as tkFont
from tkinter import ttk
import sqlite3
import mainMenu

#creating the connector to database
dataConnector = sqlite3.connect('todolist.db')

#createing a cursor
cursor = dataConnector.cursor()

#app window creation
root = Tk()
root.title('To Do List')

#centering the window
width = str(int(root.winfo_screenwidth()/2)-450)
height = str(int(root.winfo_screenheight()/2)-300)
root.geometry("900x600+"+width+'+'+height)

mainMenu

bfont = tkFont.Font(family='Helvetica', size=16, weight=tkFont.BOLD)

#functions
def new_task():
    def popup_destroy():
        top.destroy()
    top = Tk()
    width = str(int(root.winfo_screenwidth()/2)-150)
    height = str(int(root.winfo_screenheight()/2)-300)
    top.geometry("350x450+"+width+'+'+height)
    top.title("New Task")
    close_button = Button(top, text="Done", command=popup_destroy)
    close_button.place(x=150, y=400,width=40, height=30)


def completed_tasks():
    cursor.execute('select * from to_do_list')
    whattodo = cursor.fetchall()

    show_work = ''
    for work in whattodo:
        show_work += str(work) + "\n"

    query_label.insert('1.0', show_work)
    print("click")

def edit_task():
    def popup_destroy():
        top.destroy()
    top = Tk()
    width = str(int(root.winfo_screenwidth()/2)-150)
    height = str(int(root.winfo_screenheight()/2)-300)
    top.geometry("350x450+"+width+'+'+height)
    top.title("Edit Task")
    close_button = Button(top, text="Done", command=popup_destroy)
    close_button.place(x=150, y=400,width=40, height=30)

def delete_task():
    def popup_destroy():
        top.destroy()
    top = Tk()
    width = str(int(root.winfo_screenwidth()/2)-150)
    height = str(int(root.winfo_screenheight()/2)-300)
    top.geometry("350x450+"+width+'+'+height)
    top.title("Delete Task")
    close_button = Button(top, text="Done", command=popup_destroy)
    close_button.place(x=150, y=400,width=40, height=30)

def main_menu():
    pass

# Label to display the query results
query_label = Text(root, height=25, width=107)
query_label.grid(row=0, column=0, padx=20, pady=20)

# Buttons
new_task_button = Button(root, text="New Task", command=new_task, font=bfont)
new_task_button.place(x=20, y=450, width=200, height=60)

completed_tasks_button = Button(root, text="Completed Tasks", command=completed_tasks, font=bfont)
completed_tasks_button.place(x=240, y=450, width=200, height=60)

edit_task_button = Button(root, text="Edit Task", command=edit_task, font=bfont)
edit_task_button.place(x=460, y=450, width=200, height=60)

delete_task_button = Button(root, text="Delete Task", command=delete_task, font=bfont)
delete_task_button.place(x=680, y=450, width=200, height=60)

main_menu_button = Button(root, text="Main Menu", command=main_menu, font=bfont)
main_menu_button.place(x=20, y=520, width=200, height=60)


#run it up Blud
root.mainloop()