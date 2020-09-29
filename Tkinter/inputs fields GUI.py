import tkinter

window = tkinter.Tk()

tkinter.Label(window,text="Username",fg="blue").grid(row=0)
tkinter.Entry(window).grid(row=0,column=1)
tkinter.Label(window,text="password").grid(row=1)
tkinter.Entry(window).grid(row=1,column=1)
tkinter.Checkbutton(window,text="Keep me ,logged in.").grid(columnspan=2)

window.mainloop()