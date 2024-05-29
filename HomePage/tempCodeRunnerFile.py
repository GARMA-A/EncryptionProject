import math
import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, filedialog, messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\City tech\Desktop\pahseOnePro[1]\Project Cyber\frame\frame0")

home = r"C:\Users\City tech\Desktop\pahseOnePro[1]\Project Cyber\HomePage\gui.py"  # change the path HomePage verryyyy importanttttt

def home1():
    window.destroy()
    subprocess.run(["python", home], check=True)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def encryptMessage(msg, key):
    cipher = ""
    k_indx = 0
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))
    col = len(key)
    row = int(math.ceil(msg_len / col))
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]

    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1

    return cipher

def decryptMessage(cipher, key):
    msg = ""
    k_indx = 0
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
    col = len(key)
    row = int(math.ceil(msg_len / col))
    key_lst = sorted(list(key))
    dec_cipher = [['' for _ in range(col)] for _ in range(row)]

    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])

        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1

    msg = ''.join(sum(dec_cipher, []))
    null_count = msg.count('_')

    if null_count > 0:
        return msg[: -null_count]

    return msg.replace('_', '')

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
window.configure(bg="#080017")

canvas = Canvas(
    window,
    bg="#080017",
    height=684,
    width=1172,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

canvas.create_text(
    413.0,
    35.0,
    anchor="nw",
    text="Welcome to ColumnTransposition Cipher",
    fill="#FFFFFF",
    font=("InknutAntiqua Regular", 26 * -1)
)

canvas.create_text(
    173.0,
    133.0,
    anchor="nw",
    text="Encryption",
    fill="#555BE8",
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

canvas.create_text(
    24.0,
    333.0,
    anchor="nw",
    text="Key",
    fill="#FFFFFF",
    font=("InknutAntiqua Regular", 23 * -1)
)

entry_bg_2 = canvas.create_image(
    195.5,
    404.5,
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
    fill="#FFFFFF",
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
    fill="#1F45CC",
    font=("InknutAntiqua Regular", 23 * -1)
)

canvas.create_text(
    608.0,
    191.0,
    anchor="nw",
    text="Cipher Text",
    fill="#FFFFFF",
    font=("InknutAntiqua Regular", 23 * -1)
)

entry_bg_4 = canvas.create_image(
    785.5,
    277.5,
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
    command=lambda: update_entry_with_file(entry_4),  # Bind to entry_4 for decryption
    relief="flat",
    font=("Arial", 18)
)
button_3.place(
    x=999.0,
    y=256.0,
    width=151.0,
    height=50.0
)

def update_entry_with_file(entry_widget):
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            entry_widget.delete(0, 'end')
            entry_widget.insert(0, file.read())

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
    fill="#FFFFFF",
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

def encrypt_button_command(entry_1, entry_2, entry_3):
    try:
        message = entry_1.get().replace(' ', '')
        key = entry_2.get()
        if message == "" and key == "":
            messagebox.showerror("Error", "Please enter a message and a key.")
        elif message == "":
            messagebox.showerror("Error", "Please enter a message.")
        elif key == "":
            messagebox.showerror("Error", "Please enter a key.")
     
        elif not key.isalpha():
            messagebox.showerror("Error", "Key must be a string.")
        else:
            entry_3.delete(0, 'end')
            entry_3.insert(0, encryptMessage(message, key))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid key.")

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

def decrypt_button_command(entry_4, entry_5, entry_6):
    try:
        message = entry_4.get().replace(' ', '')
        key = entry_5.get()
        if message == "" and key == "":
            messagebox.showerror("Error", "Please enter a message and a key.")
        elif message == "":
            messagebox.showerror("Error", "Please enter a message.")
        elif key == "":
            messagebox.showerror("Error", "Please enter a key.")
        
        elif not key.isalpha():
            messagebox.showerror("Error", "Key must be a string.")
        else:
            entry_6.delete(0, 'end')
            entry_6.insert(0, decryptMessage(message, key))
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

window.resizable(False, False)
window.mainloop()
