import tkinter

window = tkinter.Tk()

def left_click(event):
    tkinter.Label(window,text="Left Click").pack()

def right_cliick(event):
    tkinter.Label(window,text="Right Click").pack()

def middle_click(event):
    tkinter.Label(window,text="Middle click").pack()

window.bind("<Button-1>",left_click)
window.bind("<Button-3>",right_cliick)
window.bind("<Button-2>",middle_click)

window.mainloop()
