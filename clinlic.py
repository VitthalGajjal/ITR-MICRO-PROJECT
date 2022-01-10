
from tkinter import *
from os import name, spawnl
from datetime import datetime
from tkinter import messagebox
from functools import partial
import MySQLdb

tkWindow = Tk()

def addpatient():
    top1=Toplevel(tkWindow)
    top1.geometry('400x500')
    top1.title(' Add Patients ')
    headline=Label(top1,text="Add Patient",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=15,y=15)

    reglab = Label(top1,text="Reg.No", font = "Verdana 10 bold").place(x=15,y=80)
    regno11 = StringVar()
    regno= Entry(top1, textvariable=regno11).place(x=15,y=110)

    namelab = Label(top1,text="Patient Name", font = "Verdana 10 bold").place(x=15,y=160)
    name11 = StringVar()
    name= Entry(top1, textvariable=name11).place(x=15, y=190)

    datelab = Label(top1,text="DOB", font = "Verdana 10 bold").place(x=15, y=240)
    date11 = StringVar()
    date= Entry(top1, textvariable=date11).place(x=15, y=270)

    pagelab = Label(top1,text="Age", font = "Verdana 10 bold").place(x=15, y=320)
    page11 = StringVar()
    page= Entry(top1, textvariable=page11).place(x=15, y=350)

    Genderlab = Label(top1,text="Gender", font = "Verdana 10 bold").place(x=200, y=80)
    gender11 = StringVar()
    genderlist=["Male","Female","Other"]
    gender=OptionMenu(top1,gender11,*genderlist).place(x=200,y=110)

    pnolab = Label(top1,text="mobile Number", font = "Verdana 10 bold").place(x=200, y=160)
    pno11 = StringVar()
    pno= Entry(top1, textvariable=pno11).place(x=200, y=190)

    emaillab = Label(top1,text="Email", font = "Verdana 10 bold").place(x=200, y=240)
    email11 = StringVar()
    email= Entry(top1, textvariable=email11).place(x=200, y=270)

    Addresslab = Label(top1,text="Address ", font = "Verdana 10 bold").place(x=200, y=320)
    address22 = StringVar()
    address= Entry(top1, textvariable=address22).place(x=200, y=350)

    def callme1():
        mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="clinic")
         
        regno1=regno11.get()
        P_name=name11.get()
        dates=date11.get()
        page1=page11.get()
        gender1=gender11.get()
        pno1=pno11.get()
        email1=email11.get()
        address1=address22.get()
        query="""INSERT INTO patient (reg_no,Patientname,dob,patientage,patientgender,patientm_no,patientemail,patientaddress) VALUES ('{}', '{}', '{}','{}','{}','{}','{}','{}');""".format(regno1,P_name,dates,page1,gender1,pno1,email1,address1)
        cur=mycon.cursor()
    
        cur.execute(query)
        mycon.commit()
        cur.close()
        headline55=Label(top1,text="Sucessfully Added!...",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=15,y=430)
    
    save= Button(top1, text="Save", font = "Verdana 10 bold",width=10,command=callme1).place(x=15, y=400)
    cahl1= Button(top1, text="Cancel", font = "Verdana 10 bold",command=top1.destroy).place(x=200,y=400)
        
    top1.mainloop()

