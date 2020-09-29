import tkinter
from tkinter import *

window= tkinter.Tk()

check_varirable1 = IntVar()
check_varirable2 = IntVar()

tkinter.Checkbutton(window, text="Machine Learning" , variable = check_varirable1 , onvalue=1, offvalue=0).grid(row=0,sticky=W)
tkinter.Checkbutton(window, text="DeepLearning" , variable = check_varirable2 , onvalue=1 ,offvalue=0).grid(row=1,sticky=W)

window.mainloop()
