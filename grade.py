import tkinter
from tkinter import *

root=Tk()
root.title("Grade Calculator")
root.geometry("1000x800")


def Calculation():
    english=int(englishentry.get())
    science=int(scienceentry.get())
    maths=int(mathsentry.get())
    social=int(socialentry.get())
    tamil=int(tamilentry.get())
    total=(english+science+maths+social+tamil)
    Label(text=f"{total}",font="arail 15 bold").place(x=250,y=270)

    average=int(total/5)
    Label(text=f"{average}",font="arial 15 bold").place(x=250,y=320)

    if (average>50):
        grade="PASS"
    else:
        grade="FAIL"

    Label(text=f"{grade}",font="arial 15 bold",fg="green").place(x=250,y=370)    
    


sub1=Label(root,text="English:",font="arial 20")
sub2=Label(root,text="Science:",font="arial 20")
sub3=Label(root,text="Maths:",font="arial 20")
sub4=Label(root,text="Social:",font="arial 20")
sub5=Label(root,text="Tamil:",font="arial 20")
total=Label(root,text="Total:",font="arial 20")
avg=Label(root,text="Avg:",font="arial 20")
grade=Label(root,text="Grade:",font="arial 20")


sub1.place(x=50,y=20)
sub2.place(x=50,y=70)
sub3.place(x=50,y=120)
sub4.place(x=50,y=170)
sub5.place(x=50,y=220)
total.place(x=50,y=270)
avg.place(x=50,y=320)
grade.place(x=50,y=370)

englishvalue=StringVar()
sciencevalue=StringVar()
mathsvalue=StringVar()
socialvalue=StringVar()
tamilvalue=StringVar()

englishentry=Entry(root,textvariable=englishvalue,font="arial 20",width=20)
scienceentry=Entry(root,textvariable=sciencevalue,font="arial 20",width=20)
mathsentry=Entry(root,textvariable=mathsvalue,font="arial 20",width=20)
socialentry=Entry(root,textvariable=socialvalue,font="arial 20",width=20)
tamilentry=Entry(root,textvariable=tamilvalue,font="arial 20",width=20)


englishentry.place(x=250,y=20)
scienceentry.place(x=250,y=70)
mathsentry.place(x=250,y=120)
socialentry.place(x=250,y=170)
tamilentry.place(x=250,y=220)

Button(text="Calculate",font="arial 20",bg="white",bd=10,command=Calculation).place(x=500,y=500)
Button(text="Exit",font="arial 20",bg="white",bd=10,width=8,command=lambda:exit()).place(x=35,y=500)


root.mainloop()
