import customtkinter
from tkinter import *
import tkinter.messagebox as messagebox
import random as rd
import string as st

app = customtkinter.CTk()
app.title("Password Generator Application")
app.geometry("400x300")
app.resizable(False, False)
app.config(bg="#2e2e2e")
font = ("Times New Roman", 13, "bold")

label = Label(app, text="Strength Of Password:", font=font, bg="#2e2e2e", fg="white")
label.place(x=10, y=10)

option = IntVar(value=0)


def select_option():
    selected = option.get()


radiobutton1 = Radiobutton(app, text="Weak", variable=option, value=0, command=select_option, font=font, bg="#2e2e2e",
                           fg="white", selectcolor="#2e2e2e")
radiobutton1.place(x=190, y=40)
radiobutton2 = Radiobutton(app, text="Neutral", variable=option, value=1, command=select_option, font=font,
                           bg="#2e2e2e", fg="white", selectcolor="#2e2e2e")
radiobutton2.place(x=290, y=40)
radiobutton3 = Radiobutton(app, text="Strong", variable=option, value=2, command=select_option, font=font, bg="#2e2e2e",
                           fg="white", selectcolor="#2e2e2e")
radiobutton3.place(x=390, y=40)

length_label = Label(app, text="Set Length:", font=font, bg="#2e2e2e", fg="white")
length_label.place(x=10, y=80)
size_entry = Entry(app, width=5)
size_entry.place(x=120, y=85)


def generate_password():
    length = size_entry.get()
    if not length.isdigit():
        messagebox.showerror("Invalid Input", "Please enter a valid number for the length.")
        return
    length = int(length)
    if option.get() == 0:
        characters = st.ascii_uppercase + st.ascii_lowercase
    elif option.get() == 1:
        characters = st.ascii_uppercase + st.ascii_lowercase + st.digits
    elif option.get() == 2:
        symbols = "~!@#$%^&*()_+{}|:\"<>?/"
        characters = st.ascii_uppercase + st.ascii_lowercase + st.digits + symbols

    password = ''.join(rd.sample(characters, length))
    password_label.config(text=password)


generate_button = customtkinter.CTkButton(app, text="Generate Password", height=40,
                                          width=160, bg_color="#2e2e2e", corner_radius=20, command=generate_password)
generate_button.place(x=120, y=150)

password_label = Label(app, text="", font=font, bg="#2e2e2e", fg="white")
password_label.pack(side=BOTTOM, pady=20)

app.mainloop()


























