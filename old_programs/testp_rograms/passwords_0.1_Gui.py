import os
import tkinter as tk
# =================================================
from cryptography.fernet import Fernet as fr

with open("key.key", "rb") as f:
    key = f.read()
fernet = fr(key)
# =================================================
passwords ={}
# =================================================
def load_passwords():
    if os.path.exists("passwords.txt"):
        with open("passwords.txt", "rb" ) as file:
            for line in file:
                parts = line.strip().split(b"|")
                if len(parts)==3:
                    site = parts[0].decode().lower()
                    login = parts[1].decode()
                    password = fernet.decrypt(parts[2]).decode()
                    passwords[site]= [login, password]
# =================================================================================
def style_buttons(master, text, command): 
    return tk.Button(
        master,
        text=text,
        command=command,
        bg="white",
        fg="black",
        font=("helvetica", 11, "italic"),
        relief="raised",
        bd=3,
        activebackground="#66b3ff",
        activeforeground="white",
        cursor="hand2"
        )
# =================================================================================
def style_lable(master, text, font=("Arial", 13, "italic")):
    return tk.Label(
        master,
        text=text,
        fg="#003366",
        bg="#e6f0ff",
        font=font
        )
# ==============================================================================
root = tk.Tk()
root.title("Passwords manager")
root.geometry("1200x800")
root.configure(bg="lightblue")

load_passwords()

# Frame labels 
top_frame = tk.Frame(root, bg="lightblue")
top_frame.pack(pady=30)

label = style_lable(top_frame, text="Hello, bro!", font=("Arial", 16, "bold"))
label.grid(row=0, column=0, columnspan=2, pady=10)

status_lable = tk.Label(top_frame, text="", fg="red", bg="lightblue", font=("Arial", 13, "bold"))
status_lable.grid(row=1, column=0, columnspan=2, pady=5)

label_site = style_lable(top_frame, text="Site:")
label_site.grid(row=2, column=0, sticky="e", padx=5, pady=5)

entry_site = tk.Entry(top_frame, width=30)
entry_site.grid(row=2, column=1, padx=5, pady=5)

label_login = style_lable(top_frame, text="Login:")
label_login.grid(row=3, column=0, sticky="e", padx=5, pady=5)

entry_login = tk.Entry(top_frame, width=30)
entry_login.grid(row=3, column=1, padx=5, pady=5)

label_password = style_lable(top_frame, text="Password:")
label_password.grid(row=4, column=0, sticky="e", padx=5, pady=5)

entry_password = tk.Entry(top_frame, width=30, show="*")
entry_password.grid(row=4, column=1, padx=5, pady=5)

# Frame buttons
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=30)
# =================================================
def save_passwords():
    with open("passwords.txt", "wb") as file:  
        for site, (login, password) in passwords.items():
            encrypted_password = fernet.encrypt(password.encode())
            file.write(f"{site}|{login}|".encode() + encrypted_password + b"\n")
# =================================================================
def add_password():
    site = entry_site.get().strip()
    site_lower = site.lower()
    login = entry_login.get().strip()
    password = entry_password.get().strip()
    if not site or not login or not password:
        status_lable.config(text="Enter something, bro!", fg="red")
        return
    passwords[site_lower] = [login, password]
    save_passwords()

    entry_site.delete(0, tk.END)
    entry_login.delete(0, tk.END)
    entry_password.delete(0, tk.END)

    status_lable.config(text=f"Site: {site}\nLogin: {login}\nPassword: {password}", fg="green")
# =================================================================
def show_password():
    show_win = tk.Toplevel(root)
    show_win.title("All passwords")
    show_win.geometry("800x600")

    if not passwords:
        tk.Label(show_win, text="Passwords is not found").pack(padx=10, pady=10)
        return

    for site, (login, password) in passwords.items():
        text = f"Site: {site}\nLogin: {login}\nPassword: {password}\n{'-'*20}"
        tk.Label(show_win, text=text, justify="left").pack(anchor="w", padx=10, pady=5)
# =================================================================
def search_password():
    site_searching = tk.Toplevel(root)
    site_searching.title("Searching sites.")
    site_searching.geometry("1200x500")
    site_searching.configure(bg="lightblue")

    left_frame = tk.Frame(site_searching, bg="lightblue")
    left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

    label_searching_site = style_lable(left_frame, "Enter site")
    label_searching_site.pack(padx=(0,5))

    entry_searching_site = tk.Entry(left_frame, width=25)
    entry_searching_site.pack(pady=(0,10))

    btn_site_searching = style_buttons(left_frame, "Search", None)
    btn_site_searching.pack(pady=5) 

    right_frame = tk.Frame(site_searching, bg="white", relief="sunken", bd=2)
    right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")  

    msg_searching = tk.Label(right_frame, text="", fg="green", bg="white", font=("Arial", 13, "italic"))
    msg_searching.pack(fill="both", expand=True, padx=5, pady=5)

    site_searching.grid_columnconfigure(1, weight=1)
    site_searching.grid_rowconfigure(0, weight=1)

    def searching_button(event=None):
        site_name = entry_searching_site.get().strip().lower()
        if site_name in  passwords:
            login, password = passwords[site_name]
            text = f"Site: {site_name}\nLogin: {login}\nPassword: {password}"
            msg_searching.config(text=text, fg="green")
        else:
            msg_searching.config(text="Site not found", fg="red")
    
        entry_searching_site.delete(0, tk.END)

    btn_site_searching.config(command=searching_button)
    entry_searching_site.bind("<Return>", searching_button)

# =================================================================
def delete_password():
    site_del = tk.Toplevel(root)
    site_del.title("Delete site")
    site_del.geometry("600x350")
    site_del.configure(bg="lightblue")

    lable_del_site = tk.Label(site_del, text="Enter site", fg="darkblue", bg="lightblue", font=("Arial", 12, "italic"))
    lable_del_site.pack()

    entry_del_site = tk.Entry(site_del, width=30)
    entry_del_site.pack()
    
    msg_lable = tk.Label(site_del, text="", fg="green", bg="lightblue", font=("Arial", 13, "italic"))
    msg_lable.pack(pady=5)

    def button(event=None):
        site_name = entry_del_site.get().strip().lower()
        if site_name in passwords:
            del passwords[site_name]
            msg_lable.config(text="Site was deleted", fg="green")
            save_passwords()
        else:
            msg_lable.config(text="Site is not found", fg="red")
        entry_del_site.delete(0, tk.END)

    entry_del_site.bind("<Return>", button)
    
    btn_del_site = style_buttons(site_del, "Delete", button)
    btn_del_site.pack(pady=10)
# =================================================================
btn_add = style_buttons(button_frame, "Add password", add_password)
btn_add.grid(row=0, column=0, padx=10, pady=10)

btn_show = style_buttons(button_frame, "Show all passwords", show_password)
btn_show.grid(row=0, column=1, padx=10, pady=10)

btn_del = style_buttons(button_frame, "Delete password", delete_password)
btn_del.grid(row=0, column=2, padx=10, pady=10)

btn_searching = style_buttons(button_frame, "Searching", search_password)
btn_searching.grid(row=0, column=3, padx=10, pady=10)
# =================================================================
root.mainloop()