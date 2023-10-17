from tkinter import *


def getting_from_input():
    miles = int(input_filed.get())
    km = int(miles * 1.609)
    answer.config(text=f"{km}")


window = Tk()
window.minsize(300, 200)
window.title("Mile to Km Converter")
window.config(padx=150, pady=100)

input_filed = Entry()
input_filed.grid(column=1, row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_IsEqualTo = Label(text="is equal to")
label_IsEqualTo.grid(column=0, row=1)

answer = Label(text="0")
answer.grid(column=1, row=1)


label_km = Label(text="Km")
label_km.grid(column=2, row=1)

button = Button(text="Calculate", command=getting_from_input)
button.grid(column=1, row=2)


window.mainloop()
