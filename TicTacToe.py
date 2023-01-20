
from tkinter import *
from tkinter import messagebox

window=Tk()
player=True
count=0

def disable():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def checkwinner():
    global winner
    winner = False
    if (b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X") or (b6["text"]=="X" and b4["text"]=="X" and b5["text"]=="X") or (b9["text"]=="X" and b7["text"]=="X" and b8["text"]=="X") or (b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X") or (b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X") or (b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X") or (b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X") or (b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X"):
        winner=True 
        messagebox.showinfo("TICTACTOE","X Wins!!")
        disable()

    elif (b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O") or (b6["text"]=="O" and b4["text"]=="O" and b5["text"]=="O") or (b9["text"]=="O" and b7["text"]=="O" and b8["text"]=="O") or (b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O") or (b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O") or (b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O") or (b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O") or (b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O"):
        winner = True
        messagebox.showinfo("TICTACTOE","O Wins!!")
        disable()
    
    elif count==9 and winner== False:
        messagebox.showinfo('TICTACTOE','Tie Game')
        disable()

def action(button):
    global player,count
    if button["text"] == " " and player == True:
        label.config(text="Player 2")
        button.config(text="X")
        count+=1
        player= False
        checkwinner()

    elif button["text"] == " " and player == False:
        label.config(text="Player 1")
        button.config(text="O")
        count+=1
        player = True
        checkwinner()
    else:
        messagebox.showerror("TICTACTOE","Box already chosen, choose another box")
        
def maingame():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global count,player,label
    count=0
    player=True
    
    b1=Button(window,text=" ",height=3,width=7,font='helvetica',command=lambda : action(b1))
    b2=Button(window,text=" ",height=3,width=7,font='helvetica',command=lambda : action(b2))
    b3=Button(window,text=" ",height=3,width=7,font='helvetica',command=lambda : action(b3)) 

    b4=Button(window,text=" ",height=3,width=7,font='helvetica',command=lambda : action(b4)) 
    b5=Button(window,text=" ",height=3,width=7,font='helvetica',command=lambda : action(b5))
    b6=Button(window,text=" ",height=3,width=7,font='helvetica',command=lambda : action(b6))

    b7=Button(window,text=" ",height=3,width=7,font='helvetica',command=lambda : action(b7))
    b8=Button(window,text=" ",height=3,width=7,font='helvetica',command=lambda : action(b8))
    b9=Button(window,text=" ",height=3,width=7,font='helvetica',command=lambda : action(b9))

    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)

    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2) 

    label=Label(text='Player 1')
    label.grid(row=3,column=1)  

maingame()
reset_button=Button(text="Reset Game",command=maingame)
reset_button.grid(row=4,column=1)
window.mainloop()