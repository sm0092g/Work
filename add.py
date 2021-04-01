import tkinter as tk
from tkinter import font
from tkinter import *
from tkinter.ttk import *
import sqlite3
#Create a database and connect to it
conn = sqlite3.connect("Customer_Info.db")
#Create cursor
cursor = conn.cursor()


class the_GUI:
    def add_to_category(self):
        #Create a database and connect to it
        conn = sqlite3.connect("Customer_Info.db")
        #Create cursor
        cursor = conn.cursor()

        #This code allows the admin to insert toys into the products list
        cursor.execute('INSERT INTO ProductTbl2 VALUES (:a,:b,:c)', {
        
            'a':self.toy.get(), 'b':self.category.get(), 'c':self.stock.get()
            })
        #commit information to the database
        conn.commit()
        #close the connection
        conn.close()

    def __init__(self, root):
        self.root = root
        root = tk.Tk()
        root.title("Add to category")
        root.geometry("500x400")
        
        self.toy_l = Label(root,text="The toy: ").grid(row=0, column=0, sticky = W, pady = 10)
        self.toy =Entry(root,text="")
        self.toy.grid(row=0, column=1, sticky = N, pady = 10)
        self.category_l = Label(root,text="It's category: ").grid(row=1, column=0, sticky = W, pady = 10)
        self.category = Entry(root,text="")
        self.category.grid(row=1, column=1, sticky = W, pady = 10)
        self.stock_l = Label(root, text="Stock Level: ").grid(row=2, column=0, sticky= W, pady = 10)
        self.stock = Entry(root, text="")
        self.stock.grid(row=2, column=1, sticky= W, pady = 10)
        self.btn_add = Button(root, text="Add", command= self.add_to_category).grid(row=3, column=1, sticky = W, pady = 10)



root = tk.Tk()

gui = the_GUI(root)
gui.add_to_category()
root.mainloop()
def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('Customer_Info.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from ProductTbl"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("Toy: ", row[0]) 
            print("Category: ", row[1])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

readSqliteTable()
