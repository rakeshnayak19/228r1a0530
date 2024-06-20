from tkinter import *
from PIL import ImageTk



window =Tk()
window.title("sign in")
window.geometry('925x500+300+200')

background =ImageTk.PhotoImage(file='mANOGG.jpg')
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
passwordLabel = Label(frame, text="Password",font=('Arial',15,'bold'),bg='black',fg='white')
passwordLabel.grid(row=1, column=0)
passwordEntry = Entry(frame,width=30)
passwordEntry.grid(row=1,column=1)


button=Button(frame,text="submit" )
button.grid(row=4, column=1)
window.mainloop()