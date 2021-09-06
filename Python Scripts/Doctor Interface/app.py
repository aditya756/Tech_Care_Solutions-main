from tkinter import *
from tkinter.simpledialog import askstring
import tkinter.messagebox
import tkinter.scrolledtext as st
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
#-------------------------------------------------------------------------------------------

#Initialize---------------------------------------------------------------------------------
app=Tk()
app.geometry('400x210')
app.title('The Bug Slayers')
mlabel=Label(app, text="Tech-Care", bg='white', font=('consolas', 24, 'bold'),fg='green')
mlabel.pack(side=TOP)
app.config(background='white')
#-------------------------------------------------------------------------------------------

#Functions----------------------------------------------------------------------------------
def his():
    status=["-select-","yes","no"]
    global db
    user=askstring('Unique Id','Patient Unique Id')

    m=Tk()
    m.geometry("520x930")
    m.title("Update History")
    mlabel=Label(m, text="History", bg='white', font=('consolas', 20, 'bold'),fg='red')
    mlabel.pack(side=TOP)
    m.config(background='white')

    blv=StringVar(m)
    blv.set(status[0])
    pld=StringVar(m)
    pld.set(status[0])
    plu=StringVar(m)
    plu.set(status[0])
    stp=StringVar(m)
    stp.set(status[0])

    diablabel=Label(m, text="Diabetes Management",bg='white', font=('consolas', 17, 'bold'))
    diablabel.place(x=10,y=50)
    bvlabel=Label(m,text="Blur Vision",font=('consolas', 15, 'bold'),bg="white")
    bvlabel.place(x=10,y=80)
    bv=OptionMenu(m,blv,*status)
    bv.config(bg='slategray1',width=28,bd=4,font=("consolas",14,'bold'),relief='sunken')
    bv.place(x=150,y=80)
    pdlabel=Label(m,text="Polydipsia",font=('consolas', 15, 'bold'),bg="white")
    pdlabel.place(x=10,y=130)
    pd=OptionMenu(m,pld,*status)
    pd.config(bg='slategray1',width=28,bd=4,font=("consolas",14,'bold'),relief='sunken')
    pd.place(x=150,y=130)
    pulabel=Label(m,text="Polyuria",font=('consolas', 15, 'bold'),bg="white")
    pulabel.place(x=10,y=180)
    pu=OptionMenu(m,plu,*status)
    pu.config(bg='slategray1',width=28,bd=4,font=("consolas",14,'bold'),relief='sunken')
    pu.place(x=150,y=180)
    splabel=Label(m,text="Stupor",font=('consolas', 15, 'bold'),bg="white")
    splabel.place(x=10,y=230)
    sp=OptionMenu(m,stp,*status)
    sp.config(bg='slategray1',width=28,bd=4,font=("consolas",14,'bold'),relief='sunken')
    sp.place(x=150,y=230)

    ams=StringVar(m)
    ams.set(status[0])
    cfs=StringVar(m)
    cfs.set(status[0])
    ltg=StringVar(m)
    ltg.set(status[0])
    szr=StringVar(m)
    szr.set(status[0])
    snl=StringVar(m)
    snl.set(status[0])

    ngsblabel=Label(m, text="Neuroglycopenic Symptoms",bg='white', font=('consolas', 17, 'bold'))
    ngsblabel.place(x=10,y=280)
    amlabel=Label(m,text="Amnesia",font=('consolas', 15, 'bold'),bg="white")
    amlabel.place(x=10,y=330)
    am=OptionMenu(m,ams,*status)
    am.config(bg='slategray1',width=28,bd=4,font=("consolas",14,'bold'),relief='sunken')
    am.place(x=150,y=330)
    cflabel=Label(m,text="Confusion",font=('consolas', 15, 'bold'),bg="white")
    cflabel.place(x=10,y=380)
    cf=OptionMenu(m,cfs,*status)
    cf.config(bg='slategray1',width=28,bd=4,font=("consolas",14,'bold'),relief='sunken')
    cf.place(x=150,y=380)
    lglabel=Label(m,text="Lethargy",font=('consolas', 15, 'bold'),bg="white")
    lglabel.place(x=10,y=430)
    lg=OptionMenu(m,ltg,*status)
    lg.config(bg='slategray1',width=28,bd=4,font=("consolas",14,'bold'),relief='sunken')
    lg.place(x=150,y=430)
    szlabel=Label(m,text="Seizures",font=('consolas', 15, 'bold'),bg="white")
    szlabel.place(x=10,y=480)
    sz=OptionMenu(m,szr,*status)
    sz.config(bg='slategray1',width=28,bd=4,font=("consolas",14,'bold'),relief='sunken')
    sz.place(x=150,y=480)
    sllabel=Label(m,text="Somnolence",font=('consolas', 15, 'bold'),bg="white")
    sllabel.place(x=10,y=530)
    sl=OptionMenu(m,snl,*status)
    sl.config(bg='slategray1',width=28,bd=4,font=("consolas",14,'bold'),relief='sunken')
    sl.place(x=150,y=530)

    agt=StringVar(m)
    agt.set(status[0])
    dph=StringVar(m)
    dph.set(status[0])
    ism=StringVar(m)
    ism.set(status[0])
    ppt=StringVar(m)
    ppt.set(status[0])
    tmr=StringVar(m)
    tmr.set(status[0])

    spsblabel=Label(m, text="Sympathomimetic Symptoms",bg='white', font=('consolas', 17, 'bold'))
    spsblabel.place(x=10,y=580)
    atlabel=Label(m,text="Agitation",font=('consolas', 15, 'bold'),bg="white")
    atlabel.place(x=10,y=630)
    at=OptionMenu(m,agt,*status)
    at.config(bg='slategray1',width=28,bd=4,font=("consolas",14,'bold'),relief='sunken')
    at.place(x=150,y=630)
    dplabel=Label(m,text="Diaphoresis",font=('consolas', 15, 'bold'),bg="white")
    dplabel.place(x=10,y=680)
    dp=OptionMenu(m,dph,*status)
    dp.config(bg='slategray1',width=28,bd=4,font=("consolas",14,'bold'),relief='sunken')
    dp.place(x=150,y=680)
    inslabel=Label(m,text="Insomnia",font=('consolas', 15, 'bold'),bg="white")
    inslabel.place(x=10,y=730)
    ins=OptionMenu(m,ism,*status)
    ins.config(bg='slategray1',width=28,bd=4,font=("consolas",14,'bold'),relief='sunken')
    ins.place(x=150,y=730)
    pplabel=Label(m,text="Palpitation",font=('consolas', 15, 'bold'),bg="white")
    pplabel.place(x=10,y=780)
    pp=OptionMenu(m,ppt,*status)
    pp.config(bg='slategray1',width=28,bd=4,font=("consolas",14,'bold'),relief='sunken')
    pp.place(x=150,y=780)
    trlabel=Label(m,text="Tremor",font=('consolas', 15, 'bold'),bg="white")
    trlabel.place(x=10,y=830)
    tr=OptionMenu(m,tmr,*status)
    tr.config(bg='slategray1',width=28,bd=4,font=("consolas",14,'bold'),relief='sunken')
    tr.place(x=150,y=830)
    
    def click_upt():
        #Diabetes Management
        bvs=str(blv.get())
        pds=str(pld.get())
        pua=str(plu.get())
        spr=str(stp.get())
        dia_data={
            'Blurred vision':bvs,
            'Polydipsia':pds,
            'Polyuria': pua,
            'Stupor':spr
        }
        #Neuroglycopenic Symptoms
        amn=str(ams.get())
        cfu=str(cfs.get())
        lth=str(ltg.get())
        sez=str(szr.get())
        sml=str(snl.get())
        ns_data={
            'Amnesia':amn,
            'Confusion':cfu,
            'Lethargy':lth,
            'Seizures':sez,
            'Somnolence':sml
        }
        #Sympathomimetic Sysptoms
        agn=str(agt.get())
        dip=str(dph.get())
        inm=str(ism.get())
        pal=str(ppt.get())
        tre=str(tmr.get())
        Sy_data={
            'Agitation':agn,
            'Diaphoresis':dip,
            'Insomnia':inm,
            'Palpitations':pal,
            'Tremor':tre
        }
        db.child(user).child('History').child('Diabetes Management').set(dia_data)
        db.child(user).child('History').child('Neuroglycopenic Symptoms').set(ns_data)
        db.child(user).child('History').child('Sympathomimetic Symptoms').set(Sy_data)
        m.destroy()
        tkinter.messagebox.showinfo("Successful", "History Updation Successfull!")

    upt_But=Button(m,padx=10,pady=3,bd=4,bg='royalblue1',text="Update",font=("Courier New",15,'bold'),width=10,command=click_upt)
    upt_But.place(x=190,y=880)

    mainloop()

