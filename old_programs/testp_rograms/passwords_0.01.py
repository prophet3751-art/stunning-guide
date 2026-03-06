import os
import random
import string
import platform
# ====================================================================
from cryptography.fernet import Fernet as fr
with open("key.key", "rb") as f:
    key = f.read()
fernet = fr(key)
# ====================================================================
passwords ={}
# ====================================================================
def load_passwords():
    if os.path.exists("passwords.txt"):
        with open("passwords.txt", "rb" ) as file:
            for line in file:
                parts = line.strip().split(b"|")
                if len(parts)==3:
                    site = parts[0].decode()
                    login = parts[1].decode()
                    password = fernet.decrypt(parts[2]).decode()
                    passwords[site]= [login, password]
# ====================================================================
def clear_screen():
    if platform.system()== "Windows":
        os.system("cls")
    else:
        os.system("clear")
# ====================================================================
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password
# ====================================================================
def save_passwords():
    with open("passwords.txt", "wb") as file:  # пишем байты
        for site, (login, password) in passwords.items():
            encrypted_password = fernet.encrypt(password.encode())
            file.write(f"{site}|{login}|".encode() + encrypted_password + b"\n")
# ====================================================================
def ask_something(prompt):
    while True:
        user_input= input(prompt).strip()
        if user_input:
            return user_input
        else:
            print("Enter something!")
# ====================================================================
def show_passwords():
    if not passwords:
        load_passwords()
    if passwords:
        for site, (login, password) in passwords.items():
            print(f"Site: {site}")
            print(f"Login: {login}")
            print(f"Password: {password}")
            print("-" * 30)
    else:
        print("Nothing to show!")
# ====================================================================
def add_passwords():
    add_site = ask_something("Enter site: ")
    add_login= ask_something("Enter login: ")
    choise = ask_something("Want to generate a password?(yes/no) :").lower()
    if choise == "yes":
        length = int(input("Enter the length(for example 12): "))
        add_password = generate_password(length)
        print(f"Password was generated: {add_password}")
    else:
        add_password = ask_something("Enter password: ")
    passwords[add_site]= [add_login, add_password] 
# ====================================================================
def delete_password():
    show_passwords()

    del_password = input("Enter site name to delete:")
    if del_password in passwords:
        del passwords[del_password]
        print("Password was removed")
    else:
        print("Enter is not correct")
# ====================================================================
def search_password():
    keyword = ask_something("Enter site name or part of it: ").lower()
    found = False
    for site, (login, password) in passwords.items():
        if keyword in site:
            print(f"Site: {site}")
            print(f"Login: {login}")
            print(f"Password: {password}")
            print("-" * 30)
            found = True
    if not found:
        print("Nothing found.")
# ====================================================================
def edit_password():
    site = ask_something("What site do you want to change?: ").lower()
    if site in passwords:
        login_n, password_n = passwords[site]
        print(f"Old login:{login_n} \nOld password:{password_n}")

        new_login = ask_something("Enter new login: ")
        new_password = ask_something("Enter new password: ")

        if new_login:
            login_n = new_login
        if new_password:
            password_n = new_password
        passwords[site] = [login_n, password_n]
        print("New password added")
    else:
        print("Site not found")
# ====================================================================
load_passwords()
while True:
    clear_screen()

    print("_=Manager of passwords=_")
    print("1. Add password")
    print("2. Show password")
    print("3. Delete password")
    print("4. Searching password")
    print("5. Change login or password")
    print("6. Exit")
    print("-" *30)
# ====================================================================
    user_input= input()
# ==================================================================== 
    if user_input=="1":
        add_passwords()
        save_passwords()
        input("Press 'Enter' to continue...")
    elif user_input=="2":
        show_passwords()
        input("Press 'Enter' to continue...")
    elif user_input=="3":
        delete_password()
        save_passwords()
        input("Press 'Enter' to continue...")
    elif user_input=="4":
        search_password()
        input("Press 'Enter' to continue...")
    elif user_input=="5":
        edit_password()
        save_passwords()
        input("Press 'Enter' to continue...")
    elif user_input=="6":
        print("See you, bro!")
        break
    else:
        print("Eror, Try again")
        input("Press 'Enter' to continue...")