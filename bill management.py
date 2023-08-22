from tkinter import *


root=Tk()
root.geometry("1000x900")
root.title("Bill Management")

def Reset():
    entry_Dosa.delete(0,END)
    entry_Coffee.delete(0,END)
    entry_Tea.delete(0,END)
    entry_Juices.delete(0,END)
    entry_Cakes.delete(0,END)
    entry_Cookies.delete(0,END)
    entry_Maggi.delete(0,END)

def Total():
    try:a1=int(Dosa.get())
    except: a1=0

    try:a2=int(Coffee.get())
    except: a2=0

    try:a3=int(Tea.get())
    except: a3=0

    try:a4=int(Juices.get())
    except: a4=0

    try:a5=int(Cakes.get())
    except: a5=0

    try:a6=int(Cookies.get())
    except: a6=0
    
    try:a7=int(Maggi.get())
    except: a7=0


    c1=30*a1
    c2=12*a2
    c3=10*a3
    c4=30*a4
    c5=30*a5
    c6=50*a6
    c7=30*a7

    lbl_total=Label(f2,font=('aria',20,'bold'),text="Total",width=16,fg="yellow",bg="black")
    lbl_total.place(x=0,y=50)

    entry_total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_Bill,bd=6,width=15,bg="lightgreen")
    entry_total.place(x=20,y=100)

    totalcost=c1+c2+c3+c4+c5+c6+c7
    string_bill="Rs.",str('%.2f' %totalcost)
    Total_Bill.set(string_bill)

Label(text="BILL MANAGEMENT",bg="pink",fg="black",font=("calibri",33),width="300",height="2").pack()

f=Frame(root,bg="black",highlightbackground="orange",highlightthickness=1,width=300,height=700)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="white",bg="black").place(x=80,y=0)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="Dosa         Rs.30/plate",fg="white",bg="black").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="coffee        Rs.12/cup",fg="white",bg="black").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Tea           Rs.10/cup",fg="white",bg="black").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="juices        Rs.30/cup",fg="white",bg="black").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Cakes        Rs.30/plate",fg="white",bg="black").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="cookies      Rs.50/plate",fg="white",bg="black").place(x=10,y=230)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Maggi       Rs.30/plate",fg="white",bg="black").place(x=10,y=260)


f2=Frame(root,bg="yellow",highlightbackground="orange",highlightthickness=1,width=300,height=700)
f2.place(x=690,y=118)

Bill=Label(f2,text="Bill",font=('calibri',20),bg="yellow")
Bill.place(x=120,y=10)


f1=Frame(root,bd=5,height=500,relief=RAISED)
f1.pack()


Dosa=StringVar()
Coffee=StringVar()
Tea=StringVar()
Juices=StringVar()
Cakes=StringVar()
Cookies=StringVar()
Maggi=StringVar()
Total_Bill=StringVar()


lbl_Dosa=Label(f1,font=("aria",20,'bold'),text="Dosa",width=12,fg="blue")
lbl_Coffee=Label(f1,font=("aria",20,'bold'),text="Coffee",width=12,fg="blue")
lbl_Tea=Label(f1,font=("aria",20,'bold'),text="Tea",width=12,fg="blue")
lbl_Juices=Label(f1,font=("aria",20,'bold'),text="Juices",width=12,fg="blue")
lbl_Cakes=Label(f1,font=("aria",20,'bold'),text="Cakes",width=12,fg="blue")
lbl_Cookies=Label(f1,font=("aria",20,'bold'),text="Cookies",width=12,fg="blue")
lbl_Maggi=Label(f1,font=("aria",20,'bold'),text="Maggi",width=12,fg="blue")
lbl_Dosa.grid(row=1,column=0)
lbl_Coffee.grid(row=2,column=0)
lbl_Tea.grid(row=3,column=0)
lbl_Juices.grid(row=4,column=0)
lbl_Cakes.grid(row=5,column=0)
lbl_Cookies.grid(row=6,column=0)
lbl_Maggi.grid(row=7,column=0)


entry_Dosa=Entry(f1,font=("aria",20,'bold'),textvariable=Dosa,bd=6,width=8,bg="lightpink")
entry_Coffee=Entry(f1,font=("aria",20,'bold'),textvariable=Coffee,bd=6,width=8,bg="lightpink")
entry_Tea=Entry(f1,font=("aria",20,'bold'),textvariable=Tea,bd=6,width=8,bg="lightpink")
entry_Juices=Entry(f1,font=("aria",20,'bold'),textvariable=Juices,bd=6,width=8,bg="lightpink")
entry_Cakes=Entry(f1,font=("aria",20,'bold'),textvariable=Cakes,bd=6,width=8,bg="lightpink")
entry_Cookies=Entry(f1,font=("aria",20,'bold'),textvariable=Cookies,bd=6,width=8,bg="lightpink")
entry_Maggi=Entry(f1,font=("aria",20,'bold'),textvariable=Maggi,bd=6,width=8,bg="lightpink")

entry_Dosa.grid(row=1,column=1)
entry_Coffee.grid(row=2,column=1)
entry_Tea.grid(row=3,column=1)
entry_Juices.grid(row=4,column=1)
entry_Cakes.grid(row=5,column=1)
entry_Cookies.grid(row=6,column=1)
entry_Maggi.grid(row=7,column=1)


btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)







root.mainloop()
