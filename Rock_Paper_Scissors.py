from tkinter import *
import time as t
import random

compturn = {0:"ROCK",1:"PAPER",2:"SCISSORS"}
sc = 0
sp =0
FB = 0

#BEST OF

def BO3():
    t.sleep(1)
    global FB
    B05['state'] = 'disable'
    B03['state'] = 'disable'
    FB = 3
    B1['state']='active'
    B2['state']='active'
    B3['state']='active'
def BO5():
    t.sleep(1)
    B05['state'] = 'disable'
    global FB
    B03['state'] = 'disable'
    FB =5
    B1['state']='active'
    B2['state']='active'
    B3['state']='active'

#RESPONSE

def rock():
    global sc
    global sp
    comp = random.randint(0,2)
    if compturn[comp] == "ROCK":
        win = "DRAW"
        L1.config(bg="yellow")
        L2.config(bg='yellow')
    elif compturn[comp] == "PAPER":
        win = "COMPUTER WINS"
        sc+=1
        L3.config(text = '      {}-{}'.format(sp,sc))
        L1.config(bg="red")
        L2.config(bg='green')
    elif compturn[comp] == "SCISSORS":
        win = "PLAYER WINS"
        sp+=1
        L3.config(text = '      {}-{}'.format(sp,sc))
        L1.config(bg="green")
        L2.config(bg='red')
    L3_1.config(text='ROCK >>',bg='white')
    L3_2.config(text=win,bg='black',fg = 'white')
    L3_3.config(text='<<'+compturn[comp],bg='white')
    t.sleep(0.5)
    if sp>=FB//2+1:
        L4_1.config(text='PLAYER WINS!!!',font=40,bg='red',fg='blue')
        B1['state']='disable'
        B2['state']='disable'
        B3['state']='disable'
    elif sc>=FB//2+1:
        L4_1.config(text="COMPUTER WINS!!!",font = 40, bg = 'green',fg = 'red')
        B1['state']='disable'
        B2['state']='disable'
        B3['state']='disable'

def paper():
    global sc
    global sp
    comp = random.randint(0,2)
    if compturn[comp] == "ROCK":
        win = "PLAYER WINS"
        sp+=1
        L3.config(text = '      {}-{}'.format(sp,sc))
        L1.config(bg="green")
        L2.config(bg='red')
    elif compturn[comp] == "SCISSORS":
        win = "COMPUTER WINS"
        sc+=1
        L1.config(bg="red")
        L2.config(bg='green')
        L3.config(text = '      {}-{}'.format(sp,sc))
    elif compturn[comp] == "PAPER":
        win = "DRAW"
        L1.config(bg="yellow")
        L2.config(bg='yellow')
    L3_1.config(text='PAPER >>',bg='white')
    L3_2.config(text=win,bg='black',fg = 'white')
    L3_3.config(text='<<'+compturn[comp],bg='white')
    t.sleep(0.5)
    if sp>=FB//2+1:
        L4_1.config(text='PLAYER WINS!!!',font=40,bg='red',fg='blue')
        B1['state']='disable'
        B2['state']='disable'
        B3['state']='disable'
    elif sc>=FB//2+1:
        L4_1.config(text="COMPUTER WINS!!!",font = 40, bg = 'green',fg = 'red')
        B1['state']='disable'
        B2['state']='disable'
        B3['state']='disable'

def scissors():
    global sc
    global sp
    comp = random.randint(0,2)
    if compturn[comp] == "ROCK":
        win = "COMPUTER WINS"
        sc+=1
        L3.config(text = '      {}-{}'.format(sp,sc))
        L1.config(bg="red")
        L2.config(bg='green')
    elif compturn[comp] == "SCISSORS":
        win = "DRAW"
        L1.config(bg="yellow")
        L2.config(bg='yellow')
    elif compturn[comp] == "PAPER":
        win = "PLAYER WINS"
        sp+=1
        L3.config(text = '      {}-{}'.format(sp,sc))
        L1.config(bg="green")
        L2.config(bg='red') 
    L3_1.config(text='SCISSORS >>',bg='white')
    L3_2.config(text=win,bg='black',fg = 'white')
    L3_3.config(text='<<'+compturn[comp],bg='white')
    t.sleep(0.5)
    if sp>=FB//2+1:
        L4_1.config(text='PLAYER WINS!!!',font=40,bg='red',fg='blue')
        B1['state']='disable'
        B2['state']='disable'
        B3['state']='disable'
    elif sc>=FB//2+1:
        L4_1.config(text="COMPUTER WINS!!!",font = 40, bg = 'green',fg = 'red')
        B1['state']='disable'
        B2['state']='disable'
        B3['state']='disable'

#MAIN

main = Tk()
main.geometry('500x300')
main.title("ROCK PAPER SCISSORS")
mainframe0 = Frame(main)
mainframe1 = Frame(main)
mainframe2 = Frame(main)
mainframe4 = Frame(main)
L4_1 = Label(mainframe4,text = '')
mainframe0.pack()
mainframe1.pack()
mainframe3 = Frame(main)
mainframe3.pack()
mainframe2.pack()
B05 = Button(mainframe0,text = 'Best of 5',command=BO5)
B03 = Button(mainframe0,text = 'Best of 3',command = BO3)
B03.pack(side = LEFT)
B05.pack(side = LEFT)
L1 = Label(mainframe1,text="            Player  ")
L2 = Label(mainframe1,text = "      Computer")
L3 = Label(mainframe1,text = '      {}-{}'.format(sp,sc))
L1.pack(side=LEFT,pady=0,padx=20)
L3.pack(side = LEFT,padx = 20)
L2.pack(side = RIGHT,pady=0,padx=40)
L3_1 = Label(mainframe3,text='      ')
L3_2 = Label(mainframe3,text='      ')
L3_3 = Label(mainframe3,text='      ')
L3_1.pack(side=LEFT,padx=20)
L3_2.pack(side=LEFT,padx=20)
L3_3.pack(side=RIGHT)
B1 = Button(mainframe2,text = "ROCK",command=rock)
B2 = Button(mainframe2,text = "PAPER",command=paper)
B3 = Button(mainframe2,text="SCISSORS",command=scissors)
B1.pack(side = LEFT , padx=20,pady=10)
B2.pack(side = LEFT,padx=20,pady=10)
B3.pack(side = LEFT,padx = 20,pady=10)
B1['state']='disable'
B2['state']='disable'
B3['state']='disable'   
mainframe4.pack()
L4_1.pack()
main.mainloop()     