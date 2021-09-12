from tkinter import *

def miles_to_km():
    miles = float(entry1.get())
    km = miles * 1.609
    km_label.config(text=f'{km}')

window = Tk()
window.title('Mile to Km converter')
window.config(padx=20, pady=20)

Miles = Label(text='Miles')
Miles.grid(column=2, row=0)

Km = Label(text='Km')
Km.grid(column=2, row=1)

equal = Label(text='is equal to')
equal.grid(column=0, row=1)

entry1 = Entry()
entry1.grid(column=1, row=0)

km_label = Label(text='0')
km_label.grid(column=1, row=1)

calculate = Button()
calculate.config(text='calculate', command=miles_to_km)
calculate.grid(column=1, row=2)



window.mainloop()