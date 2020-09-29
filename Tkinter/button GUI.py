import tkinter

window = tkinter.Tk()

top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side = "bottom")

button_1 = tkinter.Button(top_frame , text = "Button 1" , fg = "red").pack()
button_2 = tkinter.Button(top_frame , text = "Button 2" , fg = "green").pack()

button_3 = tkinter.Button(bottom_frame , text = "Button 3" , fg = "blue").pack(side = "left")
button_4 = tkinter.Button(bottom_frame , text = "Button 4" , fg = "orange").pack(side = "left")

window.mainloop()