def sp():
    
    top2=Toplevel(tkWindow)
    top2.geometry('1200x500')    
    top2.title('Patients list ')
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="clinic")
                
    cur=mycon.cursor()
                
    query="select * from patient limit 0,10;"
    cur.execute(query)
    i=0
    tdata=cur.fetchall()
    
    headline2=Label(top2,text=" Patient's list",width="20",fg = "white", bg = "blue", font = "Verdana 10 bold").grid(row=0, column=0) 
    e11 = Label(top2, text="RegesterNo",width="20",fg = "white", bg = "yellow", font = "Verdana 10 bold").grid(row=1,column=0) 
    
    lb=Label(top2,text="Name",width="15",fg = "white", bg = "yellow", font = "Verdana 10 bold").grid(row=1,column=1)
    lb1=Label(top2,text="DOB",width="15",fg = "white", bg = "yellow", font = "Verdana 10 bold").grid(row=1,column=2)
    lb2=Label(top2,text="Age",width="15",fg = "white", bg = "yellow", font = "Verdana 10 bold").grid(row=1,column=3)
    lb3=Label(top2,text="Gender",width="15",fg = "white", bg = "yellow", font = "Verdana 10 bold").grid(row=1,column=4)
    lb4=Label(top2,text="Ph.No",width="15",fg = "white", bg = "yellow", font = "Verdana 10 bold").grid(row=1,column=5)
    lb5=Label(top2,text="Email",width="15",fg = "white", bg = "yellow", font = "Verdana 10 bold").grid(row=1,column=6)
    lb6=Label(top2,text="Address",width="15",fg = "white", bg = "yellow", font = "Verdana 10 bold").grid(row=1,column=7)
        
    i=2
    for p in tdata: 
        e = Label(top2,width=15, text=p[0]) 
        e.grid(row=i, column=0) 

        e1 = Label(top2,width=15, text=p[1]) 
        e1.grid(row=i, column=1) 

        e2 = Label(top2,width=15, text=p[2]) 
        e2.grid(row=i, column=2) 

        e3 = Label(top2,width=15, text=p[3]) 
        e3.grid(row=i, column=3) 

        e4 = Label(top2,width=15, text=p[4]) 
        e4.grid(row=i, column=4)

        e5 = Label(top2,width=15, text=p[5]) 
        e5.grid(row=i, column=5)

        e6 = Label(top2,width=15, text=p[6]) 
        e6.grid(row=i, column=6)

        e7 = Label(top2,width=15, text=p[7]) 
        e7.grid(row=i, column=7)
       
        i=i+1
    mycon.commit()
    
    def callmeback():
        mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="clinic")
                
        cur=mycon.cursor()
                
        query="select * from patient limit 0,10;"
        cur.execute(query)
        i=0
        tdata=cur.fetchall()
    
        headline2=Label(top2,text="Patient's list",width="15",fg = "white", bg = "blue", font = "Verdana 10 bold").grid(row=0, column=0)
       
        i=2
        for student in tdata: 
            for j in range(len(student)):
                e = Label(top2,width=15, text=student[j]) 
                e.grid(row=i, column=j) 
            i=i+1
        mycon.commit()

    ref1=Button(top2, text="Refresh", font = "Verdana 10 bold",width=10,command=callmeback).place(x=15, y=460)
    def delrec():
        top9=Toplevel(tkWindow)
        top9.geometry('250x300')

        namelb = Label(top9,text="Patient Registration number",font = "Verdana 10 bold").place(x=15,y=15)
        query="select reg_no from patient"
        cur.execute(query)
        tdata=cur.fetchall()
        print(tdata)
        namelist=[]
        for a in tdata:
            data=(a[0])
            namelist.append(data)

        clicked=StringVar()
            
        drop=OptionMenu(top9,clicked,*namelist).place(x=50,y=50)
    
        def delrec1():
        
            mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="clinic")
                
            cur=mycon.cursor()
            
            cl=clicked.get()
            query="""delete from patient where reg_no='{}';""".format(cl)
            cur.execute(query)
            mycon.commit()
            cur.close()
            Addresslab35 = Label(top9,text=" Sucessfully Deleted!..").place(x=15, y=200)

        deleteit= Button(top9, text="Delete Record",width=10,command=delrec1).place(x=15, y=150)
        
        top9.mainloop()

        def check():
            mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="clinic")

    delete= Button(top2, text="Delete Rec", font = "Verdana 10 bold",width=10,command=delrec).place(x=165, y=460)
    cahl22= Button(top2, text="Back", font = "Verdana 10 bold",command=top2.destroy).place(x=315,y=460)
    top2.mainloop()
           
