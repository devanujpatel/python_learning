import tkinter
from tkinter import *

calculator = tkinter.Tk()

calculator.geometry("312x324")

calculator.title("My Calculator")

expresion = ""

def btn_click(term):

    global expression
    global show_text
    expression = " "

    input_text.set(expression)

def btn_clear():
    global expression
    global input_text
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    global input_text

    result = str(eval(expression))
    input_text.set(result)
    expression = ""

input_text = StringVar()

input_frame = tkinter.Frame(calculator , width=312 , height=50 , bd=0, highlightbackground="blue",highlightcolor="orange",highlightthickness="1" )
input_frame.pack(side="top")

input_field = Entry(input_frame,font=('arial','18','bold') , textvariable = input_text,width=50 , bg="white",bd=0,justify=RIGHT)
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)

btn_frame = Frame(calculator,width=312,height=272, bg="grey")
btn_frame.pack()

#First Row  : clear(c) and dividde(/)

clear = Button(btn_frame , text = "C" , width=32,height=3,fg="black",command=lambda:btn_clear() , cursor="hand2"  ,bg = "white").grid(row=0,column=0)
divide = Button(btn_frame , text = "=" , width=10,height=3,fg="black",command=lambda:btn_equal("/") , cursor="hand2"  ,bg = "white").grid(row=0,column=3)

#second row : buttons:7 8 9 *

seven = Button(btn_frame , text = "7" , width=3,height=10,fg="black",command=lambda:btn_click(7) , cursor="hand2"  ,bg = "white").grid(row=1,column=0)

eight = Button(btn_frame , text = "8" , width=3,height=10,fg="black",command=lambda:btn_click(8) , cursor="hand2"  ,bg = "white").grid(row=1,column=1)

nine = Button(btn_frame , text = "9" , width=3,height=10,fg="black",command=lambda:btn_click(9) , cursor="hand2" ,bg = "white").grid(row=1,column=2)

multiply = Button(btn_frame,text="*",width=3,height=10,fg="black", command=lambda:btn_click("*"),cursor="hand2",bg="white" ).grid(row=1,column=3)

#third row : 4 5 6 -

four = Button(btn_frame,text = "4",width=3 ,height=10,fg="black",command=lambda:btn_click(4),cursor="hand2",bg="white").grid(row=2,column=0)

five = Button(btn_frame,text = "5",width=3 ,height=10,fg="black",command=lambda:btn_click(5),cursor="hand2",bg="white").grid(row=2,column=1)

six = Button(btn_frame,text = "6",width=3 ,height=10,fg="black",command=lambda:btn_click(6),cursor="hand2",bg="white").grid(row=2,column=2)

minus = Button(btn_frame,text = "-",width=3 ,height=10,fg="black",command=lambda:btn_click("-"),cursor="hand2",bg="white").grid(row=2,column=3)

#fourth row : 1 2 3 +

one = Button(btn_frame,text = "1",width=3 ,height=10,fg="black",command=lambda:btn_click(1),cursor="hand2",bg="white").grid(row=3,column=0)

two = Button(btn_frame,text = "2",width=3 ,height=10,fg="black",command=lambda:btn_click(2),cursor="hand2",bg="white").grid(row=3,column=1)

three = Button(btn_frame,text = "3",width=3 ,height=10,fg="black",command=lambda:btn_click(3),cursor="hand2",bg="white").grid(row=2,column=2)

plus = Button(btn_frame,text = "+",width=3 ,height=10,fg="black",command=lambda:btn_click("+"),cursor="hand2",bg="white").grid(row=2,column=3)

# fifth row : 0 . =

zero = Button(btn_frame,text = "0",width=3 ,height=10,fg="black",command=lambda:btn_click(0),curso="hand2",bg="white").grid(row=3,column=0)

decimal = Button(btn_frame,text = ".",width=3 ,height=10,fg="black",command=lambda:btn_click("."),cursor="hand2",bg="white").grid(row=3,column=1)

equal = Button(btn_frame,text = "=",width=3 ,height=10,fg="black",command=lambda:btn_equal,cursor="hand2",bg="white").grid(row=3,column=2)

calculator.mainloop()