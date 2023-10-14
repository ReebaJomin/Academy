import random
import tkinter
window=tkinter.Tk()
window.minsize(300,400)
window.title("Calculator")
label1=tkinter.Label(text="0")
label1.place(x=10,y=0)
cal=""
def one():
        global cal
        element=button1.cget("text")
        cal+=element
        label1.config(text=cal)
def calculate():
    global cal
    '''if element=="=":
        l = len(cal)
        sy = res = 0
        for i in range(0, l):
            if cal[i] == '+' or cal[i] == '-' or cal[i] == '*' or cal[i] == '/':
                sy = i

        c = result = 0
        num1= cal[0:sy]
        num2 = cal[sy+1:l]
        if num1 and num2:  
            n1 = int(num1)
            n2 = int(num2)
            
        if cal[sy] == '+':
            result = n1 + n2
        elif cal[sy] == '-':
            result = n1 - n2
        elif cal[sy] == '*':
            result = n1 * n2
        elif cal[sy] == '/':
            result = n1 / n2
        label3.config(text=str(result))'''
def clear():
    label1.config(text="0")
    label3.config(text="0")
label3=tkinter.Label(text="0")
label3.place(x=150,y=50)
button1=tkinter.Button(text="1",command=one)
button1.place(x=50,y=100)
button=tkinter.Button(text="2",command=calculate)
button.place(x=100,y=100)
button=tkinter.Button(text="3",command=calculate)
button.place(x=150,y=100)
button=tkinter.Button(text="AC",command=clear)
button.place(x=250,y=100)
button=tkinter.Button(text="4",command=calculate)
button.place(x=50,y=150)
button=tkinter.Button(text="5",command=calculate)
button.place(x=100,y=150)
button=tkinter.Button(text="6",command=calculate)
button.place(x=150,y=150)
button=tkinter.Button(text="*",command=calculate)
button.place(x=200,y=150)
button=tkinter.Button(text="/",command=calculate)
button.place(x=250,y=150)
button=tkinter.Button(text="7",command=calculate)
button.place(x=50,y=200)
button=tkinter.Button(text="8",command=calculate)
button.place(x=100,y=200)
button=tkinter.Button(text="9",command=calculate)
button.place(x=150,y=200)
button=tkinter.Button(text="+",command=calculate)
button.place(x=200,y=200)
button=tkinter.Button(text="-",command=calculate)
button.place(x=250,y=200)
button=tkinter.Button(text="0",command=calculate)
button.place(x=50,y=250)
button=tkinter.Button(text="%",command=calculate)
button.place(x=150,y=250)
button=tkinter.Button(text="Ans",command=calculate)
button.place(x=200,y=250)
button=tkinter.Button(text="=",command=calculate)
button.place(x=250,y=250)
window.mainloop()