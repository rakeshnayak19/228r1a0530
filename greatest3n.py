from tkinter import *
from tkinter import messagebox
def g2():
    try:
        n1=int(a.get())
        n2=int(b.get())
        n3=int(c.get())
        if(n1>n2 and n1>n3):
            d.insert(0,str(n1))
        if (n2>n1 and n2>n3):
            d .insert(0, str(n2))
        else:
            d.insert(0,str(n3))
    except:
        messagebox.showerror("error")
window=Tk()
window.title(">2")
frame=Frame(window)
frame.place(x=100,y=100)
aLabel=Label(frame,text="num1")
aLabel.grid(row=0,column=0)
a=Entry(frame,width=30)
a.grid(row=0,column=1)

bLabel=Label(frame,text="num2")
bLabel.grid(row=1,column=0)
b=Entry(frame,width=30)
b.grid(row=1,column=1)
cLabel=Label(frame,text="num3")
cLabel.grid(row=2,column=0)
c=Entry(frame,width=30)
c.grid(row=2,column=1)
dLabel=Label(frame,text="greatest")
dLabel.grid(row=3,column=0)
d=Entry(frame,width=30)
d.grid(row=3,column=1)
button=Button(frame,text="greatest",command=g2)
button.grid(row=4,column=1)

window.mainloop()


