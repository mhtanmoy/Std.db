from tkinter import *
import tkinter as tk
import psycopg2

root = Tk()

def srch_id(s_id):
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="442244",host="localhost",port="5432")
    cur = conn.cursor()
    query = '''SELECT * FROM studentdb WHERE id=%s'''
    cur.execute(query,(s_id))
    row = cur.fetchone()
    dis_srch(row)
    conn.commit()
    conn.close()

def get_data(name,age,ad):
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="442244",host="localhost",port="5432")
    cur = conn.cursor()
    query = '''INSERT INTO studentdb (Name, age, Address) VALUES (%s,%s,%s);'''
    cur.execute(query,(name,age,ad))
    print('Database Included')
    conn.commit()
    conn.close()
    dis_all()

def dis_srch(row):
    listbox = Listbox(frame,width=20,height=1)
    listbox.grid(row=9,column=1)
    listbox.insert(END,row)

def dis_all():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="442244",host="localhost",port="5432")
    cur = conn.cursor()
    query = '''SELECT * FROM studentdb;'''
    cur.execute(query)
    row = cur.fetchall()
    listbox = Listbox(frame,width=20,height=8)
    listbox.grid(row=10,column=1)
    for x in row:
        listbox.insert(END,x)

canvas = Canvas(root, height=480,width=900)
canvas.pack()

frame = Frame()
frame.place(relx=0.3, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame,text="Add Data")
label.grid(row=0,column=1)

label = Label(frame,text="Name: ")
label.grid(row=1,column=0)
entry_name = Entry(frame)
entry_name.grid(row=1,column=1)

label = Label(frame,text="Age: ")
label.grid(row=2,column=0)
entry_age = Entry(frame)
entry_age.grid(row=2,column=1)

label = Label(frame,text="Address: ")
label.grid(row=3,column=0)
entry_ad = Entry(frame)
entry_ad.grid(row=3,column=1)

button = Button(frame,text="Submit", command= lambda:get_data(entry_name.get(),entry_age.get(),entry_ad.get()))
button.grid(row=4,column=1)

label = Label(frame,text="Search Data")
label.grid(row=5,column=1)

label = Label(frame,text="Search By ID: ")
label.grid(row=6,column=0)
entry_srch = Entry(frame)
entry_srch.grid(row=6,column=1)
button = Button(frame,text="Search", command= lambda: srch_id(entry_srch.get()))
button.grid(row=6,column=2)

dis_all()
root.mainloop()