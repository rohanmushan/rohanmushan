# create student information form using TKinter
# -name,address,email,schoolname,stding in,year,dob,gender,schooltype- Marathi medium,english,convent,semi


import tkinter as tk
from tkinter import *

win = tk.Tk()
win.geometry("500x500+500+150")

name = tk.Label(win,text="Name: ").place(x=30, y=50)
address = tk.Label(win,text="Address: ").place(x=30, y=80)
email = tk.Label(win,text="Email: ").place(x=30, y=110)
schoolname = tk.Label(win,text="School Name: ").place(x=30, y=140)
studyinginyear = tk.Label(win,text="Studying in Year: ").place(x=30, y=170)
dob = tk.Label(win,text="Date of Birth: ").place(x=30, y=200)
gender = tk.Label(win,text="Gender: ").place(x=30, y=230)
schooltype = tk.Label(win,text="School Type: ").place(x=30, y=310)

# Entry
ename = tk.Entry(win).place(x=150, y=50)
eadd = tk.Entry(win).place(x=150, y=80)
eemail = tk.Entry(win).place(x=150, y=110)
eschool = tk.Entry(win).place(x=150, y=140)
eyear = tk.Entry(win).place(x=150, y=170)
edob = tk.Entry(win).place(x=150, y=200)

# Gender Radio Buttons
selgender = StringVar()
male = tk.Radiobutton(win,text="Male",variable=selgender,value=1).place(x=150, y=230)
female = tk.Radiobutton(win,text="Female",variable=selgender,value=2).place(x=150, y=250)
other = tk.Radiobutton(win,text="Other",variable=selgender,value=3).place(x=150, y=270)

# School Type
selschool = StringVar()
marathi = tk.Radiobutton(win,text="Marathi Medium",variable=selschool,value=4).place(x=150, y=310)
english = tk.Radiobutton(win,text="English Medium",variable=selschool,value=5).place(x=150, y=330)
semi = tk.Radiobutton(win,text="Semi-english Medium",variable=selschool,value=6).place(x=150, y=350)
convent = tk.Radiobutton(win,text="Convent School",variable=selschool,value=7).place(x=150, y=370)

butt = tk.Button(win,text="Submit",activebackground="cyan",activeforeground="purple").place(x=150,y=420)


win.mainloop()