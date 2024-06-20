from tkinter import *
from tkinter import messagebox
def g2():
    try:
        n1=int(a.get())
        n2=int(b.get())
        if(n1>n2):
            c.insert(0,str(n1))
        else:
            c.insert(0, str(n2))
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
cLabel=Label(frame,text="greatest")
cLabel.grid(row=2,column=0)
c=Entry(frame,width=30)
c.grid(row=2,column=1)
button=Button(frame,text="greatest",command=g2)
button.grid(row=3,column=1)

window.mainloop()
'''n=int(input())
m=int(input())
if(n>=m):
    print(n)
else:
    print(m)
#using tkintern'''

