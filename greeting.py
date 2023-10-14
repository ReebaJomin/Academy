import random
import tkinter
window=tkinter.Tk()
window.minsize(600,400)
window.title("Greeting message")
label=tkinter.Label(text="Hello !",font=("Times New Roman",20,"bold"))
label.place(x=150,y=50)
window.mainloop()