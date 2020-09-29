import tkinter

window = tkinter.Tk()

icon = tkinter.PhotoImage(file ="Taj Mahal.png")

label = tkinter.Label(window,image = icon)

label.pack()

window.mainloop()
