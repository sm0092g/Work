import tkinter as tk
from tkinter import font
from tkinter import *
from tkinter.ttk import *
import sqlite3

def main_screen():
    global root
    width, height = 500, 400
    root.geometry('%dx%d+0+0' % (width, height))

#This function checks for the details within the database and cross references it with the entries to check if the entries that the user inputted are within the database, if the entry exists then it moves the admin to the product list where he can add, remove or edit the toys
def data_check():
    conn = sqlite3.connect("Customer_Info.db")
    #Create cursor
    cursor = conn.cursor()
    adminun_input = str(cursor.execute('SELECT admin_un FROM AdminTbl WHERE admin_un=?', (a_adminun.get(),),).fetchall())
    adminp_input = str(cursor.execute('SELECT admin_p FROM AdminTbl WHERE admin_p=?', (a_adminp.get(),),).fetchall())
    adminun_data = a_adminun.get()
    adminp_data = a_adminp.get()

    if not adminun_data in adminun_input or not adminp_data in adminp_input:
        print("Not an admin.")
    elif adminun_data in adminun_input or adminp_data in adminp_input:
        print("welcome")
    else:
        print("broke")
    #commit information to the database
    conn.commit()
    #close the connection
    conn.close()
 
root = tk.Tk()
root.title("Admin Login Screen")
root.configure(bg="gray94")
root.iconbitmap("C:/Users/rayni")
admin_ul = Label(root,text="Admin Username: ").grid(row=0, column=0, sticky=N, pady=5)
a_adminun = Entry(root,text="Enter ID")
a_adminun.grid(row=1, column=0, sticky=N, pady=5)
admin_ul2 = Label(root,text="Admin password: ").grid(row=2, column=0, sticky=N, pady=5)
a_adminp = Entry(root,text="Enter password", show="*")
a_adminp.grid(row=3, column=0, sticky=N, pady=5)
btn_login = Button(root, text="login", command= data_check).grid(row=4, column=0, sticky=N, pady=5)
main_screen()
#maximise_window()
data_check()
#center_window()
root.mainloop()