def addapt():
    top3=Toplevel(tkWindow)
    top3.geometry('450x500')
    top3.title(' Add Appointment ')
    headline4=Label(top3,text="Patient Appointment",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=15,y=15)

    namelab = Label(top3,text="Patient Name",font = "Verdana 10 bold").place(x=15,y=90)
    clicked = StringVar()
    name= Entry(top3, textvariable=clicked).place(x=200, y=90)

    date= Label(top3,text="Date",font = "Verdana 10 bold").place(x=15,y=140)
    dateap=StringVar()
    dateapt= Entry(top3, textvariable=dateap,font = "Verdana 10 bold").place(x=200,y=140)

    namelab = Label(top3,text="Appointment session",font = "Verdana 10 bold").place(x=15,y=190)
    clicked2 = StringVar()
    name= Entry(top3, textvariable=clicked2).place(x=200, y=190)
 
    
    message= Label(top3,text="Message",font = "Verdana 10 bold").place(x=15,y=240)
    msg=StringVar()
    emessage= Entry(top3, textvariable=msg).place(x=200,y=240)
    
     
    namelab = Label(top3,text="OPD",font = "Verdana 10 bold").place(x=15,y=290)
    clicked3 = StringVar()
    name= Entry(top3, textvariable=clicked3).place(x=200, y=290)
  

    def callme():
        mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="clinic")
         
        pname=clicked.get()
        session=clicked2.get()
        opd=clicked3.get()
        message=msg.get()
        date=dateap.get()
        query="""INSERT INTO appointment (appointmentname,appointmentdate,appointmentsession,appointmentopd,appointmentmessage) VALUES ('{}', '{}', '{}','{}','{}');""".format(pname,date,session,opd,message)
        cur=mycon.cursor()
        cur.execute(query)
        mycon.commit()
        cur.close()
        headline77=Label(top3,text="Sucessfully added",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=15,y=400)
      
    saveapt2= Button(top3, text="Save", font = "Verdana 10 bold",command=callme).place(x=15,y=350)
    cahl= Button(top3, text="Back", font = "Verdana 10 bold",command=top3.destroy).place(x=200,y=350)
   
    top3.mainloop()
                                        
