import random
import tkinter
window=tkinter.Tk()
window.minsize(600,400)
window.title("Password generator")
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

label=tkinter.Label(text="Welcome to the PyPassword Generator!")
label.pack()
label1=tkinter.Label(text="How many letters you like in password?")
label1.place(x=50,y=50)
input_element1=tkinter.Entry()
input_element1.place(x=300,y=50)
label2=tkinter.Label(text="How many symbols would you like?")
label2.place(x=50,y=100)
input_element2=tkinter.Entry()
input_element2.place(x=300,y=100)
label3=tkinter.Label(text="How many numbers would you like?")
label3.place(x=50,y=160)
input_element3=tkinter.Entry()
input_element3.place(x=300,y=160)
label4=tkinter.Label(text="Your newly generated password is ")
label4.place(x=50,y=200)
label5=tkinter.Label(text=" ")
label5.place(x=300,y=200)
def generator():
    nr_letters=input_element1.get()
    nr_symbols=input_element2.get()
    nr_numbers=input_element3.get()
    password_list = []
    for char in range(0, int(nr_letters) ):
        password_list += random.choice(letters)

    for char in range(0, int(nr_symbols) ):
        password_list += random.choice(symbols)

    for char in range(0, int(nr_numbers)):
        password_list += random.choice(numbers)

    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    label5.config(text=password)
button=tkinter.Button(text="Generate",command=generator)
button.place(x=200,y=300)
window.mainloop()

