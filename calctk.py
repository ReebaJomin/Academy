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
def two():
        global cal
        element=button2.cget("text")
        cal+=element
        label1.config(text=cal)
def three():
        global cal
        element=button3.cget("text")
        cal+=element
        label1.config(text=cal)
def five():
        global cal
        element=button5.cget("text")
        cal+=element
        label1.config(text=cal)
def six():
        global cal
        element=button6.cget("text")
        cal+=element
        label1.config(text=cal)
def seven():
        global cal
        element=button7.cget("text")
        cal+=element
        label1.config(text=cal)
def eight():
        global cal
        element=button8.cget("text")
        cal+=element
        label1.config(text=cal)
def nine():
        global cal
        element=button9.cget("text")
        cal+=element
        label1.config(text=cal)
def ten():
        global cal
        element=button1.cget("text")
        cal+=element
        label1.config(text=cal)
def eleven():
        global cal
        element=button11.cget("text")
        cal+=element
        label1.config(text=cal)
def twelve():
        global cal
        element=button12.cget("text")
        cal+=element
        label1.config(text=cal)
def thirteen():
        global cal
        element=button13.cget("text")
        cal+=element
        label1.config(text=cal)
def fourteen():
        global cal
        element=button14.cget("text")
        cal+=element
        label1.config(text=cal)
def fifteen():
        global cal
        element=button15.cget("text")
        cal+=element
        label1.config(text=cal)
def sixteen():
        global cal
        element=button16.cget("text")
        cal+=element
        label1.config(text=cal)
def calculate():
    global cal
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
    label3.config(text=str(result))
def clear():
    global cal
    cal=" "
    label1.config(text="0")
    label3.config(text="0")
label3=tkinter.Label(text="0")
label3.place(x=150,y=50)
button1=tkinter.Button(text="1",command=one)
button1.place(x=50,y=100)
button2=tkinter.Button(text="2",command=two)
button2.place(x=100,y=100)
button3=tkinter.Button(text="3",command=three)
button3.place(x=150,y=100)
button4=tkinter.Button(text="AC",command=clear)
button4.place(x=250,y=100)
button5=tkinter.Button(text="4",command=five)
button5.place(x=50,y=150)
button6=tkinter.Button(text="5",command=six)
button6.place(x=100,y=150)
button7=tkinter.Button(text="6",command=seven)
button7.place(x=150,y=150)
button8=tkinter.Button(text="*",command=eight)
button8.place(x=200,y=150)
button9=tkinter.Button(text="/",command=nine)
button9.place(x=250,y=150)
button10=tkinter.Button(text="7",command=ten)
button10.place(x=50,y=200)
button11=tkinter.Button(text="8",command=eleven)
button11.place(x=100,y=200)
button12=tkinter.Button(text="9",command=twelve)
button12.place(x=150,y=200)
button13=tkinter.Button(text="+",command=thirteen)
button13.place(x=200,y=200)
button14=tkinter.Button(text="-",command=fourteen)
button14.place(x=250,y=200)
button15=tkinter.Button(text="0",command=fifteen)
button15.place(x=50,y=250)
button16=tkinter.Button(text="%",command=calculate)
button16.place(x=150,y=250)
button17=tkinter.Button(text="Ans",command=calculate)
button17.place(x=200,y=250)
button18=tkinter.Button(text="=",command=calculate)
button18.place(x=250,y=250)
window.mainloop()