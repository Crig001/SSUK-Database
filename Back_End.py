import tkinter
import tkinter as tk
from tkinter import *
import mysql.connector
from sqlalchemy import create_engine
from mysql.connector import Error
from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import collections.abc



global i

def database(username,password):
    try:
        #try to connect through mysqlconnector
        my_connect = mysql.connector.connect(host="10.0.0.4", user=username, passwd=password, database="SSUK")
        my_conn = my_connect.cursor()


    except:
        #error handling for wrong username or password
        from Front_End import instructions
        import Front_End
        instructions.destroy()
        err_instructions = tk.Label(Front_End.root, text="Please re-enter username and password", fg='red')
        err_instructions.grid(columnspan=3, column=0, row=1)


    if my_connect.is_connected():
        #create window
        my_w = tk.Tk()
        my_w.geometry("400x250")
        #create canvas
        data_canvas = tk.Canvas(my_w, bg='white', height=300, width=300)
        #log in through sqlalchemy
        log_on = "mysql+pymysql://" + username + ":" + password +"@10.0.0.4/SSUK"
        my_connection = create_engine(log_on)
        #select from the database all of the data
        my_cursor = my_connection.execute("SELECT * FROM personal limit 0,10")
        global i
        global j
        i = 0
        for personal in my_cursor:
            for j in range(len(personal)):
                e = Label(my_w, width=10, text=personal[j],
                          relief='ridge', anchor="w")
                e.grid(row=i, column=j)
                # e.insert(END, student[j])
            e = tk.Button(my_w, width=5, text='Edit', relief='ridge',
                          anchor="w", command=lambda k=personal[0]: edit_data(k))
            e.grid(row=i, column=j + 1)
            i = i + 1
        exitButton = tk.Button(my_w, text="QUIT", command=my_w.destroy)
        exitButton.grid(column=5, row=10)


    def edit_data(id):  # display to edit and update record
        global i  # start row after the last line of display
        # collect record based on id and present for updation.
        row = my_connection.execute("SELECT * FROM personal WHERE id=%s", id)
        s = row.fetchone()  # row details as tuple

        e1_str_id = tk.StringVar(my_w)  # String variable
        e2_str_name = tk.StringVar(my_w)
        e3_str_class = tk.StringVar(my_w)
        e4_str_mark = tk.StringVar(my_w)
        e5_str_gender = tk.StringVar(my_w)
        e6_str_test = tk.StringVar(my_w)

        e1_str_id.set(s[0])  # id is stored
        e2_str_name.set(s[1])  # Name is stored
        e3_str_class.set(s[2])  # class is stored
        e4_str_mark.set(s[3])  # mark is stored
        e5_str_gender.set(s[4])  # gender  is stored
        e6_str_test.set(s[5])   #test is stored new command CC

        e1 = tk.Entry(my_w, textvariable=e1_str_id, width=10, state='disabled')
        e1.grid(row=i, column=0)
        e2 = tk.Entry(my_w, textvariable=e2_str_name, width=10)
        e2.grid(row=i, column=1)
        e3 = tk.Entry(my_w, textvariable=e3_str_class, width=10)
        e3.grid(row=i, column=2)
        e4 = tk.Entry(my_w, textvariable=e4_str_mark, width=10)
        e4.grid(row=i, column=3)
        e5 = tk.Entry(my_w, textvariable=e5_str_gender, width=10)
        e5.grid(row=i, column=4)
        e6 = tk.Entry(my_w, textvariable=e6_str_test, width=10)
        e6.grid(row=i, column=5)
        b2 = tk.Button(my_w, text='Update', command=lambda: my_update(e2_str_name, e3_str_class, e4_str_mark, e5_str_gender, e6_str_test,e1_str_id,id),
                       relief='ridge', anchor="w", width=5)
        b2.grid(row=i, column=j + 1)



    def my_update(e2_str_name, e3_str_class, e4_str_mark, e5_str_gender, e6_str_test, e1_str_id,id):  # update record
        data = (e2_str_name.get(), e3_str_class.get(), e4_str_mark.get(), e5_str_gender.get(), e6_str_test.get(), e1_str_id.get())
        id = my_connection.execute("UPDATE personal SET FirstName=%s,LastName=%s,\
            PostalAddress=%s,PostalCity=%s,PostalCounty=%s WHERE id=%s", data)
        print("Row updated  = ", id.rowcount)
        for w in my_w.grid_slaves(i):  # remove the edit row
            w.grid_forget()
        update_in_win(my_w,edit_data,username,password)  # refresh the data

def update_in_win(my_w,edit_data,username,password):
    # log in through sqlalchemy
    log_on = "mysql+pymysql://" + username + ":" + password + "@10.0.0.4/SSUK"
    my_connection = create_engine(log_on)
    # select from the database all of the data
    my_cursor = my_connection.execute("SELECT * FROM personal limit 0,10")
    global i
    i = 0
    for personal in my_cursor:
        for j in range(len(personal)):
            e = Label(my_w, width=10, text=personal[j],
                      relief='ridge', anchor="w")
            e.grid(row=i, column=j)
            # e.insert(END, student[j])
        e = tk.Button(my_w, width=5, text='Edit', relief='ridge',
                      anchor="w", command=lambda k=personal[0]: edit_data(k))
        e.grid(row=i, column=j + 1)
        i = i + 1



