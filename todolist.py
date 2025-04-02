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
# Function to add a new task
def new_task():
    def popup_destroy():
        top.destroy()

    def submit_task():
        # Get the values from the input fields
        name = name_entry.get()
        due_date = due_date_entry.get()
        description = description_entry.get()
        status = status_entry.get()
        people_involved = people_entry.get()

        # Check if any of the fields are empty
        if not name or not due_date or not description or not status or not people_involved:
            # If any field is empty, show an error message in red
            success_label.config(text="Please fill in all fields!", fg="red")
        else:
            # SQL query to insert new task into the database
            cursor.execute('''
                    INSERT INTO to_do_list (name, due_date, description, status, people_involved)
                    VALUES (?, ?, ?, ?, ?)
                ''', (name, due_date, description, status, people_involved))

            # Commit the changes and save the data
            dataConnector.commit()

            # Show a message indicating that the task was added
            success_label.config(text="Task added successfully!", fg="green")

            # Clears the fields after submitting
            name_entry.delete(0, END)
            due_date_entry.delete(0, END)
            description_entry.delete(0, END)
            status_entry.delete(0, END)
            people_entry.delete(0, END)

    # Create a new top-level window for entering the task details
    top = Tk()
    width = str(int(root.winfo_screenwidth() / 2) - 150)
    height = str(int(root.winfo_screenheight() / 2) - 300)
    top.geometry("350x450+" + width + '+' + height)
    top.title("New Task")

    # Labels and Entry fields for task details
    name_label = Label(top, text="Task Name:")
    name_label.place(x=20, y=30)
    name_entry = Entry(top, width=30)
    name_entry.place(x=120, y=30)

    due_date_label = Label(top, text="Due Date:")
    due_date_label.place(x=20, y=80)
    due_date_entry = Entry(top, width=30)
    due_date_entry.place(x=120, y=80)

    description_label = Label(top, text="Description:")
    description_label.place(x=20, y=130)
    description_entry = Entry(top, width=30)
    description_entry.place(x=120, y=130)

    status_label = Label(top, text="Status:")
    status_label.place(x=20, y=180)
    status_entry = Entry(top, width=30)
    status_entry.place(x=120, y=180)

    people_label = Label(top, text="People Involved:")
    people_label.place(x=20, y=230)
    people_entry = Entry(top, width=30)
    people_entry.place(x=120, y=230)

    # Success message label
    success_label = Label(top, text="", fg="green")
    success_label.place(x=110, y=320)

    # Submit button to save the task into the database
    submit_button = Button(top, text="Add Task", command=submit_task)
    submit_button.place(x=120, y=350, width=100, height=30)

    # Close button to close the popup window
    close_button = Button(top, text="Done", command=popup_destroy)
    close_button.place(x=150, y=400, width=40, height=30)




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