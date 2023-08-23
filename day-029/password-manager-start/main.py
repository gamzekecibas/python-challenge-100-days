from tkinter import *
from tkinter import messagebox as mb
from random import choice, randint, shuffle
import pyperclip

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    generated_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(website_user.get()) == 0 or len(generated_password.get()) == 0:
        mb.showinfo(title="Oops!", message="Please make sure you haven't left any fields empty!")
    else:
        is_ok = mb.askokcancel(title=website_user.get(),
                               message=f"These are the details entered:\nEmail: {email_user.get()}"
                                       f"\nPassword: {generated_password.get()}\nIs it OK to save?")
        if is_ok:
            log_file = open("password_manager_log.txt", "a")
            log_file.write(f"{website_user.get()} | {email_user.get()} | {generated_password.get()}\n")
            log_file.close()

            website_user.delete(0, END)
            generated_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
## Logo
window = Tk()
window.title("My Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_image)
canvas.grid(row=0, column=0, columnspan=3)

### Labels
website_title = Label(text="Website:", font=(FONT_NAME, 12))
website_title.grid(row=1, column=0)

email_title = Label(text="E-mail:", font=(FONT_NAME, 12))
email_title.grid(row=2, column=0)

password_title = Label(text="Password:", font=(FONT_NAME, 12))
password_title.grid(row=3, column=0)

## Entry
website_user = Entry(width=40)
website_user.grid(row=1, column=1, columnspan=2)
website_user.focus()

email_user = Entry(width=40)
email_user.grid(row=2, column=1, columnspan=2)
email_user.insert(0, "xyz@email.com")

generated_password = Entry(width=23)
generated_password.grid(row=3, column=1)

## Buttons
password_button = Button(text="Generate Password",
                         highlightthickness=0, command=password_generator)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=38,
                    highlightthickness=0, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
