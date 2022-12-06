import random
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('SMART')
root.geometry('400x400')
title = ttk.Label(root, text="Sam's Mental Arithmetic Rapid Test")
title.pack(side=TOP)

play = ttk.Button(root, text='play', command= lambda: playGame())
play.place(relx=.5,rely=.5,anchor=CENTER)

confirm = ttk.Button(root, text="Let's go!", command= lambda: letsgo())

add = IntVar()
sub = IntVar()
mult = IntVar()
div = IntVar()

addition = Radiobutton(root, text='addition', variable=add, value=1)
subtraction = Radiobutton(root, text='subtraction', variable=sub, value=1)
multiplication = Radiobutton(root, text='multiplication', variable=mult, value=1)
division = Radiobutton(root, text='division', variable=div, value=1)
gamemode = Label(root, text='Operations:')

minlabel = Label(root, text='Minimum:')
minimum = Entry(root, width=10)
maxlabel = Label(root, text='Maximum:')
maximum = Entry(root, width=10)
minval = 0
maxval = 0

numslabel = Label(root, text='Amount of numbers:')
numsentry = Entry(root, width=10)
nums = 10


number = 0
display = ''
num = Label(root, text=display, font=('TkDefaultFont',25))

def playGame():
    play.place_forget()

    add.set(0)
    sub.set(0)
    mult.set(0)
    div.set(0)

    gamemode.pack()
    addition.pack()
    subtraction.pack()
    multiplication.pack()
    division.pack()

    minlabel.pack()
    minimum.pack()
    maxlabel.pack()
    maximum.pack()

    numslabel.pack()
    numsentry.pack()
    
    confirm.pack()    

def letsgo():    
    if add.get() == 0 and sub.get() == 0 and mult.get() == 0 and div.get() == 0:
        add.set(1)

    try:
        int(minimum.get())
    except:
        minval = 0
    
    try:
        int(maximum.get())
    except:
        if mult == 1 or div == 1:
            maxval = 10
        else:
            maxval = 50
    
    try:
        int(numsentry.get())
    except:
        nums = 10

    gamemode.pack_forget()
    addition.pack_forget()
    subtraction.pack_forget()
    multiplication.pack_forget()
    division.pack_forget()
    minlabel.pack_forget()
    minimum.pack_forget()
    maxlabel.pack_forget()
    maximum.pack_forget()
    confirm.pack_forget()
    numslabel.pack_forget()
    numsentry.pack_forget()




    num.place(relx=.5, rely=.5, anchor=CENTER)

    for _ in range(nums):
        pass



root.mainloop()