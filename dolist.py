import random
import tkinter
window=tkinter.Tk()
window.minsize(400,400)
window.title("Calculator")
label1=tkinter.Label(text="0")
label1.place(x=10,y=0)
input_element=tkinter.Entry()
input_element.place(x=10,y=10)
tasks=[]
listbox=tkinter.Listbox(window)
listbox.place(x=10,y=60)
def add():
    input_data=input_element.get()
    listbox.insert(tkinter.END,input_data)
def complete1():
      listbox.delete(0)
def complete2():
      listbox.delete(1)
def complete3():
      listbox.delete(2)
def complete4():
      listbox.delete(3)
def complete5():
      listbox.delete(4)
button=tkinter.Button(text="Add",command=add)
button.place(x=150,y=10)
button1=tkinter.Button(text="Complete",command=complete1)
button1.place(x=150,y=70)
button2=tkinter.Button(text="Complete",command=complete2)
button2.place(x=150,y=100)
button3=tkinter.Button(text="Complete",command=complete3)
button3.place(x=150,y=150)
button4=tkinter.Button(text="Complete",command=complete4)
button4.place(x=150,y=200)
button5=tkinter.Button(text="Complete",command=complete5)
button5.place(x=150,y=250)
window.mainloop()
