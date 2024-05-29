
from pathlib import Path
import subprocess
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\krkr\Desktop\TERM4\cyper-security\EN_DE_criptionGui\Project Cyber\frame\frame0")

from tkinter import Tk, Canvas, Entry, Button, PhotoImage, filedialog, messagebox
import os

from tkinter import Tk, Canvas, Entry, Button, PhotoImage, filedialog, messagebox
home= r"C:\Users\krkr\Desktop\TERM4\cyper-security\EN_DE_criptionGui\Project Cyber\HomePage\gui.py"       #change the path HomePage verryyyy importanttttt
def home1():
    window.destroy()
    subprocess.run(["python", home], check=True)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def encrypt(text, rails):
    """Encrypts a message using the Rail Fence cipher.

    Args:
        text (str): The message to encrypt.
        rails (int): The number of rails to use in the cipher.

    Returns:
        str: The encrypted message.
    """

    text = ''.join(char for char in text.upper() if char.isalpha())  # Remove spaces and keep only alphabets

    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in text:
        fence[rail].append(char)
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    return ''.join(char for rail in fence for char in rail)


def decrypt(cipher, key):
    rail = [['\n' for _ in range(len(cipher))]
            for _ in range(key)]
    dir_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1

    return "".join(result)
def save_to_file(text, default_name='output.txt'):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=default_name)
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text)
            messagebox.showinfo("Success", "File saved successfully!")

def update_entry_with_file(entry_widget):
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            entry_widget.delete(0, 'end')
            entry_widget.insert(0, file.read())


window = Tk()
window.geometry("1172x684")
window.configure(bg="#1A1A1A")  # Changed to dark gray

canvas = Canvas(
    window,
    bg = "#080017",
    height = 684,
    width = 1172,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

canvas.create_text(
    413.0,
    35.0,
    anchor="nw",
    text="Welcome to Rail Fence  Cipher",
    fill="#FFFFFF",
    font=("InknutAntiqua Regular", 26 * -1)
)


canvas.create_text(
    24.0,
    191.0,
    anchor="nw",
    text="Message",
    fill="#FFFFFF",
    font=("InknutAntiqua Regular", 26 * -1)
)

entry_bg_1 = canvas.create_image(
    192.5,
    276.5,
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=27.0,
    y=251.0,
    width=331.0,
    height=49.0
)

button_1 = Button(
    text="Upload File",
    bg="#2a4e78",
    fg="#ffffff",
    borderwidth=0,
    highlightthickness=0,
     command=lambda: update_entry_with_file(entry_1),
    relief="flat",
    font=("Arial", 18)
)
button_1.place(
    x=391.0,
    y=252.0,
    width=151.0,
    height=50.0
)
entry_bg_2 = canvas.create_image(
    195.5,
    404.5,
)

canvas.create_text(
    24.0,
    333.0,
    anchor="nw",
    text="Key",
    fill="#FFFFFF",
    font=("InknutAntiqua Regular", 23 * -1)
)

entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=30.0,
    y=379.0,
    width=331.0,
    height=49.0
)
canvas.create_text(
    18.0,
    458.0,
    anchor="nw",
    text="Cipher Text",
    fill="#FFFFFF",  # Green color
    font=("InknutAntiqua Regular", 23 * -1)
)

entry_bg_3 = canvas.create_image(
    191.5,
    536.5,
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=27.0,
    y=511.0,
    width=329.0,
    height=49.0
)

button_2 = Button(
    text="Save File",
    bg="#2a4e78",
    fg="#ffffff",
    borderwidth=0,
    highlightthickness=0,
     command=lambda: save_to_file(entry_3.get(), 'encrypted_message.txt'),
    relief="flat",
    font=("Arial", 18)
)
button_2.place(
    x=391.0,
    y=513.0,
    width=151.0,
    height=50.0
)

canvas.create_text(
    805.0,
    133.0,
    anchor="nw",
    text="Decryption",
    fill="#1F45CC",  # Blue color
    font=("InknutAntiqua Regular", 23 * -1)
)
canvas.create_text(
    200.0,
    133.0,
    anchor="nw",
    text="Encryption",
    fill="#1F45CC",  # Blue color
    font=("InknutAntiqua Regular", 23 * -1)
)
entry_bg_4 = canvas.create_image(
    785.5,
    277.5,
)

canvas.create_text(
    608.0,
    191.0,
    anchor="nw",
    text="Cipher Text",
    fill="#FFFFFF",  # Red color
    font=("InknutAntiqua Regular", 23 * -1)
)

entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=620.0,
    y=252.0,
    width=331.0,
    height=49.0
)


