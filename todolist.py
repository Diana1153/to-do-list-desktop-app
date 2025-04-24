#libraries
from tkinter import *
from tkinter import font as tkFont
from tkinter import ttk
import tkinter as tk
import sqlite3
import mainMenu

def show_todolist_admin():
    #creating the connector to database
    dataConnector = sqlite3.connect('todolist.db')

    #createing a cursor
    cursor = dataConnector.cursor()


    #app window creation
    root = Tk()
    root.title('To Do List - Admin')


    #centering the window
    width = str(int(root.winfo_screenwidth()/2)-450)
    height = str(int(root.winfo_screenheight()/2)-300)
    root.geometry("900x600+"+width+'+'+height)

    mainMenu

    # Fonts
    bfont = tkFont.Font(family='OpenSymbol', size=16, weight=tkFont.BOLD)

    def rerendertable():
        # Clear the Treeview first
        for item in query_label.get_children():
            query_label.delete(item)

        # Then fetch and re-insert fresh data
        cursor.execute('SELECT * FROM to_do_list')
        rows = cursor.fetchall()
        for row in rows:
            query_label.insert("", tk.END, values=row)
        print("Table rerendered")



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

                rerendertable()

        # Create a new top-level window for entering the task details
        top = Tk()
        width = str(int(root.winfo_screenwidth() / 2) - 150)
        height = str(int(root.winfo_screenheight() / 2) - 300)
        top.geometry("350x380+" + width + '+' + height)
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
        success_label.place(x=110, y=260)

        # Submit button to save the task into the database
        submit_button = Button(top, text="Add Task", command=submit_task)
        submit_button.place(x=120, y=290, width=100, height=30)

        # Close button to close the popup window
        close_button = Button(top, text="Done", command=popup_destroy)
        close_button.place(x=150, y=330, width=40, height=30)

    def completed_tasks():
        # Clear previous Treeview rows
        for item in query_label.get_children():
            query_label.delete(item)

        # Fetch only completed tasks
        cursor.execute("SELECT * FROM to_do_list WHERE status = '10/10'")
        rows = cursor.fetchall()

        # Insert the completed tasks into the Treeview
        for row in rows:
            query_label.insert("", tk.END, values=row)

        print("Completed tasks rendered")

    def edit_task():
        def popup_destroy():
            top.destroy()

        def update_task():
            task_id = id_entry.get()
            name = name_entry.get()
            due_date = due_date_entry.get()
            description = description_entry.get()
            status = status_entry.get()
            people = people_entry.get()

            if not task_id:
                # Display an error message if the task ID is empty
                error_label.config(text="Please fill in the ID you wish to delete", fg="red")
            else: 
                if name and due_date and description and status and people: 
                    # Execute query
                    cursor.execute('''update to_do_list 
                                   set name = ?, due_date = ?, description = ?, status = ?, people_involved = ?
                                   where id = ?''',
                                   [name, due_date, description, status, people, task_id])
                    # Commit the changes and save the data
                    dataConnector.commit()

                    # Show a message indicating that the task was added
                    success_label.config(text="Task Edited successfully!", fg="green")
                    error_label.config(text="")

                    # Clears the fields after submitting
                    id_entry.delete(0, END)
                    name_entry.delete(0, END)
                    due_date_entry.delete(0,END)
                    description_entry.delete(0, END)
                    status_entry.delete(0, END)
                    people_entry.delete(0, END)

                    rerendertable()

                elif name and due_date and description and status: 
                    # Execute query
                    cursor.execute('''UPDATE to_do_list 
                                   SET name = ?, due_date = ?, description = ?, status = ?
                                   WHERE id = ?''',
                                   [name, due_date, description, status, task_id])
                    # Commit the changes and save the data
                    dataConnector.commit()

                    # Show a message indicating that the task was added
                    success_label.config(text="Task Edited successfully!", fg="green")
                    error_label.config(text="")

                    # Clears the fields after submitting
                    id_entry.delete(0, END)
                    name_entry.delete(0, END)
                    due_date_entry.delete(0,END)
                    description_entry.delete(0, END)
                    status_entry.delete(0, END)

                    rerendertable()

                elif name and due_date and description:
                    # Execute query
                    cursor.execute('''UPDATE to_do_list 
                                   SET name = ?, due_date = ?, description = ?
                                   WHERE id = ?''',
                                   [name, due_date, description, task_id])
                    # Commit the changes and save the data
                    dataConnector.commit()

                    # Show a message indicating that the task was added
                    success_label.config(text="Task Edited successfully!", fg="green")
                    error_label.config(text="")

                    # Clears the fields after submitting
                    id_entry.delete(0, END)
                    name_entry.delete(0, END)
                    due_date_entry.delete(0,END)
                    description_entry.delete(0, END)

                    rerendertable()

                elif name and due_date:
                    # Execute query
                    cursor.execute('''UPDATE to_do_list 
                                   SET name = ?, due_date = ?
                                   WHERE id = ?''',
                                   [name, due_date, task_id])
                    # Commit the changes and save the data
                    dataConnector.commit()

                    # Show a message indicating that the task was added
                    success_label.config(text="Task Edited successfully!", fg="green")
                    error_label.config(text="")

                    # Clears the fields after submitting
                    id_entry.delete(0, END)
                    name_entry.delete(0, END)
                    due_date_entry.delete(0,END)

                    rerendertable()

                elif task_id and name:
                    # Execute query
                    cursor.execute('''UPDATE to_do_list 
                                   SET name = ? 
                                   WHERE id = ?''', [name, task_id])
                    # Commit the changes and save the data
                    dataConnector.commit()

                    # Show a message indicating that the task was added
                    success_label.config(text="Task Edited successfully!", fg="green")
                    error_label.config(text="")

                    # Clears the fields after submitting
                    id_entry.delete(0, END)
                    name_entry.delete(0, END)

                    rerendertable()

        # Window display
        top = Tk()
        width = str(int(root.winfo_screenwidth() / 2) - 150)
        height = str(int(root.winfo_screenheight() / 2) - 300)
        top.geometry("350x400+" + width + '+' + height)
        top.title("Edit Task")

        # Labels and Entry fields for task details
        id_label = Label(top, text="Task ID:")
        id_label.place(x=20, y= 30)
        id_entry = Entry(top, width=30)
        id_entry.place(x=120, y=30)

        name_label = Label(top, text="Task Name:")
        name_label.place(x=20, y=80)
        name_entry = Entry(top, width=30)
        name_entry.place(x=120, y=80)

        due_date_label = Label(top, text="Due Date:")
        due_date_label.place(x=20, y=130)
        due_date_entry = Entry(top, width=30)
        due_date_entry.place(x=120, y=130)

        description_label = Label(top, text="Description:")
        description_label.place(x=20, y=180)
        description_entry = Entry(top, width=30)
        description_entry.place(x=120, y=180)

        status_label = Label(top, text="Status:")
        status_label.place(x=20, y=230)
        status_entry = Entry(top, width=30)
        status_entry.place(x=120, y=230)

        people_label = Label(top, text="People Involved:")
        people_label.place(x=20, y=280)
        people_entry = Entry(top, width=30)
        people_entry.place(x=120, y=280)

        # Success message label
        success_label = Label(top, text="", fg="green")
        success_label.place(x=105, y=300)

        # Error message label
        error_label = Label(top, text="", fg="red")
        error_label.place(x=75, y=300)

        no_id_label = Label(top, text="", fg="red")
        no_id_label.place(x=75, y=300)

        # delete button to save the task into the database
        update_button = Button(top, text="Update Task", command=update_task)
        update_button.place(x=120, y=320, width=100, height=30)

        close_button = Button(top, text="Done", command=popup_destroy)
        close_button.place(x=150, y=360,width=40, height=30)

    def delete_task():
        def popup_destroy():
            top.destroy()

        def delete_taskid():
            delete = delete_entry.get()

            if not delete:
                # Display an error message if the task ID is empty
                error_label.config(text="Please fill in the ID you wish to delete", fg="red")
                success_label.config(text="")  # Hide success label
            else:
                # SQL query to insert new task into the database
                cursor.execute('''DELETE FROM to_do_list where id = ?''', [delete])

                # Commit the changes and save the data
                dataConnector.commit()

                # Show a message indicating that the task was added
                success_label.config(text="Task Deleted successfully!", fg="green")
                error_label.config(text="")

                # Clears the fields after submitting
                delete_entry.delete(0, END)

                rerendertable()

        top = Tk()
        width = str(int(root.winfo_screenwidth()/2)-150)
        height = str(int(root.winfo_screenheight()/2)-300)
        top.geometry("350x200+"+width+'+'+height)
        top.title("Delete Task")

        #Delete Message Label & Entry
        delete_label = Label(top, text="Please enter the ID you wish to delete")
        delete_label.place(x=60, y=10)
        delete_entry = Entry(top, width=30)
        delete_entry.place(x=90, y=40)

        # Success message label
        success_label = Label(top, text="", fg="green")
        success_label.place(x=100, y=75)

        # Error message label
        error_label = Label(top, text="", fg="red")
        error_label.place(x=75, y=75)

        # delete button to save the task into the database
        delete_button = Button(top, text="Delete Task", command=delete_taskid)
        delete_button.place(x=120, y=100, width=100, height=30)

        # Close button to close the popup window
        close_button = Button(top, text="Done", command=popup_destroy)
        close_button.place(x=150, y=150,width=40, height=30)

    def main_menu():
        root.destroy()
        import mainMenu
        mainMenu.show_login()

    def refreshtable():
        rerendertable()
        
    # Label to display the query results
    query_label = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings')
    query_label.column("#1", anchor=tk.NW, width=15)
    query_label.heading("#1", text="ID", anchor=tk.CENTER)
    query_label.column("#2", anchor=tk.NW)
    query_label.heading("#2", text="Task Name")
    query_label.column("#3", anchor=tk.NW, width=60)
    query_label.heading("#3", text="Due Date")
    query_label.column("#4", anchor=tk.NW)
    query_label.heading("#4", text="Description")
    query_label.column("#5", anchor=tk.NW, width=40)
    query_label.heading("#5", text="Status")
    query_label.column("#6", anchor=tk.NW)
    query_label.heading("#6", text="People")
    query_label.place(x=20, y=20, width=850, height=400)

    # Buttons
    new_task_button = Button(root, text="New Task", command=new_task, font=bfont)
    new_task_button.place(x=20, y=450, width=200, height=60)

    completed_tasks_button = Button(root, text="Completed Tasks", command=completed_tasks, font=bfont)
    completed_tasks_button.place(x=240, y=450, width=200, height=60)

    edit_task_button = Button(root, text="Edit Task", command=edit_task, font=bfont)
    edit_task_button.place(x=460, y=450, width=200, height=60)

    delete_task_button = Button(root, text="Delete Task", command=delete_task, font=bfont)
    delete_task_button.place(x=680, y=450, width=200, height=60)

    main_menu_button = Button(root, text="Log-Out", command=main_menu, font=bfont)
    main_menu_button.place(x=680, y=520, width=200, height=60)

    refresh_button = Button(root, text="Refresh Tasks", command=refreshtable, font=bfont)
    refresh_button.place(x=20, y=520, width=200, height=60)

    # Call rerendertable() to populate the table on startup
    rerendertable()

    #run it up Blud
    root.mainloop()


