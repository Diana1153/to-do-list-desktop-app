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
width = str(int(root.winfo_screenwidth()/2)-450)
height = str(int(root.winfo_screenheight()/2)-300)
root.geometry("900x600+"+width+'+'+height)



#run it up Blud
root.mainloop()