def listapts():
    top4=Toplevel(tkWindow)
    top4.geometry('800x500')    
    top4.title('Appointments list ')
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="clinic")
                
    cur=mycon.cursor()
                
    query="select * from appointment limit 0,10;"
    cur.execute(query)
    i=0
    tdata=cur.fetchall()
    
    headline2=Label(top4,text="Appointments schedule",width="20",fg = "white", bg = "blue", font = "Verdana 10 bold").grid(row=0, column=0) 
    e11 = Label(top4, text="Name",width="20",fg = "white", bg = "yellow", font = "Verdana 10 bold").grid(row=1,column=0) 
    
    lb=Label(top4,text="Date",width="15",fg = "white", bg = "yellow", font = "Verdana 10 bold").grid(row=1,column=1)
    lb1=Label(top4,text="Session",width="15",fg = "white", bg = "yellow", font = "Verdana 10 bold").grid(row=1,column=2)
    lb2=Label(top4,text="OPD Type",width="15",fg = "white", bg = "yellow", font = "Verdana 10 bold").grid(row=1,column=3)
    lb3=Label(top4,text="Message",width="15",fg = "white", bg = "yellow", font = "Verdana 10 bold").grid(row=1,column=4)
    
    i=2
    for p in tdata: 
        e = Label(top4,width=15, text=p[0]) 
        e.grid(row=i, column=0) 

        e1 = Label(top4,width=15, text=p[1]) 
        e1.grid(row=i, column=1) 

        e2 = Label(top4,width=15, text=p[2]) 
        e2.grid(row=i, column=2) 

        e3 = Label(top4,width=15, text=p[3]) 
        e3.grid(row=i, column=3) 

        e4 = Label(top4,width=15, text=p[4]) 
        e4.grid(row=i, column=4)

        i=i+1
		
    mycon.commit() 

    def callmeback223():

        mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="clinic")
                
        cur=mycon.cursor()
                    
        query="select * from appointment limit 0,10;"
        cur.execute(query)
        i=0
        print("530")
        tdata=cur.fetchall()
        print("532")
        headline2=Label(top4,text="Appointment Lists",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=0, column=0) 
        print("536")
        e11 = Label(top4, text="Name",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=0) 
        print("538")
        
        lb=Label(top4,text="Date",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=1)
        lb1=Label(top4,text="Session",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=2)
        lb2=Label(top4,text="Opd Type",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=3)
        lb3=Label(top4,text="Message",width="15",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=1,column=4)
        print("545")
        i=2
        for p in tdata: 
            e = Label(top4,width=15, text=p[0]) 
            e.grid(row=i, column=0) 
            print("550")
            e1 = Label(top4,width=15, text=p[1]) 
            e1.grid(row=i, column=1) 

            e2 = Label(top4,width=15, text=p[2]) 
            e2.grid(row=i, column=2) 

            e3 = Label(top4,width=15, text=p[3]) 
            e3.grid(row=i, column=3) 

            e4 = Label(top4,width=15, text=p[4]) 
            e4.grid(row=i, column=4)

            i=i+1
        print("570")
        mycon.commit() 
     
    def deleterecorda():
        top10=Toplevel(tkWindow)
        top10.geometry('200x200')

        namelb = Label(top10,text=" Registration number",font = "Verdana 10 bold").place(x=15,y=15)
        query="select appointmentname from appointment"
        cur.execute(query)
        tdata=cur.fetchall()
        print(tdata)
        namelist=[]
        for a in tdata:
            data=(a[0])
            namelist.append(data)

        clicked=StringVar()
        drop=OptionMenu(top10,clicked,*namelist).place(x=15,y=40)
    
        def delrec1():
        
            mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="clinic")
                
            cur=mycon.cursor()
            
            cl=clicked.get()
            query="""delete from appointment where appointmentname='{}';""".format(cl)
            cur.execute(query)
            mycon.commit()
            query="select * from appointment limit 0,10;"
            cur.execute(query)
            i=0
            tdata=cur.fetchall()
    
            headline2=Label(top4,text="List of Appointments",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").grid(row=0, column=0) 
            i=2
            for student in tdata: 
                for j in range(len(student)):
                    e = Label(top4,width=10, text=student[j]) 
                    e.grid(row=i, column=j) 
                i=i+1
				
        deleteit= Button(top10, text="Delete Rec", font = "Verdana 10 bold",width=10,command=delrec1).place(x=15,y=150)
   
    deleteit= Button(top4, text="Delete Rec", font = "Verdana 10 bold",width=10,command=deleterecorda).place(x=15, y=400)
    cahl33= Button(top4, text="Cancel", font = "Verdana 10 bold",command=top4.destroy).place(x=150,y=400)
    top4.mainloop()

def genratebill():
    top5=Toplevel(tkWindow)
    top5.geometry('500x500')
    headline30=Label(top5,text="Generate Bill",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=15,y=15)
    
    pnamelb = Label(top5,text=" Patient name",font = "Verdana 10 bold").place(x=15, y=90)
    p2 = StringVar()
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="clinic")
                
    cur=mycon.cursor()
              
    query="select appointmentname from appointment"
    cur.execute(query)
    tdata=cur.fetchall()
    print(tdata)
    namelist=[]
    for a in tdata:
        data=(a[0])
        namelist.append(data)

    drop36=OptionMenu(top5,p2,*namelist).place(x=15, y=120)
    
    datelb = Label(top5,text="date",font = "Verdana 10 bold").place(x=15, y=170)
    d2 = StringVar()
    date= Entry(top5, textvariable=d2).place(x=15, y=200)

    billtypelb = Label(top5,text="Bill Type",font = "Verdana 10 bold").place(x=15, y=250)
    bill2 = StringVar()
    aptscl=["OPD","IPD","Reciept"]
    drop22=OptionMenu(top5,bill2,*aptscl).place(x=15, y=280)

    opdnamelb = Label(top5,text="OPD type",font = "Verdana 10 bold").place(x=15, y=330)
    o2 = StringVar()
    opdlist=["Gynecologist","Orthopedic"]
    opds=OptionMenu(top5,o2,*opdlist).place(x=15, y=360)

    billnolb = Label(top5,text="Bill Number",font = "Verdana 10 bold").place(x=300,y=90)
    b2 = StringVar()
    billno= Entry(top5, textvariable=b2).place(x=300,y=120)
 
    opdnolb = Label(top5,text="OPD Number ",font = "Verdana 10 bold").place(x=300, y=170)
    opdno2 = StringVar()
    opdno= Entry(top5, textvariable=opdno2).place(x=300, y=200)
   
    ipdnolb = Label(top5,text="IPD Number",font = "Verdana 10 bold").place(x=300, y=250)
    i2 = StringVar()
    ipdno= Entry(top5, textvariable=i2).place(x=300, y=280)
  
    paymodlb = Label(top5,text=" Payment Mode",font = "Verdana 10 bold").place(x=300, y=330)
    paymod2 = StringVar()
    paymodlist=["Cash","Online Paymant","UPI","Credit Card","Debit Card"]
    
    opds=OptionMenu(top5,paymod2,*paymodlist).place(x=300, y=350)

    def total():

        if o2.get()=="Orthopedic":
            
            price=750
        else:
            price=1000

        mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="clinic")

        pname=b2.get()
        session=bill2.get()
        opd=opdno2.get()
        message=p2.get()
        opdn=o2.get()
        ip=i2.get()
        pay=paymod2.get()    
        date_time=d2.get()
        
        print(date_time)
        
        query="""INSERT INTO bill (billno,billpatientname,billdate,billtype,opdtype,opdnumber,ipdnumber,billpaymod,total) VALUES ('{}', '{}', '{}','{}','{}', '{}', '{}','{}','{}');""".format(pname,message,date_time,session,opdn,opd,ip,pay,price)
        cur=mycon.cursor()
        
        cur.execute(query)
        mycon.commit()
        cur.close()
        metoo()
       
    def metoo():
        top6=Toplevel(tkWindow)
        top6.geometry('500x400')
        billno=b2.get()
        billtype=bill2.get()
        opdno=opdno2.get()
        pnamee=p2.get()
        opd=o2.get()
        ip=i2.get()
        pay=paymod2.get()

        headline2=Label(top6,text="BILL",width="40",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=15,y=15)

        nlb = Label(top6,text="Bill Number : ",font = "Verdana 10 bold").place(x=15,y=90)
        bb = Label(top6,text=billno).place(x=15, y=120)

        nlb2 = Label(top6,text="Bill Type :",font = "Verdana 10 bold").place(x=15,y=170)
        bb2 = Label(top6,text=billtype).place(x=15, y=200)

        nlb3 = Label(top6,text="OPD No :",font = "Verdana 10 bold").place(x=15,y=250)
        bb3= Label(top6,text=opdno).place(x=15, y=280)
        

        nlb4 = Label(top6,text="Patient Name : ",font = "Verdana 10 bold").place(x=200,y=90)
        bb4= Label(top6,text=pnamee).place(x=200, y=120)

        nlb5 = Label(top6,text="OPD :",font = "Verdana 10 bold").place(x=200,y=170)
        bb= Label(top6,text=opd).place(x=200, y=200)

        nlb6 = Label(top6,text="IPD NO : ",font = "Verdana 10 bold").place(x=200,y=250)
        bb6= Label(top6,text=ip).place(x=200, y=280)

        nlb7 = Label(top6,text="Mode Of payment : ",font = "Verdana 10 bold").place(x=200,y=330)
        bb7= Label(top6,text=pay).place(x=200, y=360)

        headline2=Label(top6,text="ThankYou....",width="20",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=15,y=330)

        top6.mainloop()
    
    saveapt22= Button(top5, text="Save",font = "Verdana 10 bold",command=total).place(x=15,y=400)
    cahl44= Button(top5, text="Cancel",font = "Verdana 10 bold",command=top5.destroy).place(x=300,y=400)

    top5.mainloop()