def show_todolist_user():
    # creating the connector to database
    dataConnector = sqlite3.connect('todolist.db')

    # createing a cursor
    cursor = dataConnector.cursor()

    # app window creation
    root = Tk()
    root.title('To Do List - User')

    # centering the window
    width = str(int(root.winfo_screenwidth() / 2) - 450)
    height = str(int(root.winfo_screenheight() / 2) - 300)
    root.geometry("900x600+" + width + '+' + height)

    # Fonts
    bfont = tkFont.Font(family='OpenSymbol', size=16, weight=tkFont.BOLD)

    def rerendertable():
        # Clear the Treeview first
        for item in query_label.get_children():
            query_label.delete(item)

        # Then fetch and re-insert fresh data
        cursor.execute('SELECT * FROM to_do_list')
        rows = cursor.fetchall()
        for row in rows:
            query_label.insert("", tk.END, values=row)
        print("Table rerendered")

    # functions
    # Function to add a new task

    def edit_task():
        def popup_destroy():
            top.destroy()

        def update_task():
            task_id = Update_entry.get()  # Get task ID
            update = status_entry.get()  # Get new status value

            if not update or not task_id:
                # Display an error message if the task ID is empty
                error_label.config(text="Please fill in the ID you wish to delete", fg="red")
                success_label.config(text="")  # Hide success label
            else:
                # SQL query to insert new task into the database
                cursor.execute('''update to_do_list set status = ? where id = ? ''', [update, task_id])

                # Commit the changes and save the data
                dataConnector.commit()

                # Show a message indicating that the task was added
                success_label.config(text="Task Edited successfully!", fg="green")
                error_label.config(text="")

                # Clears the fields after submitting
                Update_entry.delete(0, END)
                status_entry.delete(0, END)

                rerendertable()

        top = Tk()
        width = str(int(root.winfo_screenwidth() / 2) - 150)
        height = str(int(root.winfo_screenheight() / 2) - 300)
        top.geometry("350x250+" + width + '+' + height)
        top.title("Edit Task")

        # Delete Message Label & Entry
        Update_label = Label(top, text="Please enter the ID you wish to edit")
        Update_label.place(x=60, y=10)
        Update_entry = Entry(top, width=30)
        Update_entry.place(x=90, y=40)

        # Label and Entry for new Status
        status_label = Label(top, text="Enter new status EX: (#/10)")
        status_label.place(x=60, y=80)
        status_entry = Entry(top, width=30)
        status_entry.place(x=90, y=110)

        # Success message label
        success_label = Label(top, text="", fg="green")
        success_label.place(x=100, y=130)

        # Error message label
        error_label = Label(top, text="", fg="red")
        error_label.place(x=75, y=130)

        # delete button to save the task into the database
        update_button = Button(top, text="Update Task", command=update_task)
        update_button.place(x=120, y=160, width=100, height=30)

        close_button = Button(top, text="Done", command=popup_destroy)
        close_button.place(x=150, y=200, width=40, height=30)

    def main_menu():
        root.destroy()
        import mainMenu
        mainMenu.show_login()

    def refreshtable():
        rerendertable()

    # Label to display the query results
    query_label = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings')
    query_label.column("#1", anchor=tk.NW, width=15)
    query_label.heading("#1", text="ID", anchor=tk.CENTER)
    query_label.column("#2", anchor=tk.NW)
    query_label.heading("#2", text="Task Name")
    query_label.column("#3", anchor=tk.NW, width=60)
    query_label.heading("#3", text="Due Date")
    query_label.column("#4", anchor=tk.NW)
    query_label.heading("#4", text="Description")
    query_label.column("#5", anchor=tk.NW, width=40)
    query_label.heading("#5", text="Status")
    query_label.column("#6", anchor=tk.NW)
    query_label.heading("#6", text="People Involved")
    query_label.place(x=20, y=20, width=850, height=400)

    # Buttons
    edit_task_button = Button(root, text="Edit Status", command=edit_task, font=bfont)
    edit_task_button.place(x=240, y=450, width=200, height=60)

    main_menu_button = Button(root, text="Log-Out", command=main_menu, font=bfont)
    main_menu_button.place(x=680, y=520, width=200, height=60)

    refresh_button = Button(root, text="Refresh Tasks", command=refreshtable, font=bfont)
    refresh_button.place(x=20, y=450, width=200, height=60)

    # Call rerendertable() to populate the table on startup
    rerendertable()

    # run it up Blud
    root.mainloop()