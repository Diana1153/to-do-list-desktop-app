#libraries
from tkinter import *
import sqlite3

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

#functions
def query_todolist() :
    cursor.execute('select * from to_do_list')
    whattodo = cursor.fetchall()

    show_work = ''
    for work in whattodo:
        show_work += str(work) + "\n"

    query_label.insert('1.0', show_work)
    print("click")

# Label to display the query results
query_label = Text(root, height=20, width=107)
query_label.grid(row=0, column=0, padx=20, pady=20)

# Button to trigger the query function
query_button = Button(root, text="Show To-Do List", command=query_todolist)
query_button.grid(row=1, column=0, pady=10)

#run it up Blud
root.mainloop()