def listbill():
    top7=Toplevel(tkWindow)
    top7.geometry('1320x500')    
    
    mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="clinic")
                
    cur=mycon.cursor()
                
    query="select * from bill;"
    cur.execute(query)
    i=0
    tdata=cur.fetchall()
    
    headline2=Label(top7,text="List of Bills",width="20",fg = "white", bg = "blue", font = "Verdana 10 bold").grid(row=0, column=0) 
    
    e11 = Label(top7, text="Bill No",width="20",fg = "white", bg = "yellow", font = "Verdana 10 bold").grid(row=1,column=0) 
    
    lb3=Label(top7,text="Name",width="15",fg = "white", bg = "yellow", font = "Verdana 10 bold").grid(row=1,column=1)
    lb=Label(top7,text="Date",width="15",fg = "white", bg = "yellow", font = "Verdana 10 bold").grid(row=1,column=2)
    lb1=Label(top7,text="Bill Type",width="15",fg = "white", bg = "yellow", font = "Verdana 10 bold").grid(row=1,column=3)
    lb4=Label(top7,text="OPD Type",width="15",fg = "white", bg = "yellow", font = "Verdana 10 bold").grid(row=1,column=4)
    lb2=Label(top7,text="OPD Number",width="15",fg = "white", bg = "yellow", font = "Verdana 10 bold").grid(row=1,column=5)
    lb5=Label(top7,text="IPD Number",width="15",fg = "white", bg = "yellow", font = "Verdana 10 bold").grid(row=1,column=6)
    lb6=Label(top7,text="Payment Mode",width="15",fg = "white", bg = "yellow", font = "Verdana 10 bold").grid(row=1,column=7)
    lb6=Label(top7,text="Total",width="15",fg = "white", bg = "yellow", font = "Verdana 10 bold").grid(row=1,column=8)
    i=2
    for p in tdata: 
        e = Label(top7,width=15, text=p[0]) 
        e.grid(row=i, column=0) 

        e1 = Label(top7,width=15, text=p[1]) 
        e1.grid(row=i, column=1) 

        e2 = Label(top7,width=15, text=p[2]) 
        e2.grid(row=i, column=2) 

        e3 = Label(top7,width=15, text=p[3]) 
        e3.grid(row=i, column=3) 

        e4 = Label(top7,width=15, text=p[4]) 
        e4.grid(row=i, column=4)

        e5 = Label(top7,width=15, text=p[5]) 
        e5.grid(row=i, column=5)

        e6 = Label(top7,width=15, text=p[6]) 
        e6.grid(row=i, column=6)

        e7 = Label(top7,width=15, text=p[7]) 
        e7.grid(row=i, column=7)
        
        e8 = Label(top7,width=15, text=p[8]) 
        e8.grid(row=i, column=8)
       
        i=i+1
    mycon.commit() 

    cahl55= Button(top7, text="BACK", font = "Verdana 10 bold",command=top7.destroy).place(x=15,y=450)
    
    top7.mainloop()

