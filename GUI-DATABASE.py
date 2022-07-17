from cProfile import label
from tkinter import *
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = ""
)
mycursor = mydb.cursor()

window = Tk()
window.geometry("400x500")
window.title("GUI DBMS")

a = ""
column = []

def create_db():
    create_db.A = Toplevel(window)
    create_db.A.geometry("500x500")
    create_db.A.title("CREATE DATABASE")
    l2 = Label(create_db.A,text="Enter the name of database")
    l2.pack()
    create_db.e1 = Entry(create_db.A,width="15")
    create_db.e1.pack()
    b7 = Button(create_db.A,text="SUBMIT",width="20",command = create_db1)
    b7.pack()

def create_db1():
    x = str(create_db.e1.get())
    mycursor.execute(f"CREATE DATABASE {x}")
    l3 = Label(create_db.A,text="Database Created")
    l3.pack()
    create_db.e1.delete("0","end")

def select_db():
    select_db.B = Toplevel(window)
    select_db.B.geometry("500x500")
    select_db.B.title("SELECT THE DATABASE")
    select_db.click = StringVar()
    mycursor.execute("SHOW DATABASES")
    l = mycursor.fetchall()
    l = [i[0] for i in l]
    option = l
    drop = OptionMenu(select_db.B,select_db.click,*option)
    drop.pack()
    b1 = Button(select_db.B,text="CLICK ME",command=select_db1)
    b1.pack()

def select_db1():
    select_db1.x = select_db.click.get()
    l = Label(select_db.B ,text="DATABASE SELECTED")
    l.pack()

def create_table():
    create_table.C = Toplevel(window)
    create_table.C.geometry("500x500")
    create_table.C.title("CREATE THE TABLE")
    l1 = Label(create_table.C,text="Enter the table name")
    l1.pack()
    create_table.e1 = Entry(create_table.C,width="20")
    create_table.e1.pack()
  #  l2 = Label(create_table.C,text="Enter no. of columns in your table")
   # l2.pack()
    #create_table.e2 = Entry(create_table.C,width="20")
    #create_table.e2.pack()
    b1 = Button(create_table.C,text="SUBMIT",command=create_table1)
    b1.pack()

def create_table1():
    x = create_table.e1.get()
    mycursor.execute(f"USE {select_db1.x}")
    mycursor.execute(f"CREATE TABLE {x} (TEST VARCHAR(20))")
    l1 = Label(create_table.C,text="ENTER THE NAME OF COLUMN")
    l1.pack()
    create_table1.e1 = Entry(create_table.C,width="30")
    create_table1.e1.pack()
    b1 = Button(create_table.C,text="SUBMIT",command=create_table2)
    b1.pack()
    create_table.C.mainloop()


def create_table2():
    y = create_table.e1.get()
    x = create_table1.e1.get()
    mycursor.execute(f"ALTER TABLE {y} \nADD COLUMN {x} VARCHAR(20)")
    create_table1.e1.delete("0","end")


def insert_values():
    insert_values.D = Toplevel(window)
    insert_values.D.geometry("500x500")
    l1 = Label(insert_values.D,text="SELECT THE TABLE")
    l1.pack()
    insert_values.click = StringVar()
    mycursor.execute(f"USE {select_db1.x}")
    mycursor.execute("SHOW TABLES")
    l = mycursor.fetchall()
    l = [i[0] for i in l]
    option = l
    insert_values.drop = OptionMenu(insert_values.D,insert_values.click,*option)
    insert_values.drop.pack()
    b1 = Button(insert_values.D,text="SUBMIT",width="15",command= insert_values1)
    b1.pack()
    insert_values.D.mainloop()

def insert_values1():
    x = insert_values.click.get()
    y = select_db.click.get()
    mycursor.execute(f"SHOW COLUMNS FROM {x} FROM {y}")
    l = mycursor.fetchall()
    l = [i[0] for i in l]
    insert_values1.click = StringVar()
    insert_values1.drop = OptionMenu(insert_values.D,insert_values1.click,*l)
    insert_values1.drop.pack()
    l1 = Label(insert_values.D,text="Enter your values")
    l1.pack()
    insert_values1.e2 = Entry(insert_values.D,width="20")
    insert_values1.e2.pack()
    b1 = Button(insert_values.D,text = "SUBMIT",width="15",command=insert_values2)
    b1.pack()

def insert_values2():
    l = []
    x = insert_values1.e2.get()
    l.append(x)
    y = insert_values.click.get()
    a = select_db.click.get()
    z = insert_values1.click.get()
    sql = f"INSERT INTO {y} ({z}) VALUES (%s)"
    mycursor.execute(f"USE {a};")
    mycursor.execute(sql, l)
    mydb.commit()
    insert_values1.e2.delete("0","end")

def update():
    pass
    

    

def gap():
    l1 = Label(window,text="\n\n")
    l1.pack()

gap()
b1 = Button(window,text="CREATE DATABASE",width="20",command=create_db )
b1.pack()
gap()
b2 = Button(window,text="SELECT DATABASE",width="20",command = select_db)
b2.pack()
gap()
b3 = Button(window,text="CREATE THE TABLE",width="20",command = create_table)
b3.pack()
gap()
b4 = Button(window,text="INSERT VALUES TO TABLE",width="20",command=insert_values)
b4.pack()
gap()
b5 = Button(window,text="UPDATE",width="20")
b5.pack()
gap()
b6 = Button(window,text="DELETE",width="20")
b6.pack()



window.mainloop()