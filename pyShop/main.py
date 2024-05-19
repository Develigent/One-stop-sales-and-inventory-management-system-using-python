
import os
from tkinter import *
from tkinter import messagebox

main = Tk()
main.geometry("1366x768")
main.title("Big Bazaar")
main.resizable(0, 0)
def Exit():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=main)
    if sure == True:
        main.destroy()
        
main.protocol("WM_DELETE_WINDOW", Exit)

def emp():
    main.withdraw()
    os.system("python employee.py")
    main.deiconify()


def adm():
    main.withdraw()
    os.system("python admin.py")
    main.deiconify()

def credit():
    main.withdraw()
    os.system("python credit.py")
    main.deiconify()

label1 = Label(main)
label1.place(relx=0, rely=0, width=1366, height=768)
img = PhotoImage(file="./images/main.png")
label1.configure(image=img)

button1 = Button(main)
button1.place(relx=0.1, rely=0.57, width=260, height=80)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#ffffff")
button1.configure(cursor="hand2")
button1.configure(foreground="#ffffff")
button1.configure(background="#ffffff") # #fffff <- original valie for tranparency
button1.configure(borderwidth="0")#visibility of border 
img2 = PhotoImage(file="./images/1.png")
button1.configure(image=img2)
button1.configure(command=emp)

button2 = Button(main)
button2.place(relx=0.1, rely=0.448, width=260, height=80)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(activebackground="#ffffff")
button2.configure(cursor="hand2")
button2.configure(foreground="#ffffff")
button2.configure(background="#ffffff") # #fffff <- original valie for tranparency
button2.configure(borderwidth="0")#visibility of border

img3 = PhotoImage(file="./images/2.png")
button2.configure(image=img3)
button2.configure(command=adm)

button3 = Button(main)
button3.place(relx=0.1, rely=0.695, width=260, height=80)
button3.configure(relief="flat")
button3.configure(overrelief="flat")
button3.configure(activebackground="#ffffff")
button3.configure(cursor="hand2")
button3.configure(foreground="#ffffff")
button3.configure(background="#ffffff") # #fffff <- original valie for tranparency
button3.configure(borderwidth="0")#visibility of border
img4 = PhotoImage(file="./images/3.png")
button3.configure(image=img4)
button3.configure(command=credit)

main.mainloop()
A