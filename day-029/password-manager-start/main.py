from tkinter import *
from tkinter import messagebox as mb
from random import choice, randint, shuffle
import pyperclip

import json

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
    website = website_user.get()
    email = email_user.get()
    password = generated_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }}

    if len(website) == 0 or len(password) == 0:
        mb.showinfo(title="Oops!", message="Please make sure you haven't left any fields empty!")
    else:
        # This approach is useful for just writing
        # with open("password_manager_log.json", "w") as log_file:
        #    json.dump(new_data, log_file, indent=4)
        try:
            with open("password_manager_log.json", "r") as log_file:
                # Read previous data
                data = json.load(log_file)
        except FileNotFoundError:
            with open("password_manager_log.json", "w") as log_file:
                json.dump(new_data, log_file, indent=4)
        else:
            # Update the previous data with new one
            data.update(new_data)
            ## Write the log json file
            with open("password_manager_log.json", "w") as log_file:
                json.dump(data, log_file, indent=4)
        finally:
            website_user.delete(0, END)
            generated_password.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    try:
        with open("password_manager_log.json", "r") as log_file:
            # Read previous data
            data = json.load(log_file)
            website = website_user.get()
            current_web_dict = data[website]
    except FileNotFoundError as error_file:
        mb.showinfo(title="Oops!", message=f"Log file is not found!")
    except KeyError as error_key:
        mb.showinfo(title="Oops!", message=f"No details for the {error_key} does not exist!")
    else:
        mb.showinfo(title=f"{website}",
                    message=f"E-mail: {current_web_dict['email']}\nPassword: {current_web_dict['password']}")


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
website_user = Entry(width=23)
website_user.grid(row=1, column=1)
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
search_button = Button(text="Search",
                         highlightthickness=0, command=search_password, width=12)
search_button.grid(row=1, column=2)


add_button = Button(text="Add", width=38,
                    highlightthickness=0, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
