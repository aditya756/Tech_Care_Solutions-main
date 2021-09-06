from tkinter import *
from tkinter.simpledialog import askstring
import tkinter.messagebox
import pyrebase
from fpdf import FPDF
from datetime import date

#Firebase Configuration---------------------------------------------------------------------
config={
    "apiKey": "AIzaSyBCN51h67sT_3BCpaNSKNLzerOCxdseP4Y",
    "authDomain": "hospital-199fc.firebaseapp.com",
    "databaseURL": "https://hospital-199fc-default-rtdb.firebaseio.com",
    "projectId": "hospital-199fc",
    "storageBucket": "hospital-199fc.appspot.com",
    "messagingSenderId": "539786147277",
    "appId": "1:539786147277:web:be627abbf2a53d92b80084",
    "measurementId": "G-HHX9X0MVTH"
  }
#-------------------------------------------------------------------------------------------

#Initialize Firebase------------------------------------------------------------------------
global db
firebase = pyrebase.initialize_app(config)
db=firebase.database()
#------------------------------------------------------------------------------------------

#Functions----------------------------------------------------------------------------------
def down_pres():
    global db
    user=askstring('Unique Id','Your Unique Id')
    pes=(db.child(user).child("Prescription").get()).val()
    year=(str(pes[-1]["Date"]).split("-"))[-1]
    name=(db.child(user).child("Name").get()).val()
    age=int(year)-int((db.child(user).child("Age").get()).val())
    sex=(db.child(user).child("Sex").get()).val()
    doc=pes[-1]["Doctor"]
    dat=pes[-1]["Date"]
    
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",'B',25)

    pdf.image('/home/anurag/Documents/NIIT University/Semester-IV/Computer Architechture/HackNU3.0/Python Scripts/Patient Interface/rx.jpg',x=10,y=10,w=25,h=25)
    pdf.cell(200, 10, txt="PRESCRIPTION", ln=1, align='C')
    pdf.set_font("Arial",'B',20)
    pdf.cell(200, 10, txt='  ',ln=2,align='L')
    pdf.cell(200, 10, txt='_______________________________________________',ln=3,align='L')
    pdf.cell(200, 10, txt = "Doctor: "+str(doc),ln = 4, align = 'L')
    pdf.set_font("Arial", size = 13)
    pdf.cell(200, 10, txt = "Name: "+str(name), ln=5, align='L') 
    pdf.cell(200, 10, txt = "Age:"+str(age)+"                                             Sex:"+str(sex), ln=6, align='L')
    pdf.cell(200, 10, txt="Date: "+str(dat), ln=7, align='L')
    pdf.cell(200, 10, txt="Place: "+str(pes[-1]["place"]), ln=8, align='L')
    pdf.cell(200, 10, txt = "________________________________________________________________________", ln=6, align='L') 
    pdf.cell(200, 10, txt="Diagnosis: "+str(pes[-1]["Diagnosis"]), ln=9, align='L')
    pdf.cell(200, 10, txt="Medication: ", ln=10, align='L')
    for i in range(1,len(pes[-1]["Medication"])):
        pdf.cell(200, 10, txt="     "+str(pes[-1]["Medication"][i]).capitalize(), ln=8+i, align='L')
    
    title=str(name)+str(dat)+".pdf"
    pdf.output(title)
    tkinter.messagebox.showinfo("Successful", "Prescription Saved Successfully!")

def gen_tic():
    global db
    user=askstring('Unique Id','Your Unique Id')
    d=date.today()
    d=str(d).split("-")
    dat=str(d[2])+"-"+str(d[1])+"-"+str(d[0])
    temp_dic={
        "Date":dat,
        "Diagnosis":"Nill",
        "Doctor":"Nill",
        "Medication":[None],
        "place:":"Nill",
        "Status":"Nill"
    }
    pes_no=(db.child(user).child("Prescription").shallow().get()).val()
    pes_no=list(pes_no)
    pes_no=int(pes_no[-1])+1
    db.child(user).child("Prescription").child(pes_no).set(temp_dic)
    tkinter.messagebox.showinfo("Successful", "Ticket is Successfully Generated!")

