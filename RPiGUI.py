from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#Hardware
redLed=LED(14)
yellowLed=LED(15)
greenLed=LED(18)

#GUI
win = Tk()
win.title("LED Toggler")
var = IntVar()


#Functions
def ledToggle():
    if var.get() == 1:
        if redLed.is_lit:
            redLed.off()
        else:
            redLed.on()
    
    elif var.get() == 2:
        if yellowLed.is_lit:
            yellowLed.off()
        else:
            yellowLed.on()
            
    elif var.get() == 3:
        if greenLed.is_lit:
            greenLed.off()
        else:
            greenLed.on()

def ledToggle2():
    if redLed.is_lit:
        redLed.off()
    else:
        redLed.on()

def close():
    GPIO.cleanup()
    win.destroy()



#Widgets
radio1 = Radiobutton(win, text='Red', variable=var, value=1)
radio1.grid(row=0,column=0)

radio2 = Radiobutton(win, text='Yellow', variable=var, value=2)
radio2.grid(row=1,column=0)

radio3 = Radiobutton(win, text='Green', variable=var, value=3)
radio3.grid(row=2,column=0)

ledButton = Button(win, text='Toggle', command=ledToggle, height=1, width=24)
ledButton.grid(row=3,column=0)


win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()