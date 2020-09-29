import tkinter

window = tkinter.Tk()

def my_text():
    tkinter.Label(window,text="Hi , coming form your click!").pack(side="bottom")

tkinter.Button(window,text ="Click Me",command=my_text).pack(side="top")

window.mainloop()