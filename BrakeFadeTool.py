#3.0{30/112020}
#==============================================================================================
from tkinter import*
from tkinter import messagebox
import tkinter.font as tkFont

#import serial
import time
import my_serial as ser

root = Tk()

sysdim = PhotoImage(file = 'images/_System data.png')
setim = PhotoImage(file = 'images/_   Settings.png')
conim = PhotoImage(file = 'images/small_confirm.png')
startim = PhotoImage(file = 'images/_    Initiate.png')
#==============================================================================================

'''def Confirm():
    label4["text"]=entry2.get()
    label6["text"]=entry3.get()
    with open("DataExp.txt", "w") as text_file:
       text_file.write("vehicle category :" + entry2.get()+ '\n')
       text_file.write("Date :" + entry3.get()+ '\n')'''

#==============================================================================================

def start():
    
    '''msg = ser.get_message(ser1)
    if msg != None:
        msg1 = msg[1:-1]
        result = ser.parse_message(msg1)
        print(result)
        print(result[0])

    root.after(50, start)'''


#==============================================================================================

def sysdata():
    sysdata = Toplevel()
    #photo = PhotoImage(file = "C:\\Users\\yaron\Desktop\\python examples\\matmon.ico")
    photo = PhotoImage(file = "images/matmon.ico")
    sysdata.iconphoto(False, photo)
    sysdata.geometry('600x400+650+400')
    sysdata.resizable(width=False,height=False)
    sysdata.attributes('-alpha',1)
    sysdata.title('System Data')
    '''#P = Canvas(sysdata, bg="blue", height=210, width=0)
    img = PhotoImage(file = 'C:\\Users\\yaron\Desktop\\python examples\\resized_window.png')
    background_label = Label(sysdata, image=img)
    #background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image=img
    background_label.pack()

    #P.pack()'''


    Label(sysdata,text='System Data',font='calibri 22', fg='black').place(x=220, y=0)
    Label(sysdata,text='Raspberry pi Temp:',font='calibri 17', fg='black').place(x=20, y=40)
    Label(sysdata,text='Version 2.0.1',font='calibri 17', fg='black').place(x=20, y=340)

#==============================================================================================

def opensettings():

    settings = Toplevel()
    photo = PhotoImage(file ="images/matmon.ico")
    settings.iconphoto(False, photo)
    settings.geometry('600x400+650+400')
    settings.resizable(width=False,height=False)
    settings.attributes('-alpha',1)
    settings.title('Settings')
    P = Canvas(settings, bg="blue", height=210, width=0)
    img = PhotoImage(file = 'images/resized_window.png')
    background_label = Label(settings, image=img)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    P.pack()
    def Confirm():
     label4["text"]=entry2.get()
     label6["text"]=entry3.get()
     label15["text"]=entry6.get()
     with open("DataExp.txt", "w") as text_file:
       text_file.write("vehicle category :" + entry2.get()+ '\n')
       text_file.write("Date :" + entry3.get()+ '\n')
       text_file.write("delta between measurments:" + entry6.get()+ '\n')

    Label(settings,text='Settings',font='calibri 22', fg='black').place(x=240, y=0)
    Label(settings,text='Units( g | m/s^2 ) :',font='calibri 17', fg='black').place(x=20, y=40)
    Label(settings,text=' Δ between measurments (ms):',font='calibri 17', fg='black').place(x=14, y=75)
    button6=Button(settings,text='  g  ',command=start,relief="groove")
    button6.place(x=260, y=46)
    button9=Button(settings,text=' m/s^2 ',command=start,relief="groove")
    button9.place(x=300, y=46)
    #button10=Button(settings,text='✓',command=start,relief="groove")
    #button10.place(x=490, y=78)

    label5=Label(settings,text='vehicle category:',font='calibri 17', fg='black')
    label5.place(x=20, y=120)
    entry2=Entry(settings,font='calibri 16', fg='blue')
    entry2.place(x=260, y=120)
    label4=Label(settings,text="")
    label7=Label(settings,text='Date:',font='calibri 17', fg='black')
    label7.place(x=20, y=165)
    entry3=Entry(settings,font='calibri 16', fg='blue')
    entry3.place(x=260, y=165)
    label6=Label(settings,text="")
    entry6=Entry(settings,font='calibri 16', fg='black')
    entry6.place(x=260, y=76)
    label15=Label(settings,text="")

    button3=Button(settings,text='Confirm!',command=Confirm,image = conim)
    button3.place(x=20, y=300)


