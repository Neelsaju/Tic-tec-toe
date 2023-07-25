from tkinter import *
root = Tk()
root.title("Tik Tec Toe")
root.geometry("500x500")

frame1=Frame(root)
frame1.pack()

titlelabel=Label ( frame1 , text="Tic Tec Toe", font=("Caprasimo",30),bg="white" )
titlelabel.grid(row=0,column=0)

frame2=Frame(root)
frame2.pack()

board={1:" ",2:" ",3:" ",
       4:" ",5:" ",6:" ",
       7:" ",8:" ",9:" ",}

turn="x"

def restartGame():
    global game_end
    game_end = False
    for button in buttons:
        button["text"] = " "

    for i in board.keys():
        board[i] = " "

    titleLabel = Label(frame1 , text="Tic Tac Toe" , font=("Arial" , 30) , bg="white" , width=15 )
    titleLabel.grid(row=0 , column=0)


def check_win(player):

    if board[1] == board[2] == board[3] and board[1] == player:
        return True
    elif board[4] == board[5] == board[6] and board[4] == player:
        return True
    elif board[7] == board[8] == board[9] and board[7] == player:
        return True
    elif board[1] == board[4] == board[7] and board[1] == player:
        return True
    elif board[2] == board[5] == board[8] and board[2] == player:
        return True
    elif board[3] == board[6] == board[9] and board[3] == player:
        return True
    elif board[1] == board[5] == board[9] and board[1] == player:
        return True
    elif board[7] == board[5] == board[3] and board[7] == player:
        return True
    else:
        return False

def check_draw():
    for i in board.keys():
        if board[i] == " ":
            return False
        
    return True

#function play
def play(event):
    global turn
    button=event.widget
    buttontext=str(button)
    clicked=buttontext[-1]
    print(clicked)
    if clicked=="n":
        clicked=1
    else:
        clicked=int(clicked)

    if button["text"]==" ":
        if turn=="x":
            button["text"]="x"
            board[clicked]=turn
            if check_win(turn):
                winlabel=Label(frame1 ,text=f"{turn} win the game!!",bg="white",font=("Caprasimo",20),width=15)
                winlabel.grid(row=0,column=0,columnspan=3)
            turn="o"
        else:
            button["text"]="o"
            board[clicked]=turn
            if check_win(turn):
                winlabel=Label(frame1 ,text=f"{turn} win the game!!",bg="white",font=("Caprasimo",20),width=15)
                winlabel.grid(row=0,column=0,columnspan=3)
            turn="x"
    
        if check_draw():
            drawlabel=Label(frame1 ,text=f"draw game!!",bg="yellow",font=("Caprasimo",20),width=15)
            drawlabel.grid(row=0,column=0,columnspan=3)



#tic tac toe board

#1st row

button1=Button(frame2,text=" ",width=4,height=2, font=("Arial",35))
button1.grid(row=0,column=0)
button1.bind("<Button-1>", play)

button2=Button(frame2,text=" ",width=4,height=2, font=("Arial",35))
button2.grid(row=0,column=1)
button2.bind("<Button-1>", play)

button3=Button(frame2,text=" ",width=4,height=2, font=("Arial",35))
button3.grid(row=0,column=2)
button3.bind("<Button-1>", play)

#1st row

button4=Button(frame2,text=" ",width=4,height=2, font=("Arial",35))
button4.grid(row=1,column=0)
button4.bind("<Button-1>", play)

button5=Button(frame2,text=" ",width=4,height=2, font=("Arial",35))
button5.grid(row=1,column=1)
button5.bind("<Button-1>", play)

button6=Button(frame2,text=" ",width=4,height=2, font=("Arial",35))
button6.grid(row=1,column=2)
button6.bind("<Button-1>", play)

#3rd row

button7=Button(frame2,text=" ",width=4,height=2, font=("Arial",35))
button7.grid(row=2,column=0)
button7.bind("<Button-1>", play)

button8=Button(frame2,text=" ",width=4,height=2, font=("Arial",35))
button8.grid(row=2,column=1)
button8.bind("<Button-1>", play)

button9=Button(frame2,text=" ",width=4,height=2, font=("Arial",35))
button9.grid(row=2,column=2)
button9.bind("<Button-1>", play)

restartButton = Button(frame2 , text="Restart Game" , width=19 , height=1 , font=("Arial" , 20) , bg="Green" , relief=RAISED , borderwidth=5 , command=restartGame )
restartButton.grid(row=4 , column=0 , columnspan=3)

buttons = [button1 , button2 , button3 , button4 , button5 , button6 , button7 , button8, button9]
'''
#widgets are added here
'''
root.mainloop()


