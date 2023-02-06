from tkinter import *

number_count = 0

def button1():
    global number_count
    number_count += 1
    count.config(text=number_count)

def button2():
    global number_count
    number_count -= 1
    count.config(text=number_count)

window = Tk()
window.minsize(400,300)
window.resizable(False,False)
window.title("Counter")
window.config(bg="#67C5FF")


count = Label(text=0, font=("Helvetica", 40))
count.config(bg="#67C5FF")
count.place(x=180, y=10)

button_1 = Button(text="+", font=("Helvetica", 20),command=button1)
button_1.place(x=130,y=150)


button_2 = Button(text="-", font=("Helvetica", 20), command=button2)
button_2.place(x=230,y=150)

window.mainloop()