def read_next_msg():
    msg = ser.get_message(ser1)
    if msg != None:
        msg1 = msg[1:-1]
        result = ser.parse_message(msg1)
        print(result)
        print(result[0])

    root.after(50, read_next_msg)

#==============================================================================================
ser1 = ser.my_init_serial()



photo = PhotoImage(file ="images/matmon.ico")
root.iconphoto(False, photo)
root.geometry('1252x834+320+150')
C = Canvas(root, bg="blue", height=210, width=0)
#img = PhotoImage(file = 'C:\\Users\\yaron\Desktop\\python examples\\bgmatmombigger.png')
img = PhotoImage(file = 'images/bgmatmombigger.png')

background_label = Label(root, image=img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.place()

#==============================================================================================

"""label5=Label(root,text='vehicle category:',font='calibri 22', fg='black')
label5.place(x=170, y=165)
entry2=Entry(root,font='calibri 22', fg='blue')
entry2.place(x=380, y=166)
label4=Label(root,text="")
label7=Label(root,text='Date:',font='calibri 22', fg='black')
label7.place(x=305, y=222)
entry3=Entry(root,font='calibri 22', fg='blue')
entry3.place(x=380, y=223)
label6=Label(root,text="")"""

#==============================================================================================

#button3=Button(root,text='Confirm!',command=Confirm,relief="groove")
#button3.place(x=290, y=630)
#button3=Button(root,text='Confirm!',command=Confirm,image = conim)
#button3.place(x=168, y=450)
#button2=Button(root,text='Settings',command=opensettings,relief="groove")
#button2.place(x=470, y=630)
#button5=Button(root,text='System Data',command=sysdata,relief="groove")
#button5.place(x=372, y=630)
button5=Button(root,text='System Data',command=sysdata,image = sysdim)
button5.place(x=168, y=168)
button2=Button(root,text='Settings',command=opensettings,image = setim)
button2.place(x=168, y=270)
button1=Button(root,text='Start',command=start,image = startim)
button1.place(x=168, y=372)



#==============================================================================================

#x=root.winfo_screenwidth()
#y=root.winfo_screenheight()
#root.geometry(str(x)+'x'+str(y))
#root.geometry('{}x{}'.format(x,y))
#root.geometry(f'{x}x{y}')
root.title('Brake Fade Tool')
#root.overrideredirect(1)
root.resizable(width=False,height=False)
root.attributes('-alpha',1)
#w=Label(root,text="hello,world" ,bg="blue",fg="yellow")
#w.pack()
#img = PhotoImage(file='C:\\Users\\yaron\Desktop\\python examples\\matmon.png')
#label1 = Label(root,image=img)
#label1.pack()
#fnt=tkFont.Font(family="Helvetica",size=20,weight=tkFont.BOLD)
#label3 = Label(root,text="Matmon 5000",font=fnt)


#==============================================================================================
'''from tkinter import *

sensor_value =300.4 #said sensor value
master = Tk()
x = sensor_value #assigned to variable x like you showed
master.minsize(width=400, height=400)
w = Label(master, text=x) #shows as text in the window
w.pack() #organizes widgets in blocks before placing them in the parent.

mainloop()'''
#root.after(50,start)
root.after(50, read_next_msg)
root.mainloop()