button_3 = Button(
    text="Upload File",
    bg="#2a4e78",
    fg="#ffffff",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat",
    font=("Arial", 18)
)
button_3.place(
    x=999.0,
    y=256.0,
    width=151.0,
    height=50.0
)

canvas.create_text(
    608.0,
    331.0,
    anchor="nw",
    text="Key",
    fill="#FFFFFF",
    font=("InknutAntiqua Regular", 24 * -1)
)
entry_bg_5 = canvas.create_image(
    785.5,
    406.5,
)

entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=620.0,
    y=381.0,
    width=331.0,
    height=49.0
)

canvas.create_text(
    608.0,
    450.0,
    anchor="nw",
    text="Message",
    fill="#FFFFFF",  # Green color
    font=("InknutAntiqua Regular", 26 * -1)
)

entry_bg_6 = canvas.create_image(
    785.5,
    537.5,
)
entry_6 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=620.0,
    y=512.0,
    width=331.0,
    height=49.0
)

button_4 = Button(
    text="Save File",
    bg="#2a4e78",
    fg="#ffffff",
    borderwidth=0,
    highlightthickness=0,
        command=lambda: save_to_file(entry_6.get(), 'decrypted_message.txt'),
    relief="flat",
    font=("Arial", 18)
)
button_4.place(
    x=993.0,
    y=518.0,
    width=157.0,
    height=51.0
)

button_5 = Button(
    text="Go to Home",
    bg="#2a4e78",
    fg="#ffffff",
    borderwidth=0,
    highlightthickness=0,
    command=home1,  
    relief="flat",
    font=("Arial", 18)
)
button_5.place(
    x=124.0,
    y=602.0,
    width=267.0,
    height=59.0
)

button_6 = Button(
    text="Exit",
    bg="#2a4e78",
    fg="#ffffff",
    borderwidth=0,
    highlightthickness=0,
     command=lambda: window.destroy(),
    relief="flat",
    font=("Arial", 18)
)
button_6.place(
    x=726.0,
    y=596.0,
    width=267.0,
    height=65.0
)
button_7 = Button(
    text="Encrypt",
    bg="#2a4e78",
    fg="#ffffff",
    borderwidth=0,
    highlightthickness=0,
        command=lambda: encrypt_button_command(entry_1, entry_2, entry_3),
    relief="flat",
    font=("Arial", 18)
)
button_7.place(
    x=392.0,
    y=378.0,
    width=151.0,
    height=52.0
)

def encrypt_button_command(entry_1, entry_2, entry_3):
    try:
        message = entry_1.get().replace(' ', '')
        key = entry_2.get()
        
        if not message:
            messagebox.showerror("Error", "Please enter a message.")
        elif not key:
            messagebox.showerror("Error", "Please enter a key.")
        elif not message.isalpha():
            messagebox.showerror("Error", "Message must be a string containing only alphabetic characters.")
        elif not key.isdigit():
            messagebox.showerror("Error", "Key must be a number.")
        elif int(key) <= 1 or int(key) > len(message):
            messagebox.showerror("Error", "Key must be greater than 1 and less than or equal to the length of the message.")
        else:
            encrypted_message = encrypt(message, int(key))
            entry_3.delete(0, 'end')
            entry_3.insert(0, encrypted_message)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid key.")
        
button_8 = Button(
    text="Decrypt",
    bg="#2a4e78",
    fg="#ffffff",
    borderwidth=0,
    highlightthickness=0,
        command=lambda: decrypt_button_command(entry_4, entry_5, entry_6),
    relief="flat",
    font=("Arial", 18)
)
button_8.place(
    x=999.0,
    y=381.0,
    width=151.0,
    height=52.0
)
def decrypt_button_command(entry_4, entry_5, entry_6):
    try:
        cipher = entry_4.get().replace(' ', '')
        key = entry_5.get()
        
        if not cipher:
            messagebox.showerror("Error", "Please enter a cipher.")
        elif not key:
            messagebox.showerror("Error", "Please enter a key.")
        elif not cipher.isalpha():
            messagebox.showerror("Error", "Cipher must be a string containing only alphabetic characters.")
        elif not key.isdigit():
            messagebox.showerror("Error", "Key must be a number.")
        elif int(key) <= 1 or int(key) > len(cipher):
            messagebox.showerror("Error", "Key must be greater than 1 and less than or equal to the length of the cipher.")
        else:
            decrypted_message = decrypt(cipher, int(key))
            entry_6.delete(0, 'end')
            entry_6.insert(0, decrypted_message)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid key.")




window.resizable(False, False)
window.mainloop()
