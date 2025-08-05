"""
main.py
"""
import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------------------- PASSWORD GENERATOR ---------------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_set = [random.choice(letters) for _ in range(random.randint(8, 10))]

    password_set += [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_set += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_set)

    # Populate password field with new password & copy to clipboard
    password_input.insert(0, "".join(password_set))
    pyperclip.copy("".join(password_set)) # Copy to clipboard


# ---------------------------------------- SAVE PASSWORD --------------------------------------------- #
def save_data():
    # Retrieve information
    website = website_input.get()
    username = email_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    # Detect empty fields & notify user
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning("Oops", "All fields should be filled!")
    else:
        try:
            with open('data.json', mode='r') as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode='w') as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old with new data
            data.update(new_data)

            with open('data.json', mode='w') as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            # Clear fields
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------------------- FIND PASSWORD --------------------------------------------- #
def find_password():
    website_name = website_input.get()

    try:
        with open("data.json", mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning("Oops!", "No Data File Found")
    else:
        if website_name in data:
            website = data[website_name]
            messagebox.showinfo(website_name, f"Email: {website["email"]}"
                                f"\nPassword:{website["password"]}")
        else:
            messagebox.showwarning("Oops", f"Entry '{website_name}' Not Found")

# ---------------------------------------- UI SETUP -------------------------------------------------- #
window = Tk()
window.title("MyPass")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
img_path = "logo.png"
bg_img = PhotoImage(file=img_path)
canvas.create_image(100, 100, image=bg_img)
canvas.grid(row=0, column=1)

# Enter website name
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1)
website_input.focus()

search_btn = Button(text="Search", width=13, command=find_password)
search_btn.grid(row=1, column=2)

# Enter Email or Username
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
# Inserts your primary email at start of app
email_input.insert(0 , "chukwuemekangumoha@gmail.com")

# Enter or Generate Password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=30)
password_input.grid(row=3, column=1)

gen_password_btn = Button(text="Generate Password", command=generate_password)
gen_password_btn.grid(row=3, column=2)

# Add Credentials
submit_btn = Button(text="Add", width=36, command=save_data)
submit_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()