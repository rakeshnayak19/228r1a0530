from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import ImageTk
def saveData():
    if (usernameEntry.get == '' or emailEntry.get() == '' or passwordEntry.get() == ''):
        messagebox.showerror('Error', "all fields are mandatory")
    else:
       try:
           conn=mysql.connector.connect(host="localhost", user="root", password="12345", database="customerdata")
           mycur = conn.cursor()
           sql = 'insert into studentreg(username,email,password)values(%s,%s ,%s)'
           mycur.execute(sql, (usernameEntry.get(), passwordEntry.get(), emailEntry.get()))
           conn.commit()
       except :
           messagebox.showerror('error','problem in database')

window = Tk()
window.title("hhh")
window.geometry('925x500+300+200')

background =ImageTk.PhotoImage(file='download.jpeg')
blabel=Label(window,image=background)
blabel.grid()

# Add widgets and set up your GUI here
frame = Frame(window)
frame.place(x=600,y=100)

# Create a label widget and place it in the frame using grid geometry manager
usernameLabel = Label(frame, text="Username",font=('Arial',15,'bold'), bg='black', fg='white')
usernameLabel.grid(row=0, column=0)
usernameEntry = Entry(frame, width=30)
usernameEntry.grid(row=0, column=1)


emailLabel = Label(frame,text="Email",font=('Arial',15,'bold'),bg='black',fg='white')
emailLabel.grid(row=2, column=0)
emailEntry = Entry(frame, width=30)
emailEntry.grid(row=2, column=1)
passwordLabel = Label(frame, text="Password",font=('Arial',15,'bold'),bg='black',fg='white')
passwordLabel.grid(row=1, column=0)
passwordEntry = Entry(frame,width=30)
passwordEntry.grid(row=1,column=1)


button=Button(frame,text="submit" ,command=saveData)
button.grid(row=4, column=1)
window.mainloop()