from tkinter import *
from threading import Thread
import time
import pymsgbox


root=Tk()
root.title("Cornometer")
root.resizable(0 , 0)
root.geometry("300x250")
root.config(background = "#8000ff")

hour=0
min=0
sec=0

def press(t):
    global hour , min , sec
    while sec!=59:
        sec+=1
        time.sleep(1)
        sv_result.set("Sec : {}".format(sec)),sv_result02.set("Min : {}".format(min)),sv_result03.set("Hour : {}".format(hour))
        while sec==59:
            sec=0
            min+=1
            time.sleep(1)
            sv_result02.set("Min : {}".format(min))
            while min==59:
                sec=0
                min=0
                hour+=1
                time.sleep(1)
                sv_result03.set("Ho : {}".format(hour))
                if hour==99:
                    pymsgbox.alert("The Program Worked Correctly\nHave a Nice Day")
                    break

thread01=Thread(target = press , args = (0 ,))

def reset(r):
    global sec , min , hour
    sec=0
    min=0
    hour=0
    if r=="01":
        sv_result.set("Sec : {}".format(sec)),sv_result02.set("Min : {}".format(min)),sv_result03.set("Hour : {}".format(hour))

def callfunction():
    thread01.start()


sv_result=StringVar()
lbl01=Label(root , textvariable =sv_result , font = ("Courier" , 9 , "bold") , bg = "#ff1aff" , fg = "#ffff1a" , relief = RIDGE , borderwidth = 2)
lbl01.place(x = 210 , y = 25)
lbl01.config(width = 11 , height = 3)

sv_result02=StringVar()
lbl02=Label(root , textvariable =sv_result02 , font = ("Courier" , 9 , "bold") , bg = "#ff1aff" , fg = "#ffff1a" , relief = RIDGE , borderwidth = 2)
lbl02.place(x = 109 , y = 25)
lbl02.config(width = 11 , height = 3)

sv_result03=StringVar()
lbl03=Label(root , textvariable =sv_result03 , font = ("Courier" , 9 , "bold") , bg = "#ff1aff" , fg = "#ffff1a" , relief = RIDGE , borderwidth = 2)
lbl03.place(x = 9 , y = 25)
lbl03.config(width = 11 , height = 3)

btn01=Button(root , text = "Start" , command = callfunction  , font = ("Courier" , 9) , bg = "#33cc00" , fg = "#000000" , relief = RAISED , borderwidth = 3)
btn01.place(x = 30 , y = 120)
btn01.config(width = 12 , height = 2)

btn02=Button(root , text = "Reset" , command = lambda :reset("01"), font = ("Courier" , 9) , bg = "#ff751a" , fg = "#000000" , relief = RAISED , borderwidth = 3)
btn02.place(x = 170 , y = 120)
btn02.config(width = 12 , height = 2)

btn03=Button(root , text = "Exit" , command = root.destroy , font = ("Courier" , 9) , bg = "#b30000" , fg = "#000000" , relief = RAISED , borderwidth = 3)
btn03.place(x = 100 , y = 180)
btn03.config(width = 12 , height = 2)

sv_result.set("Sec : {}".format(sec)),sv_result02.set("Min : {}".format(min)),sv_result03.set("Hour : {}".format(hour))

root.mainloop()