def patientclinic():

    top8=Toplevel(tkWindow)
    top8.geometry('400x200')
    top8.title('Patient registration section')

    addp= Button(top8, text="Add patient",command=addpatient,height="4",width="30",bg="green", font = "Verdana 10 bold").place(x=15,y=15)
    listp=Button(top8,text="Patient List",height="4",width="30",bg="green", font = "Verdana 10 bold",command=sp).place(x=15,y=90)
        
    top8.mainloop()

def appointmentclinic():

    top9=Toplevel(tkWindow)
    top9.geometry('400x200')
    top9.title('Patient registration section')

    addappontment=Button(top9,text="Add Appointment",height="4",width="30",bg="green", font = "Verdana 10 bold",command=addapt).place(x=15,y=15)
    listappontment=Button(top9,text="Appointment List",height="4",width="30",bg="green", font = "Verdana 10 bold",command=listapts).place(x=15,y=90)
            

    top9.mainloop()

def billclinic():

    top10=Toplevel(tkWindow)
    top10.geometry('400x200')
    top10.title('Patient registration section')

    generatebill=Button(top10,text="Generate Bill",height="4",width="30",bg="green", font = "Verdana 10 bold",command=genratebill).place(x=15,y=15)
    Billist=Button(top10,text="Bill List",height="4",width="30",bg="green", font = "Verdana 10 bold",command=listbill).place(x=15,y=90)
                
    top10.mainloop()

