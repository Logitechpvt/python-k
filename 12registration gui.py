from tkinter import*
base=Tk()
base.geometry("500x500")
base.title("Registration Form")

ib=Label(base,text="Registration Form",width=50,font=("arial",15))
ib.place(x=0,y=60)

ib1=Label(base,text="Enter Name",width=10,font=("arial",12))
ib1.place(x=20,y=120)
en1=Entry(base)
en1.place(x=200,y=120)

ib3=Label(base,text="Enter Email",width=10,font=("arial",12))
ib3.place(x=19,y=160)
en3=Entry(base)
en3.place(x=200,y=160)

ib4=Label(base,text="Contact Number",width=13,font=("arial",12))
ib4.place(x=19,y=200)
en4=Entry(base)
en4.place(x=200,y=200)
ib5=Label(base,text="Select Gender",width=15,font=("arial",12))
ib5.place(x=5,y=240)
vars=IntVar()
Radiobutton(base,text="male",padx=5,variable=vars,value=1).place(x=180,y=240)
Radiobutton(base,text="female",padx=10,variable=vars,value=2).place(x=240,y=240)
Radiobutton(base,text="others",padx=15,variable=vars,value=3).place(x=310,y=240)

list_of_entry=("United states","India","Nepal","Germaney")
cv=StringVar()
drplist=OptionMenu(base,cv,*list_of_entry)
drplist.config(width=15)

cv.set("United states")
ib2=Label(base,text="Select Country",width=13,font=("arial",12))
ib2.place(x=14,y=280)
drplist.place(x=200,y=275)

ib6=Label(base,text="Enter Password",width=13,font=("arial",12))
ib6.place(x=19,y=320)
en6=Entry(base,show="*")
en6.place(x=200,y=320)

ib7=Label(base,text="Re-Enter password",width=15,font=("arial",12))
ib7.place(x=21,y=360)
en7=Entry(base,show="*")
en7.place(x=200,y=360)
Button(base,text="SUBMIT",width=10).place(x=200,y=400)
base.mainloop()

