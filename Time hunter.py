# Bên dưới khai báo các thư viện cần dùng
from tkinter import *
from threading import *
from tkinter import ttk
from tkinter import messagebox
import pyttsx3
import datetime
import time
import winsound
 
window = Tk()
window.geometry("400x278+430+170")
window.title("Time Hunter")
window.iconbitmap('icon.ico')
# Make sure app can't be resized
window.resizable(width=False, height=False)
 
main_tab = ttk.Notebook(window)
main_tab.pack(expand=1, fill='both')
 
tab1 = Frame(main_tab)
tab2 = Frame(main_tab)
tab3 = Frame(main_tab)
 
main_tab.add(tab1, text='Countdown')
main_tab.add(tab2, text='Alarm')
main_tab.add(tab3, text='...')
#=================================================================================================
#=================================================================================================
# Các dòng code chung của tab 1 vs tab 2
# tạo nốt
notes = {'c':0, 'd':2, 'e':4, 'f':5, 'g':7, 'a':9, 'b':11}
robot_mouth = pyttsx3.init()
 
#độ dài 500
def play_note(note, duration=1000):
    winsound.Beep(int(256*(2**(notes[note]/12))), duration)
#=================================================================================================
 
# Code tab 1: Countdown
# Use Images as Backgrounds
# Define image
bg1 = PhotoImage(file= "space1.png")
# Create a label
## Define Label
my_label1 = Label(tab1, image=bg1)
## Add the entry boxes to the frame
my_label1.place(x=0, y=0,relwidth=1, relheight=1)
 
# Declaration of variables:
hh=StringVar()
mm=StringVar()
ss=StringVar()
 
# Define Entry Boxes
hh_Entry1= Entry(tab1, font=(18), width=3, fg="#336d92", bd=0, textvariable=hh)
mm_Entry1= Entry(tab1, font=(18), width=3, fg="#336d92", bd=0, textvariable=mm)
ss_Entry1= Entry(tab1, font=(18), width=3, fg="#336d92", bd=0, textvariable=ss)
reminder_Entry1= Entry(tab1, font=(18), width=8, fg="#336d92", bd=0)
ringtone_Entry1= Entry(tab1, font=(18), width=8, fg="#336d92", bd=0)
 
# Add the entry boxes to the frame
hh_Entry1.place(x=132,y=120)
mm_Entry1.place(x=179,y=120)
ss_Entry1.place(x=225,y=120)
reminder_Entry1.place(x=16,y=120)
ringtone_Entry1.place(x=290,y=120)
 
# setting the default value
hh.set("00")
mm.set("00")
ss.set("00")
reminder_Entry1.insert(0, "Wake up boy! Wake up boy!")
ringtone_Entry1.insert(0, "c d e c c d e c e f g e f g g a g f e c g a g f e c")
 
# Function
def Threading1():
    if  ringtone_Entry1.get() == "╰(°▽°)╯":
        ringtone_Entry1.delete(0,END)
        ringtone_Entry1.insert(0, 'c d e c c d e c e f g e f g g a g f e c g a g f e c')
    if  reminder_Entry1.get() == "╰(°▽°)╯":
        reminder_Entry1.delete(0,END)
        reminder_Entry1.insert(0, "Wake up boy! Wake up boy!")
    t1=Thread(target=dem_nguoc)
    t1.start()
 
def myClick1():
    ringtone_Entry1.delete(0,END)
    ringtone_Entry1.insert(0, "╰(°▽°)╯")
    reminder_Entry1.delete(0,END)
    reminder_Entry1.insert(0, "╰(°▽°)╯")
 
def dem_nguoc():
    try:
        temp = int(hh.get())*3600 + int(mm.get())*60 + int(ss.get())
    except:
        messagebox.showwarning("Oops…", "Please make sure to enter the correct format in the Time box.")
 
    while temp >-1 and ringtone_Entry1.get() != '╰(°▽°)╯':
        mins,secs = divmod(temp,60)
        hours=0
 
        if mins >60:
            hours, mins = divmod(mins, 60)
 
		hh.set(('%02d')%(hours))
		mm.set(('%02d')%(mins))
		ss.set(('%02d')%(secs))
 
        time.sleep(1)
 
        if (temp == 0):
            while True:  
                reminder = f"{reminder_Entry1.get()}"
                ringtone = f"{ringtone_Entry1.get()}"
               
                for note in ringtone:
                    if note.lower() in notes:
                        play_note(note.lower())
                    if ringtone_Entry1.get() == '╰(°▽°)╯':
                            break
 
                robot_mouth.say(reminder)
                robot_mouth.runAndWait()
 
                if ringtone_Entry1.get() == '╰(°▽°)╯':
                            break
 
        temp -= 1
 
# Create button
setButton1 = Button(tab1, text="Set", font=("Helvetiva", 10), width=8, height=1, fg="#336d92", command=Threading1)
quitButton1 = Button(tab1, text="Quit", font=("Helvetiva", 10), width=8, height=1, fg="#336d92", command=myClick1)
 
setButton1.place(x = 160,y = 166)
quitButton1.place(x=160, y=205)
#=====================================================================
# CODE TAB 2
bg2 = PhotoImage(file= "space2.png")
my_label2 = Label(tab2, image=bg2)
my_label2.place(x=0, y=0,relwidth=1, relheight=1)
 
