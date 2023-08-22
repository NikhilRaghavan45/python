from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if label3entry.get()=='' or passwordentry.get()=='':
        messagebox.showerror("error","the fields cannot be empty")
    elif label3entry.get()=="Nikhil" and passwordentry.get()=="12345":
        messagebox.showinfo("success","welcome")
        base.destroy()
        import nsm
    else:
        messagebox.showerror('error','please give valid input')


base=Tk()
base.geometry("1221x814+0+0")
base.title("Login")
base.resizable(False,False)
bgimage=ImageTk.PhotoImage(file="bg.jpg")
imglabel=Label(base,image=bgimage)

loginframe=Frame(base,bg="white")
loginframe.place(x=200,y=100)
loginimage=PhotoImage(file="graduate3.png")

label2=Label(loginframe,image=loginimage)
label2.grid(row=0,columnspan=2,pady=10)

username=ImageTk.PhotoImage(file="user.png")
label3=Label(loginframe,text="Username",font=("times new roman",20,"bold"),image=username,compound=LEFT,bg="white")
label3.grid(row=1,column=0,pady=10,padx=20)
label3entry=Entry(loginframe,font=("times new roman",20,"bold"),fg="light slate gray")
label3entry.grid(row=1,column=1,pady=10,padx=20)


password=ImageTk.PhotoImage(file="lock.png")
passwordlabel=Label(loginframe,text="Password",font=("times new roman",20,"bold"),image=password,compound=LEFT,bg="white")
passwordlabel.grid(row=2,column=0,pady=10,padx=20)
passwordentry=Entry(loginframe,font=("times new roman",20,"bold"),fg="light slate gray")
passwordentry.grid(row=2,column=1,pady=10,padx=20)

loginbutton=Button(loginframe,text="Login",font=("times new roman",15,"bold"),command=login)
loginbutton.grid(row=3,column=1,pady=10)
imglabel.pack()
base.mainloop()