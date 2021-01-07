
import tkinter

theBoard = {'7':' ' , '8':' ' , '9':' ' ,
            '4':' ' , '5':' ' , '6':' ' ,
            '1':' ' , '2':' ' , '3':' ' }

window = tkinter.Tk()
btn_frame = tkinter.Frame(window, width=300, height=300, bd=0, highlightbackground="black", highlightcolor="orange",
                          highlightthickness="1")
chance = "X"
winner = False
count = 0

def all_str_var():
    global winner_dis,chance_dis
    winner_dis = tkinter.StringVar()
    chance_dis = tkinter.StringVar()
    chance_dis.set("chance:" + chance)
    tkinter.Label(window, textvariable=chance_dis, fg="black").pack(side="bottom")
    return winner_dis,chance_dis

all_str_var()

def forget_str_var(widget):
    widget.pack_forget()

def coordinate_pos(pos_num):
    global row,column
    if pos_num == "7":
        row =0
        column =0
    if pos_num == "8":
        row =0
        column =1
    if pos_num == "9":
        row = 0
        column =2
    if pos_num == "4":
        row =1
        column =0
    if pos_num == "5":
        row =1
        column =1
    if pos_num == "6":
        row =1
        column =2
    if pos_num == "1":
        row =2
        column =0
    if pos_num == "2":
        row =2
        column =1
    if pos_num == "3":
            row =2
            column =2

def point_system():

    global btn_frame,winner,chance_dis,count,game,chance

    if count >= 5:

            """if chance == "X":
                chance = "O"
            else:
                chance = "X" """

            if theBoard['7'] == theBoard['8'] == theBoard['9']:
                    winner = True

            else:
                winner = False

            if theBoard['4'] == theBoard['5'] == theBoard['6']:
                winner = True

            else:
                winner = False

            if theBoard['1'] == theBoard['2'] == theBoard['3']:
                winner = True

            else:
                winner = False

            if theBoard['7'] == theBoard['5'] == theBoard['3']:
                winner = True

            else:
                winner = False

            if theBoard['9'] == theBoard['5'] == theBoard['1']:
                winner = True

            else:
                winner = False

            if theBoard['7'] == theBoard['4'] == theBoard['1']:
                winner = True

            else:
                winner = False

            if theBoard['8'] == theBoard['5'] == theBoard['2']:
                winner = True

            else:
                winner = False

            if theBoard['9'] == theBoard['6'] == theBoard['3']:
                winner = True

            else:
                winner = False

            if winner == True:
                chance_dis.set("")
                winner_dis.set(chance + " wins!")
                tkinter.Label(window, textvariable=winner_dis, fg="black").pack(side="bottom")

            if count == 9 and winner == False:
                winner = "tie"
                chance_dis.set("")
                winner_dis.set("It's a Tie!")
                tkinter.Label(window, textvariable=winner_dis, fg="black").pack(side="bottom")

            """if chance == "X":
                chance = "O"
            else:
                chance = "X" """

    return winner , chance

def play_system(pos):
    global chance, count,winner,winner_dis,chance_dis
    coordinate_pos(pos)

    if winner == False:

        if theBoard[pos] == ' ':

            theBoard[pos] = chance
            print(theBoard)
            tkinter.Label(btn_frame, text=theBoard[pos], fg="blue", bg="orange", height=2, width=3).grid(row=row,
                                                                                                         column=column)

            count += 1

            point_system()

            if chance == "X":
                chance = "O"
            else:
                chance = "X"



            chance_dis.set("chance:" + chance+"\ncount:"+str(count))



        elif theBoard[pos] != ' ':
            tkinter.Label(window, text="Plz Enter another location.").pack(side="bottom")



button1 = tkinter.Label(btn_frame,text="Game Over", width=300, height=300,bg="black",fg="white")

button2 = tkinter.Button(btn_frame, text="",width=10, height=5,fg="black",bg = "white",command=lambda :play_system('7')).grid(row=0,column=0)

button3 = tkinter.Button(btn_frame, text="" ,width=10, height=5,fg="black",bg="white",command=lambda :play_system('8')).grid(row=0,column=1)

button4 = tkinter.Button(btn_frame , text = "",width = 10 , height = 5 ,fg = "black",bg = "white",command=lambda :play_system('9')).grid(row=0,column=2)

button5 = tkinter.Button(btn_frame, text = "",width = 10 , height = 5,fg = "black",bg = "white",command=lambda :play_system('4')).grid(row=1,column=0)

button6 = tkinter.Button(btn_frame, text = "",width = 10 , height = 5 ,fg = "black",bg = "white",command=lambda :play_system('5')).grid(row=1,column=1)

button7 = tkinter.Button(btn_frame , text = "",width = 10 , height = 5 ,fg = "black",bg = "white",command=lambda :play_system('6')).grid(row=1,column=2)

button8 = tkinter.Button(btn_frame , text = "",width = 10 , height = 5 ,fg = "black",bg = "white",command=lambda :play_system('1')).grid(row=2,column=0)

button9 = tkinter.Button(btn_frame, text = "",width = 10 , height = 5 ,fg = "black",bg = "white" ,command=lambda :play_system('2')).grid(row=2,column=1)

button10 = tkinter.Button(btn_frame  , text = "",width = 10 , height = 5 ,fg = "black",bg = "white",command=lambda :play_system('3')).grid(row=2,column=2)

btn_frame.pack()

window.mainloop()





