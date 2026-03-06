import tkinter as tk
# =================================================
passwords ={}
# =================================================

root = tk.Tk()
root.title("Passwords manager")
# =================================================
label = tk.Label(root, text="Hello, bro!")
label.pack(pady=10)
# =================================================
label_site = tk.Label(root, text="Site:")
label_site.pack()

entry_site = tk.Entry(root, width=30)
entry_site.pack()

label_login = tk.Label(root, text="Login:")
label_login.pack()

entry_login = tk.Entry(root, width=30)
entry_login.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack()

entry_password = tk.Entry(root, width=30, show="*")
entry_password.pack()
# =================================================
def add_password():
    site = entry_site.get().strip()
    login = entry_login.get().strip()
    password = entry_password.get().strip()

    print(f"Site: {site}")
    print(f"Login: {login}")
    print(f"Password: {password}")
    passwords[site] = [login, password]
# =================================================
btn_add = tk.Button(root, text="Add password", command=add_password)
btn_add.pack(pady=10)
# =================================================

root.mainloop()