from tkinter import *
window=Tk()
window.geometry('250x100')
lbl1=Label(window,text="User Name")
lbl2=Label(window,text="Password")
lbl1.grid()
lbl2.grid()
txt1=Entry(window,width=10)
txt2=Entry(window,width=10)
txt1.grid(column=1,row=0)
txt2.grid(column=1,row=1)
btn1=Button(window,text='Submit')
btn2=Button(window,text='Reset')
btn1.grid(column=1,row=3)
btn2.grid(column=2,row=3)
window.mainloop()