import sqlite3
from tkinter import *
from tkinter import messagebox, ttk


def feed():
    window = Tk()
    window.geometry('600x700+750+100')
    window.title("Feedback")
    window.config(bg='pink')

    def create():
        conn = sqlite3.connect('database.db', timeout=10)
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS users(id integer primary key autoincrement, name TEXT, email TEXT, "
                  "message TEXT, sqltime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)")
        conn.commit()
        conn.close()

    create()

    labelheading = Label(window, text="We Want Your Feedback", bg='pink',  font=('Arial Black', 24))
    labelheading.place(x=70, y=20)

        #NAME#
    labelname = Label(window, text="Name", bg='light blue', font=('Times-new-roman', 16))
    name_entry = StringVar()
    name_entry = ttk.Entry(window, width=40, font=('calibri', 16), textvariable=name_entry)
    labelname.place(x=20,y=100)
    name_entry.place(x=120, y=100)

        #Email#
    Labelemail = Label(window, text="Email ID", bg='light blue', font=('arial', 16))
    email_entry = StringVar()
    email_entry = ttk.Entry(window, width=40, font=('calibri', 16), textvariable=email_entry)
    Labelemail.place(x=20, y=140)
    email_entry.place(x=120, y=140)

        #Message#
    Labelmsg = Label(window, text="Comment", bg='light blue', font=('arial', 16))
    msg_entry = StringVar()
    msg_entry = ttk.Entry(window, width=40, font=('calibri', 16), textvariable=msg_entry)
    Labelmsg.place(x=20, y=180)
    msg_entry.place(x=120, y=180)


    war = Label(window, text="Fill every details", bg='red', fg='black', font=('arial', 16))

######################--------Button to save data into database------------######################

    def saveData():
        if(len(name_entry.get()) == 0 or len(email_entry.get()) == 0 or len(msg_entry.get()) == 0):
            war.place(x=230, y=230)
            print("Enter data")

        else:
            war.place_forget()
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            c.execute('INSERT INTO users(name,email,message) VALUES(?,?,?)',
                      (name_entry.get(), email_entry.get(), msg_entry.get()))
            conn.commit()
            print("Data Saved")
            #"1.0", 'end-1c'
    buttonsv = ttk.Button(window, width=20, text="Submit", command=saveData)
    buttonsv.place(x=250,y=270)

