from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter.messagebox
from datetime import date
from tkinter import filedialog
import shutil 
import os
from tkinter import Text,Tk
#import TkTreectrl as treect

today = date.today()
print ("Software is Running.....")
firstw = Tk()
firstw.title("Hospital Management System")
firstw.geometry("1600x1000")
label = Label(text = "Hospital Management System", font = ("times new roman",35) ,bg = "MediumOrchid2")
label.place(side = "top",fill = X )
user1 = Label(text = "USERNAME",font = ("arial",23))
user1.place(x=610,y=120)
user = Entry(width=17,bd=5,font=("arial",20))
user.place(x=570,y=200)
label.place(side = "top",fill = X)
user2 = Label(text="PASSWORD",font=("arial",23))
user2.place(x=610,y=280)
user3 = Entry(width=17,show="*",bd=5,font=("arial",20))
user3.place(x=570,y=360)

def second():
    global secondw
    secondw=Tk()
    secondw.title("Hospital Management Sysyem")
    secondw.geometry("1600*1000")
    def distroy4():
        secondw.destroy()
        root()

    def patientwindow():
        thirdw=Tk()
        thirdw.title("PATIENT WINDOW")
        thirdw.geometry("1600*1000") 

    



    def distroy5():
        secondw.destroy()
        patientwindow()

    def about():
        about=Tk()
        about.title("ABOUT WINDOW")
        about.geometry("1600*1000")


    def aboutwindow():
        about=Tk()
        about.title("Hospital Management System")
        about.geometry("1600*1000")
        def back():
            about.destroy()
            second()

    def appointmentwindow():
        fourthw=Tk()
        fourthw.title("APPOINTMENT WINDOW")
        fourthw.geometry("1600*1000")

    def back():
        back=Tk()


        label1 = Label(about,text="DEVELOPER 1",font=("bold",20))
        label1.place(x=100,y=100)
        label1 = Label(about,text="Pankaj",font=("bold",15))
        label1.place(x=100,y=150)
        label1 = Label(about,text="0501ca091044",font=("bold",15))
        label1.place(x=100,y=200)
        label1 = Label(about,text="DEVELOPER 2",font=("bold",20))
        label1.place(x=350,y=100)
        label1 = Label(about,text="Dolly",font=("bold",15))
        label1.place(x=350,y=150)
        label1 = Label(about,text="0501ca091047",font=("bold",15))
        label1.place(x=350,y=200)
        label2 = Label(about,text="BACK",width=15,command=back)
        label2.place(x=0,y=0)

    about.mainloop() 

    mainlabel = Label(secondw,text="ADMIN PANEL",font=("times new roman",35),bg="MediumOrchid2")
    mainlabel.place(side=TOP,fill=X)
    button = Button(secondw,width=15,font=("arial",20),text="DOCTOR",bg="MediumOrchid2",command=distroy4)
    button.place(x=170,y=200)
    enquiry = Button(secondw,width=15,font=("arial",20),text="PATIENT",bg="MediumOrchid2",command=distroy5)
    enquiry.place(x=750,y=280)
    fee_details = Button(secondw,width=15,font=("arial",20),text="APPOINTMENT",bg="MediumOrchid2",command=appointmentwindow)
    fee_details.place(x=170,y=480)
    viewenquiry = Button(secondw,width=15,font=("arial",20),text="ABOUT US",bg="MediumOrchid2",command=aboutwindow)
    viewenquiry.place(x=750,y=480)

def distroy():
    firstw.destroy()
def login():
    if user.get() == "admin" and user3.get() == "admin" :
        second()
        distroy()
    else :
        t = tkinter.messagebox.showinfo("INVALID USERNAME OR PASSWORD" , "YOU HAVE ENTERED INVALID USERNAME OR PASSWORD")
        user.delete(0,END)
        user3.delete(0,END)

def root():
    root = Tk()
    root.geometry("1600x1000")
    root.title("HOSPITAL MANAGEMENT SYSTEM")
    global entry1
    global entry2
    global entry3 
    global entry4

    global name 
    name = StringVar()
    global specialization
    specialization = StringVar()

    global contact
    contact =  StringVar()
    global rollno
    rollno = StringVar()

    id = IntVar()
    search = IntVar()

    NAME = name.get()
    SPECIALIZATION = specialization.get()
    CONTACT = contact.get()

    label = Label(root,text="MANAGE DOCTOR",font=("arial",25),bg="violetred1")
    label.place(side=TOP,fill=X)

    label1 = Label(root,text="NAME: ",font=("arial",17))
    label1.place(x=250,y=150)

    label2 = Label(root,text="SPECIALIZATION: ",font=("arial",17))
    label2.place(x=250,y=210)

    label3 = Label(root,text="CONTACT: ",font=("arial",17))
    label3.place(x=250,y=270)

root()