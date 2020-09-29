import tkinter
import tkinter.messagebox
window = tkinter.Tk()

tkinter.messagebox.showinfo("Alert Box" , "this is just an alert message!")

response = tkinter.messagebox.askquestion("tricky question","do you like Deep Learning?")

if response == 1:
    tkinter.Label(window,text = "yes ofcourse i love it ").pack()

else:
    tkinter.Label(window,text="No i dont like it").pack()

window.mainloop()