# Define Entry Boxes
hh_Entry2= Entry(tab2, font=(18), width=3, fg="#336d92", bd=0)
mm_Entry2= Entry(tab2, font=(18), width=3, fg="#336d92", bd=0)
ss_Entry2= Entry(tab2, font=(18), width=3, fg="#336d92", bd=0)
reminder_Entry2= Entry(tab2,font=(18), width=8, fg="#336d92", bd=0)
ringtone_Entry2= Entry(tab2,font=(18), width=8, fg="#336d92", bd=0)
 
hh_Entry2.insert(0, "00")
mm_Entry2.insert(0, "00")
ss_Entry2.insert(0, "00")
reminder_Entry2.insert(0, "Wake up boy! Wake up boy!")
ringtone_Entry2.insert(0, "c d e c c d e c e f g e f g g a g f e c g a g f e c")
 
# Add the entry boxes to the frame
hh_Entry2.place(x=132,y=120)
mm_Entry2.place(x=179,y=120)
ss_Entry2.place(x=225,y=120)
reminder_Entry2.place(x=16,y=120)
ringtone_Entry2.place(x=290,y=120)
 
# Function
def Threading2():
    if  ringtone_Entry2.get() == "╰(°▽°)╯":
        ringtone_Entry2.delete(0,END)
        ringtone_Entry2.insert(0, 'c d e c c d e c e f g e f g g a g f e c g a g f e c')
    if  reminder_Entry2.get() == "╰(°▽°)╯":
        reminder_Entry2.delete(0,END)
        reminder_Entry2.insert(0, "Wake up boy! Wake up boy!")
    t1=Thread(target=alarm)
    t1.start()
 
def myClick2():
    ringtone_Entry2.delete(0,END)
    ringtone_Entry2.insert(0, "╰(°▽°)╯")
    reminder_Entry2.delete(0,END)
    reminder_Entry2.insert(0, "╰(°▽°)╯")
 
# Hàm chính của tab2
def alarm():
    # Infinite Loop
    try:
        temp = int(hh_Entry2.get())*3600 + int(mm_Entry2.get())*60 + int(ss_Entry2.get())
        tempt = temp - 1
    except:
        messagebox.showwarning(" Oops…", "Make sure you enter the correct format in the Time box.")
 
    if int(hh_Entry2.get()) >24 or int(hh_Entry2.get()) < 0:
        messagebox.showwarning(" Oops… ", "Make sure variable hour has value between 0 and 24 in the Time box.")
    elif int(mm_Entry2.get()) >60 or int(mm_Entry2.get()) < 0:
        messagebox.showwarning(" Oops… ", "Make sure variable minute has value between 0 and 60 in the Time box.")
    elif int(ss_Entry2.get()) >60 or int(ss_Entry2.get()) < 0:
        messagebox.showwarning(" Oops… ", "Make sure variable second has value between 0 and 60 in the Time box.")
    else:
        while tempt < temp and ringtone_Entry2.get() != '╰(°▽°)╯':
            # Set Alarm
            set_alarm_time = f"{hh_Entry2.get()}:{mm_Entry2.get()}:{ss_Entry2.get()}"
            # Wait for one seconds
            time.sleep(1)
     
            # Get current time
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time,set_alarm_time)
     
            # Check whether set alarm is equal to current time or not
            if current_time == set_alarm_time:
                while True:
                    reminder=f"{reminder_Entry2.get()}"
                    ringtone=f"{ringtone_Entry2.get()}"
                    # Playing sound              
                    for note in ringtone:
                        if note.lower() in notes:
                            play_note(note.lower())
                        if ringtone_Entry2.get() == '╰(°▽°)╯':
                            break
                    robot_mouth.say(reminder)
                    robot_mouth.runAndWait()
                    if ringtone_Entry2.get() == '╰(°▽°)╯':
                        tempt = temp
                        break
 
setButton2 = Button(tab2, text="Set", font=("Helvetiva", 10), width=8, height=1, fg="#336d92", command=Threading2)
quitButton2 = Button(tab2, text="Quit", font=("Helvetiva", 10), width=8, height=1, fg="#336d92", command=myClick2)
 
setButton2.place(x = 160,y = 166)
quitButton2.place(x=160, y=205)
#=======================================================
# Định dạng tab3 “ORION”, phần này mn hỏi Nhi nhớ
C = Canvas(tab3,bg='black',height=200, width=400)
   
C.pack()
def create_circle(x, y, r, canvasName): #center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1, fill= "white")
 
#  23*3600 + 56*60 + 4 = 86164.09053
#  x/400 = ((hiện tại - 0h 15/6/2012) % 23h 56m 4s) / 23h 56m 4s
def o():
    dt = datetime.datetime.now()
    dt2 = datetime.datetime(2012, 6, 15)
    td= dt - dt2
    x= (td.days*86400 + td.seconds)% 86164.09053/86164.09053*400
    y=100*10/9
    create_circle(x, y, 3, C)
    create_circle(x-8, y+4, 3, C)
    create_circle(x+8, y-5, 3, C)
 
setButton3 = Button(tab3, text="Set", font=("Helvetiva", 10), width=8, height=1, fg="#336d92", command=o)
setButton3.place(x = 160,y = 205)
 
window.mainloop()