def pescribe():
    status=["-select-","General","Restricted"]
    global db
    user=askstring('Unique Id','Patient Unique Id')
    pes_no=(db.child(user).child("Prescription").shallow().get()).val()
    pes_no=list(pes_no)
    pes_no=pes_no[-1]
    nm=str((db.child(user).child("Name").get()).val())
    pes=(db.child(user).child("Prescription").get()).val()
    year=(str(pes[-1]["Date"]).split("-"))[-1]
    age=int(year)-int((db.child(user).child("Age").get()).val())
    sex=str((db.child(user).child("Sex").get()).val())
    dat=str(pes[-1]["Date"])

    m=Tk()
    m.geometry("600x480")
    m.title("Prescription")
    mlabel=Label(m, text="Prescription", bg='white', font=('consolas', 20, 'bold'),fg='red')
    mlabel.pack(side=TOP)
    m.config(background='white')
    st=StringVar(m)
    st.set(status[0])

    nlabel=Label(m,text="Name",font=('consolas', 15, 'bold'),bg="white")
    nlabel.place(x=10,y=50)
    name=Label(m,text=nm,font=('consolas', 15, 'bold'),bg="white")
    name.place(x=150,y=50)
    dlabel=Label(m,text="Age",font=('consolas', 15, 'bold'),bg="white")
    dlabel.place(x=10,y=80)
    year=Label(m,text=str(age),font=('consolas', 15, 'bold'),bg="white")
    year.place(x=150,y=80)
    slabel=Label(m,text="Sex",font=('consolas', 15, 'bold'),bg="white")
    slabel.place(x=10,y=110)
    sx=Label(m,text=sex,font=('consolas', 15, 'bold'),bg="white")
    sx.place(x=150,y=110)
    slabel=Label(m,text="Date",font=('consolas', 15, 'bold'),bg="white")
    slabel.place(x=10,y=140)
    sx=Label(m,text=dat,font=('consolas', 15, 'bold'),bg="white")
    sx.place(x=150,y=140)
    ndlabel=Label(m,text="Doctor",font=('consolas', 15, 'bold'),bg="white")
    ndlabel.place(x=10,y=170)
    doc=Entry(m,bd=5,bg='slategray1',width=35,font=('consolas', 15, 'bold'))
    doc.place(x=150,y=170)
    dialabel=Label(m,text="Diagnosis",font=('consolas', 15, 'bold'),bg="white")
    dialabel.place(x=10,y=220)
    diag=Entry(m,bd=5,bg='slategray1',width=35,font=('consolas', 15, 'bold'))
    diag.place(x=150,y=220)
    plabel=Label(m,text="Place",font=('consolas', 15, 'bold'),bg="white")
    plabel.place(x=10,y=270)
    place=Entry(m,bd=5,bg='slategray1',width=35,font=('consolas', 15, 'bold'))
    place.place(x=150,y=270)
    stlabel=Label(m,text="Status",font=('consolas', 15, 'bold'),bg="white")
    stlabel.place(x=10,y=320)
    sts=OptionMenu(m,st,*status)
    sts.config(bg='slategray1',width=35,bd=4,font=("consolas",14,'bold'),relief='sunken')
    sts.place(x=150,y=320)
    mdlabel=Label(m,text="Medication",font=('consolas', 15, 'bold'),bg="white")
    mdlabel.place(x=10,y=370)
    med=Entry(m,bd=5,bg='slategray1',width=35,font=('consolas', 15, 'bold'))
    med.place(x=150,y=370)

    def click_pes():
        dia=str(diag.get())
        doctor=str(doc.get())
        pl=str(place.get())
        stat=str(st.get())
        meds=str(med.get()).split(",")
        medic=[None]+meds
        temp_data={
            "Date":dat,
            "Diagnosis":dia,
            "Doctor":doctor,
            "Medication":medic,
            "place":pl,
            "Status":stat
        }
        db.child(user).child("Prescription").child(pes_no).set(temp_data)
        m.destroy()
        tkinter.messagebox.showinfo("Successful", "Prescription is Successfully Uploaded!")

    pes_But=Button(m,padx=10,pady=3,bd=4,bg='royalblue1',text="Upload",font=("Courier New",15,'bold'),width=10,command=click_pes)
    pes_But.place(x=250,y=420)
    
    mainloop()