def signin(username, password):
    if (username.get()=="clinic" and password.get()=="123456"):
        
        top11=Toplevel(tkWindow)
        top11.geometry('800x500')
        top11.title('CNS Clinic')
        
        mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="clinic")
        
        cur=mycon.cursor()
        query="select count(*) from patient;"
        cur.execute(query)
        tdata=cur.fetchall()
        print(tdata)
        cur.close()
        cur=mycon.cursor()
        query="select count(*) from appointment;"
        cur.execute(query)
        tdata2=cur.fetchall()
        print(tdata2)
        cur.close()

        head=Label(top11,text="<<<<MENU>>>>",height="4",width="30",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=15,y=15)
        

        head1=Label(top11,text="Total Patient Register",height="5",width="30",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=400,y=80)
        label1=Label(top11,text=tdata,width="30",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=400,y=150)
        p_reg=Button(top11,text="More info -->",height="1",width="30",bg="green", font = "Verdana 10 bold",command=sp).place(x=400,y=170)
        
        head2=Label(top11,text="Today's Appointment",height="5",width="30",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=400,y=220)
        label2=Label(top11,text=tdata2,width="30",fg = "white", bg = "green", font = "Verdana 10 bold").place(x=400,y=270)
        a_reg=Button(top11,text="More info -->",height="1",width="30",bg="green", font = "Verdana 10 bold",command=listapts).place(x=400,y=300)
        
        patientreg=Button(top11,text="Patient Registration",height="4",width="30",bg="green", font = "Verdana 10 bold",command=patientclinic).place(x=15,y=90)
        appointmentreg=Button(top11,text="appointment Registration",height="4",width="30",bg="green", font = "Verdana 10 bold",command=appointmentclinic).place(x=15,y=180)
        billreg=Button(top11,text="billing section",height="4",width="30",bg="green", font = "Verdana 10 bold",command=billclinic).place(x=15,y=270)
        cahl99= Button(top11, text="Sign Out", font = "Verdana 10 bold",command=top11.destroy).place(x=15,y=450)
        top11.mainloop()
    else:
        messagebox.showerror("SOMETHING WENT WRONG......")


tkWindow.geometry('800x500')
tkWindow.title(' CLINIC LOGIN')

clinic = Label(tkWindow,text="CLINIC",fg = "black", bg = "white", font = "Verdana 50 bold").place(x=250,y=100)


usernameLabel = Label(tkWindow, text="Username",fg = "black", bg = "white", font = "Verdana 10 bold").place(x=250,y=250)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).place(x=400,y=250)

passwordLabel22 = Label(tkWindow,text="Password",fg = "black", bg = "white", font = "Verdana 10 bold").place(x=250,y=300)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').place(x=400,y=300)  

sign_in = partial(signin, username, password)

loginButton = Button(tkWindow, text="Sign in",font = "Verdana 10 bold",command=sign_in).place(x=250,y=350)

tkWindow.mainloop()