def reg():
    gen=["-select-","M","F"]
    m=Tk()
    m.geometry("600x300")
    m.title("Registration Form")
    mlabel=Label(m, text="Registration Form", bg='white', font=('consolas', 20, 'bold'),fg='red')
    mlabel.pack(side=TOP)
    m.config(background='white')
    sx=StringVar(m)
    sx.set(gen[0])

    nlabel=Label(m,text="Name",font=('consolas', 15, 'bold'),bg="white")
    nlabel.place(x=10,y=50)
    name=Entry(m,bd=5,bg='slategray1',width=35,font=('consolas', 15, 'bold'))
    name.place(x=150,y=50)
    dlabel=Label(m,text="Birth Year",font=('consolas', 15, 'bold'),bg="white")
    dlabel.place(x=10,y=100)
    year=Entry(m,bd=5,bg='slategray1',width=35,font=('consolas', 15, 'bold'))
    year.place(x=150,y=100)
    plabel=Label(m,text="Phone",font=('consolas', 15, 'bold'),bg="white")
    plabel.place(x=10,y=150)
    ph=Entry(m,bd=5,bg='slategray1',width=35,font=('consolas', 15, 'bold'))
    ph.place(x=150,y=150)
    slabel=Label(m,text="Sex",font=('consolas', 15, 'bold'),bg="white")
    slabel.place(x=10,y=200)
    sex=OptionMenu(m,sx,*gen)
    sex.config(bg='slategray1',width=35,bd=4,font=("consolas",14,'bold'),relief='sunken')
    sex.place(x=150,y=200)
    
    def click_reg():
        users=(db.shallow().get()).val()
        users=list(users)
        uname=[str((db.child(x).child("Name").get().val())) for x in users]
        nm=name.get()
        s=sx.get()
        yr=year.get()
        phn=ph.get()
        if nm in uname:
            tkinter.messagebox.showinfo("Error!", "Already Registered!")
        else:
            ind=users[-1]
            ind=int(ind[2:])
            ind=ind+1
            n=3-len(str(ind))
            uid="AA"
            for i in range(n):
                uid+="0"
            uid=uid+str(ind)
            temp_data={
                "Name":nm,
                "Age":yr,
                "Phone":phn,
                "Sex":s,
                "Prescription":{},
                "History":{}
            }
            db.child(uid).set(temp_data)
            m.destroy()
            tkinter.messagebox.showinfo("Successful", "Your Unique id is "+str(uid))
    reg_But=Button(m,padx=10,pady=3,bd=4,bg='royalblue1',text="Register",font=("Courier New",15,'bold'),width=10,command=click_reg)
    reg_But.place(x=250,y=250)

    mainloop()
#-------------------------------------------------------------------------------------------

#Initialize---------------------------------------------------------------------------------
app=Tk()
app.geometry('400x210')
app.title('The Bug Slayers')
mlabel=Label(app, text="Tech-Care", bg='white', font=('consolas', 24, 'bold'),fg='green')
mlabel.pack(side=TOP)
app.config(background='white')
#-------------------------------------------------------------------------------------------

#Initial Screen-----------------------------------------------------------------------------
butreg=Button(app,padx=10,pady=3,bd=4,bg='royalblue1',text="Register",font=("Courier New",18,'bold'),width=25,command=reg)
butreg.place(x=10,y=50)
butgen=Button(app,padx=10,pady=3,bd=4,bg='royalblue1',text="Generate Ticket",font=("Courier New",18,'bold'),width=25,command=gen_tic)
butgen.place(x=10,y=100)
butpes=Button(app,padx=10,pady=3,bd=4,bg='royalblue1',text="Download Prescription",font=("Courier New",18,'bold'),width=25,command=down_pres)
butpes.place(x=10,y=150)
#-------------------------------------------------------------------------------------------


app.mainloop()
