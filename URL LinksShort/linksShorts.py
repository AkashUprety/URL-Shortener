import tkinter
import pyshorteners
import pyperclip
from tkinter import*
t=tkinter.Tk()
t.geometry('860x525')
t.configure(bg='#1f3641')
t.resizable(False,False)
t.title("Link Shorts")

#-------------Image & Canvas
img=PhotoImage(file='codeclause.png')
Label(t,image=img,bg='#1f3641').place(x=-3,y=50)
sysName=Label(t,text='Intern',fg='#fff',bg='#1f3641',font=('Calibri',14)).place(x=20,y=50)
cn=Canvas(t,width=350,height=400,bg='#f0ffff').place(x=460,y=80)


#--------------main Functions
def short():
    url=entry1.get()
    sot =pyshorteners.Shortener().tinyurl.short(url)
    
    entry2.insert(END,sot)
    
def copyurl():
    url_short= entry2.get()
    pyperclip.copy(url_short)
    
    


#----------Lable & Entry or Buttons------------------
label=Label(t,text="URL Shotener",fg='#fff',bg='#1f3641',font=('Microsoft YaHei UI Light',28))
label.pack(fill='x')

label1=Label(cn,text="Enter URL",fg='black',bg='#f0ffff',font=('Microsoft YaHei UI Light',14))
label1.place(x=487,y=120)


def on_enter(e):
    entry1.delete(0,100)
    
def on_leave(e):
    name=entry1.get()
    if name=='':
        entry1.insert(0,EnterURL)

entry1=Entry(cn,width=33,fg='black',border=0,bg='#f0ffff',font=('Microsoft YaHei UI Light',11))
entry1.place(x=500,y=155)
entry1.insert(0,'Enter Your URL Link.')
entry1.bind('<FocusIn>',on_enter)
entry1.bind('<FocusOut>',on_leave)
Canvas(t,width=288,height=2,bg='black').place(x=490,y=181)


short=Button(cn,width=10,text='Short Link',border=0,bg='#1f3641',cursor='hand2',fg='#fff',command=short)
short.place(x=595,y=215)

entry2=Entry(cn,width=35,fg='black',border=1,bg='#f0ffff',font=('Microsoft YaHei UI Light',11),bd=0)
entry2.place(x=495,y=300)

copy_link=Button(cn,width=10,text='copy',border=0,bg='#1f3641',cursor='hand2',fg='#fff',command=copyurl)
copy_link.place(x=600,y=350)
label3=Label(t,text="Powered by Akash Uprety",fg='black',bg='#f0ffff',font=('Microsoft YaHei UI Light',9))
label3.place(x=560,y=430)


t.mainloop()
