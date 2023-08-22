from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas

def isexit():
    result=messagebox.askyesno('confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def export():
    url=filedialog.asksaveasfilename(defaultextension=".csv")
    indexing=stable.get_children()
    newlist=[]
    for index in indexing:
        content=stable.item(index)
        datalist=content['values']
        newlist.append(datalist)

    table=pandas.DataFrame(newlist,columns=['Id','Name','Mobile','Email','Address','Gender','DOB','Added Date','Added Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('success','Data is saved successfully')




def update():
    def update_data():
        date = time.strftime("%d/%m/%Y")
        exacttime = time.strftime("%H:%M:%S")
        query='update student set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(query,(nameentry.get(),phoneentry.get(),emailentry.get(),addressentry.get(),genderentry.get(),
                                dobentry.get(),date,exacttime,identry.get()))
        con.commit()
        messagebox.showinfo('success',f'Id {identry.get()} is updated successfully',parent=updatewindow)
        updatewindow.destroy()
        show()

    updatewindow = Toplevel()
    updatewindow.title('Update')
    updatewindow.resizable(False, False)
    updatewindow.grab_set()
    idlabel = Label(updatewindow, text="Id", font=("times new roman", 20, "bold"))
    idlabel.grid(row=0, column=0, padx=10, pady=20, sticky=W)
    identry = Entry(updatewindow, font=("romans", 20, "bold"), width=24, bd=2)
    identry.grid(row=0, column=1, padx=10, pady=20)

    namelabel = Label(updatewindow, text="Name", font=("times new roman", 20, "bold"))
    namelabel.grid(row=1, column=0, padx=10, pady=20, sticky=W)
    nameentry = Entry(updatewindow, font=("romans", 20, "bold"), width=24, bd=2)
    nameentry.grid(row=1, column=1, padx=10, pady=20)

    phonelabel = Label(updatewindow, text="Mobile", font=("times new roman", 20, "bold"))
    phonelabel.grid(row=2, column=0, padx=10, pady=20, sticky=W)
    phoneentry = Entry(updatewindow, font=("romans", 20, "bold"), width=24, bd=2)
    phoneentry.grid(row=2, column=1, padx=10, pady=20)

    emaillabel = Label(updatewindow, text="Email", font=("times new roman", 20, "bold"))
    emaillabel.grid(row=3, column=0, padx=10, pady=20, sticky=W)
    emailentry = Entry(updatewindow, font=("romans", 20, "bold"), width=24, bd=2)
    emailentry.grid(row=3, column=1, padx=10, pady=20)

    addresslabel = Label(updatewindow, text="Address", font=("times new roman", 20, "bold"))
    addresslabel.grid(row=4, column=0, padx=10, pady=20, sticky=W)
    addressentry = Entry(updatewindow, font=("romans", 20, "bold"), width=24, bd=2)
    addressentry.grid(row=4, column=1, padx=10, pady=20)

    genderlabel = Label(updatewindow, text="Gender", font=("times new roman", 20, "bold"))
    genderlabel.grid(row=5, column=0, padx=10, pady=20, sticky=W)
    genderentry = Entry(updatewindow, font=("romans", 20, "bold"), width=24, bd=2)
    genderentry.grid(row=5, column=1, padx=10, pady=20)

    doblabel = Label(updatewindow, text="D.O.B", font=("times new roman", 20, "bold"))
    doblabel.grid(row=6, column=0, padx=10, pady=20, sticky=W)
    dobentry = Entry(updatewindow, font=("romans", 20, "bold"), width=24, bd=2)
    dobentry.grid(row=6, column=1, padx=10, pady=20)

    updatebutton = ttk.Button(updatewindow, text="UPDATE", width=15,command=update_data)
    updatebutton.grid(row=7, columnspan=2, pady=15)

    indexing=stable.focus()
    content=stable.item(indexing)
    listdata=content['values']
    identry.insert(0,listdata[0])
    nameentry.insert(0, listdata[1])
    phoneentry.insert(0, listdata[2])
    emailentry.insert(0, listdata[3])
    addressentry.insert(0, listdata[4])
    genderentry.insert(0, listdata[5])
    dobentry.insert(0, listdata[6])



def show():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    stable.delete(*stable.get_children())
    for data in fetched_data:
        stable.insert('', END, values=data)


def delete():
    index=stable.focus()
    content=stable.item(index)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('deleted',f'this {content_id} is deleted successfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    stable.delete(*stable.get_children())
    for data in fetched_data:
        stable.insert('',END,values=data)

def search():
    def search_data():
        query='select *from student where id=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dob=%s'
        mycursor.execute(query,(identry.get(),nameentry.get(),emailentry.get(),phoneentry.get(),addressentry.get(),genderentry.get(),dobentry.get()))
        stable.delete(*stable.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            stable.insert('',END,values=data)



    searchwindow = Toplevel()
    searchwindow.title('Search')
    searchwindow.resizable(False, False)
    searchwindow.grab_set()
    idlabel = Label(searchwindow, text="Id", font=("times new roman", 20, "bold"))
    idlabel.grid(row=0, column=0, padx=10, pady=20, sticky=W)
    identry = Entry(searchwindow, font=("romans", 20, "bold"), width=24, bd=2)
    identry.grid(row=0, column=1, padx=10, pady=20)

    namelabel = Label(searchwindow, text="Name", font=("times new roman", 20, "bold"))
    namelabel.grid(row=1, column=0, padx=10, pady=20, sticky=W)
    nameentry = Entry(searchwindow, font=("romans", 20, "bold"), width=24, bd=2)
    nameentry.grid(row=1, column=1, padx=10, pady=20)

    phonelabel = Label(searchwindow, text="Mobile", font=("times new roman", 20, "bold"))
    phonelabel.grid(row=2, column=0, padx=10, pady=20, sticky=W)
    phoneentry = Entry(searchwindow, font=("romans", 20, "bold"), width=24, bd=2)
    phoneentry.grid(row=2, column=1, padx=10, pady=20)

    emaillabel = Label(searchwindow, text="Email", font=("times new roman", 20, "bold"))
    emaillabel.grid(row=3, column=0, padx=10, pady=20, sticky=W)
    emailentry = Entry(searchwindow, font=("romans", 20, "bold"), width=24, bd=2)
    emailentry.grid(row=3, column=1, padx=10, pady=20)

    addresslabel = Label(searchwindow, text="Address", font=("times new roman", 20, "bold"))
    addresslabel.grid(row=4, column=0, padx=10, pady=20, sticky=W)
    addressentry = Entry(searchwindow, font=("romans", 20, "bold"), width=24, bd=2)
    addressentry.grid(row=4, column=1, padx=10, pady=20)

    genderlabel = Label(searchwindow, text="Gender", font=("times new roman", 20, "bold"))
    genderlabel.grid(row=5, column=0, padx=10, pady=20, sticky=W)
    genderentry = Entry(searchwindow, font=("romans", 20, "bold"), width=24, bd=2)
    genderentry.grid(row=5, column=1, padx=10, pady=20)

    doblabel = Label(searchwindow, text="D.O.B", font=("times new roman", 20, "bold"))
    doblabel.grid(row=6, column=0, padx=10, pady=20, sticky=W)
    dobentry = Entry(searchwindow, font=("romans", 20, "bold"), width=24, bd=2)
    dobentry.grid(row=6, column=1, padx=10, pady=20)

    searchbutton = ttk.Button(searchwindow, text="SEARCH", width=15,command=search_data)
    searchbutton.grid(row=7, columnspan=2, pady=15)


def add():
    def add_data():
        if identry.get()=='' or nameentry.get()=='' or phoneentry.get()=='' or emailentry.get()=='' or addressentry.get()=='' or genderentry.get()=='' or dobentry.get()=="":
            messagebox.showerror('error','All fields are required to be filled',parent=addwindow)

        else:
            currentdate = time.strftime("%d/%m/%Y")
            currenttime = time.strftime("%H:%M:%S")
            try:
                query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(identry.get(),nameentry.get(),phoneentry.get(),emailentry.get(),addressentry.get(),
                                        genderentry.get(),dobentry.get(),currentdate,currenttime))
                con.commit()
                result=messagebox.askyesno("confirm","Data inserted successfully,do you want to clear the form")
                if result:
                    identry.delete(0,END)
                    nameentry.delete(0, END)
                    phoneentry.delete(0, END)
                    emailentry.delete(0, END)
                    addressentry.delete(0, END)
                    genderentry.delete(0, END)
                    dobentry.delete(0, END)

                else:
                    pass

            except:
                messagebox.showerror('Error','Id cannot be repeated',parent=addwindow)
                return

            query='select *from student'
            mycursor.execute(query)
            fetched_data=mycursor.fetchall()
            stable.delete(*stable.get_children())
            for data in fetched_data:
                datalist=list(data)
                stable.insert('',END,values=datalist)

    addwindow=Toplevel()
    addwindow.resizable(False,False)
    addwindow.grab_set()
    idlabel=Label(addwindow,text="Id",font=("times new roman",20,"bold"))
    idlabel.grid(row=0,column=0,padx=10,pady=20,sticky=W)
    identry=Entry(addwindow,font=("romans",20,"bold"),width=24,bd=2)
    identry.grid(row=0,column=1,padx=10,pady=20)

    namelabel=Label(addwindow,text="Name",font=("times new roman",20,"bold"))
    namelabel.grid(row=1,column=0,padx=10,pady=20,sticky=W)
    nameentry=Entry(addwindow,font=("romans",20,"bold"),width=24,bd=2)
    nameentry.grid(row=1,column=1,padx=10,pady=20)

    phonelabel=Label(addwindow,text="Mobile",font=("times new roman",20,"bold"))
    phonelabel.grid(row=2,column=0,padx=10,pady=20,sticky=W)
    phoneentry=Entry(addwindow,font=("romans",20,"bold"),width=24,bd=2)
    phoneentry.grid(row=2,column=1,padx=10,pady=20)

    emaillabel=Label(addwindow,text="Email",font=("times new roman",20,"bold"))
    emaillabel.grid(row=3,column=0,padx=10,pady=20,sticky=W)
    emailentry=Entry(addwindow,font=("romans",20,"bold"),width=24,bd=2)
    emailentry.grid(row=3,column=1,padx=10,pady=20)

    addresslabel=Label(addwindow,text="Address",font=("times new roman",20,"bold"))
    addresslabel.grid(row=4,column=0,padx=10,pady=20,sticky=W)
    addressentry=Entry(addwindow,font=("romans",20,"bold"),width=24,bd=2)
    addressentry.grid(row=4,column=1,padx=10,pady=20)

    genderlabel=Label(addwindow,text="Gender",font=("times new roman",20,"bold"))
    genderlabel.grid(row=5,column=0,padx=10,pady=20,sticky=W)
    genderentry=Entry(addwindow,font=("romans",20,"bold"),width=24,bd=2)
    genderentry.grid(row=5,column=1,padx=10,pady=20)

    doblabel=Label(addwindow,text="D.O.B",font=("times new roman",20,"bold"))
    doblabel.grid(row=6,column=0,padx=10,pady=20,sticky=W)
    dobentry=Entry(addwindow,font=("romans",20,"bold"),width=24,bd=2)
    dobentry.grid(row=6,column=1,padx=10,pady=20)

    subbutton=ttk.Button(addwindow,text="SUBMIT",width=15,command=add_data)
    subbutton.grid(row=7,columnspan=2,pady=15)



def alarm():
    date=time.strftime("%d/%m/%Y")
    exacttime=time.strftime("%H:%M:%S")
    DTlabel.config(text=f"  Date: {date}\n Time: {exacttime} ")
    DTlabel.after(1000,alarm)

def connect():
    def join():
        global mycursor,con
        try:
            con=pymysql.connect(host=hostentry.get(),user=userentry.get(),password=passentry.get())
            mycursor=con.cursor()
        except:
            messagebox.showerror("Error","Invalid",parent=connectwindow)
            return
        try:
            query='create database studentmanagementsystem'
            mycursor.execute(query)
            query='use studentmanagementsystem'
            mycursor.execute(query)
            query='create table student(id int not null primary key,name varchar(30),mobile varchar(10),email varchar(30),' \
                    'address varchar(100),gender varchar(20),dob varchar(20),date varchar(50),time varchar(50))'
            mycursor.execute(query)
        except:
            query='use studentmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('success', "connection successful", parent=connectwindow)
        connectwindow.destroy()

        addbutton.config(state=NORMAL)
        updatebutton.config(state=NORMAL)
        deletebutton.config(state=NORMAL)
        searchbutton.config(state=NORMAL)
        showbutton.config(state=NORMAL)
        exportbutton.config(state=NORMAL)

    connectwindow=Toplevel()
    connectwindow.grab_set()
    connectwindow.geometry('470x250+700+230')
    connectwindow.title('DBconnection')
    connectwindow.resizable(False,False)

    hostlabel=Label(connectwindow,text="HOST NAME",font=("arial",20,"bold"))
    hostlabel.grid(row=0,column=0,pady=10)

    hostentry=Entry(connectwindow,font=("times new roman",15,"bold"),bd=2)
    hostentry.grid(row=0,column=1,padx=30,pady=10)

    userlabel=Label(connectwindow,text="USER NAME",font=("arial",20,"bold"))
    userlabel.grid(row=1,column=0,pady=10)

    userentry=Entry(connectwindow,font=("times new roman",15,"bold"),bd=2)
    userentry.grid(row=1,column=1,padx=30,pady=10)

    passlabel=Label(connectwindow,text="PASSWORD",font=("arial",20,"bold"))
    passlabel.grid(row=2,column=0,pady=10)

    passentry=Entry(connectwindow,font=("times new roman",15,"bold"),bd=2)
    passentry.grid(row=2,column=1,padx=30,pady=10)

    cbutton=ttk.Button(connectwindow,text="Connect",width=15,command=join)
    cbutton.grid(row=3,columnspan=2,pady=10)


root=ttkthemes.ThemedTk()

root.get_themes()

root.set_theme("breeze")
root.geometry("1221x814+0+0")
root.title("student management system")
root.resizable(False,False)

DTlabel=Label(root,font=("times new roman",15,"bold"))
DTlabel.place(x=10,y=10)
alarm()

slabel=Label(root,text="STUDENT MANAGEMENT SYSTEM",font=("arial",20,"italic bold"))
slabel.place(x=400,y=0)

connectbutton=ttk.Button(root,text="connect database",width=15,command=connect)
connectbutton.place(x=1050,y=10)


lframe=Frame(root)
lframe.place(x=50,y=80,width=400,height=900)

logo_image=PhotoImage(file="reading-book.png")
logolabel=Label(lframe,image=logo_image)
logolabel.grid(row=0,column=0)

addbutton=ttk.Button(lframe,text="Add Student",width=15,state=DISABLED,command=add)
addbutton.grid(row=1,column=0,pady=20)

updatebutton=ttk.Button(lframe,text="Update Student",width=15,state=DISABLED,command=update)
updatebutton.grid(row=2,column=0,pady=20)

deletebutton=ttk.Button(lframe,text="Delete Student",width=15,state=DISABLED,command=delete)
deletebutton.grid(row=3,column=0,pady=20)

searchbutton=ttk.Button(lframe,text="Search Student",width=15,state=DISABLED,command=search)
searchbutton.grid(row=4,column=0,pady=20)

showbutton=ttk.Button(lframe,text="Show Student",width=15,state=DISABLED,command=show)
showbutton.grid(row=5,column=0,pady=20)

exportbutton=ttk.Button(lframe,text="Export Student",width=15,state=DISABLED,command=export)
exportbutton.grid(row=6,column=0,pady=20)

exitbutton=ttk.Button(lframe,text="Exit Student",width=15,command=isexit)
exitbutton.grid(row=7,column=0,pady=20)

rframe=Frame(root)
rframe.place(x=350,y=80,width=820,height=600)

scrollbarX=Scrollbar(rframe,orient=HORIZONTAL)
scrollbarY=Scrollbar(rframe,orient=VERTICAL)

stable=ttk.Treeview(rframe,columns=('Id','Name','Mobile','Email','Address','Gender',
                             'D.O.B','Added Date','Added Time'),
                    xscrollcommand=scrollbarX.set,yscrollcommand=scrollbarY.set)

scrollbarX.config(command=stable.xview)
scrollbarY.config(command=stable.yview)

scrollbarX.pack(side=BOTTOM,fill=X)
scrollbarY.pack(side=RIGHT,fill=Y)
stable.pack(fill=BOTH,expand=1)

stable.heading('Id',text='Id')
stable.heading('Name',text='Name')
stable.heading('Mobile',text='Mobile')
stable.heading('Email',text='Email')
stable.heading('Address',text='Address')
stable.heading('Gender',text='Gender')
stable.heading('D.O.B',text='D.O.B')
stable.heading('Added Date',text='Added Date')
stable.heading('Added Time',text='Added Time')

stable.column('Id',width=60,anchor=CENTER)
stable.column('Name',width=150,anchor=CENTER)
stable.column('Mobile',width=150,anchor=CENTER)
stable.column('Email',width=200,anchor=CENTER)
stable.column('Address',width=200,anchor=CENTER)
stable.column('Gender',width=60,anchor=CENTER)
stable.column('D.O.B',width=60,anchor=CENTER)
stable.column('Added Date',width=100,anchor=CENTER)
stable.column('Added Time',width=100,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview',rowheight=40,font=('arial',15,'bold'))

stable.config(show='headings')

root.mainloop()