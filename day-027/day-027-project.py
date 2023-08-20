from tkinter import *

window = Tk()

window.title("Mile to Km Converter")
window.minsize(width=250, height=120)
window.config(padx=50, pady=20)

## Labels
equal_label = Label(text='is equal to', font=("Arial", 18))
equal_label.grid(row=1, column=0)

mile_label = Label(text='Mile(s)', font=("Arial", 18))
mile_label.grid(row=0, column=2)

km_label = Label(text='Km(s)', font=("Arial", 18))
km_label.grid(row=1, column=2)

convert_label = Label(text='0', font=("Arial", 18, 'bold'))
convert_label.grid(row=1, column=1)
convert_label.config(padx=10, pady=20)

## Entry
mile_input = Entry(width=10)
mile_input.grid(row=0, column=1)

## Button
def mile_to_km():
    km_value = float(mile_input.get()) * 1.609   ## mile to km conversion
    convert_label.config(text=km_value)

calc_button = Button(text="Calculate", command=mile_to_km)
calc_button.grid(row=2, column=1)






window.mainloop()