def hp():
    gen_pass="TBS123"
    res_pass="STF987"
    global db
    user=askstring('Unique Id','Patient Unique Id')
    k=askstring('Password','Enter Password')
    data_his_dia=dict((db.child(user).child('History').child('Diabetes Management').get()).val())
    data_his_ns=dict((db.child(user).child('History').child('Neuroglycopenic Symptoms').get()).val())
    data_his_ss=dict((db.child(user).child('History').child('Sympathomimetic Symptoms').get()).val())
    data_pes=list((db.child(user).child('Prescription').shallow().get()).val())
    m=Tk()
    m.geometry("900x900")
    m.title("History & Prescription")
    mlabel=Label(m, text="History & Prescription", bg='white', font=('consolas', 20, 'bold'),fg='red')
    mlabel.pack(side=TOP)
    m.config(background='white')

    T=st.ScrolledText(m,height=800,width=800)
    T.pack()

    his_dat="History\n\n"+"Diabetes Management\n"
    for key, value in data_his_dia.items():
        his_dat+=str(key)+":"+str(value)+"\n"
    his_dat+='\nNeuroglycopenic Symptoms\n'
    for key, value in data_his_ns.items():
        his_dat+=str(key)+":"+str(value)+"\n"
    his_dat+='\nSympathomimetic Symptoms\n'
    for key, value in data_his_ss.items():
        his_dat+=str(key)+":"+str(value)+"\n"
    for i in data_pes:
        temp_pes=dict((db.child(user).child('Prescription').child(i).get()).val())
        if temp_pes['Status']=='Restricted' and k==res_pass:
            his_dat+="\nPrescription"+str(i)+"\n"
            for key, value in temp_pes.items():
                if key=="Medication":
                    value=value[1:]
                his_dat+=str(key)+":"+str(value)+"\n"
        if temp_pes['Status']=='General':
            his_dat+="\nPrescription"+str(i)+"\n"
            for key, value in temp_pes.items():
                if key=="Medication":
                    value=value[1:]
                his_dat+=str(key)+":"+str(value)+"\n"

            
    T.insert(END,his_dat)
    

    mainloop()
        

#Initial Screen-----------------------------------------------------------------------------
butreg=Button(app,padx=10,pady=3,bd=4,bg='royalblue1',text="Update History",font=("Courier New",18,'bold'),width=25,command=his)
butreg.place(x=10,y=50)
butgen=Button(app,padx=10,pady=3,bd=4,bg='royalblue1',text="Prescribe",font=("Courier New",18,'bold'),width=25,command=pescribe)
butgen.place(x=10,y=100)
butpes=Button(app,padx=10,pady=3,bd=4,bg='royalblue1',text="History & Prescriptions",font=("Courier New",18,'bold'),width=25,command=hp)
butpes.place(x=10,y=150)
#-------------------------------------------------------------------------------------------

app.mainloop()
