import tkinter
## doc: https://docs.python.org/3/library/tkinter.html

window = tkinter.Tk()
## All program @ between window & window.mainloop()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

## Label
my_label = tkinter.Label(text='It is a label!', font=("Arial", 24, "bold"))
my_label.pack()   ## it presents the label on the screen!
my_label.config(padx=50, pady=50)

my_label['text'] = "New Text" ## OR my_label.config(text="New Text-2")

## Button

def button_clicked():
    new_text = my_input.get()
    my_label.config(text=new_text)

my_button = tkinter.Button(text="Click Me!", command=button_clicked)
my_button.pack()  ### using place to using (x,y) coordinates OR using grid defining row & column. Top left corner = 0,0
## choose grid OR pack. They are not used together.

##Entry

my_input = tkinter.Entry(width=10)
my_input.pack()
print(my_input.get())

window.mainloop()
