import tkinter
import tkinter as tk
from tkinter import *
import mysql.connector
from sqlalchemy import create_engine
from mysql.connector import Error
from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

global i


#Create the window
root = Tk()
#create window title and where window spawns
root.geometry('+%d+%d'%(450,50))
root.title("SSUK DATABASE")
#create size and width of window and how many colums window has
canvas = tk.Canvas(root, width = 300, height = 300)
canvas.grid(columnspan= 5, rowspan= 6)

#Logo

logo = Image.open("BTS.jpg")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions

instructions = tk.Label(root, text="Press the bellow button to connect to SSUK DataBase")
instructions.grid(columnspan=3, column=0, row=1)

#Connection Button
browse_text = tk.StringVar()
#The below command is what runs the function and makes the button work
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:[retrieve_input(), database(username)], bg='red', fg='blue', height=2, width=15)
browse_text.set("Connect")
browse_btn.grid(column=1, row=2)


#Exit window button
exitButton = tk.Button(root, text="QUIT", command=root.destroy)
exitButton.grid(column=1, row=10)


#Username enter box
textBox = Text(root, height=2, width=15)
textBox.grid(column=1, row=4)

#Password enter box
passwordTextBox = Text(root, height=2, width=15)
passwordTextBox.grid(column=1, row=6)

#Username Instructions
usernameInstructions = tk.Label(root, text="Enter Username")
usernameInstructions.grid(columnspan=1, column=1, row=3)

#Password Instructions
passwordInstructions = tk.Label(root, text="Enter password")
passwordInstructions.grid(column=1, row=5)


root.mainloop()