import sys
import os
import random
import string
import platform
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
)
from PyQt6.QtCore import QSize
from cryptography.fernet import Fernet as fr

# ================== ENCRYPTION ==================
with open("key.key", "rb") as f:
    key = f.read()
fernet = fr(key)

passwords = {}

# ================== LOGIC ==================
def load_passwords():
    if os.path.exists("passwords.txt"):
        with open("passwords.txt", "rb") as file:
            for line in file:
                parts = line.strip().split(b"|")
                if len(parts) == 3:
                    site = parts[0].decode().lower()
                    login = parts[1].decode()
                    password = fernet.decrypt(parts[2]).decode()
                    passwords[site] = [login, password]


def save_passwords():
    with open("passwords.txt", "wb") as file:
        for site, (login, password) in passwords.items():
            encrypted_password = fernet.encrypt(password.encode())
            file.write(f"{site}|{login}|".encode() + encrypted_password + b"\n")


def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))


# ================== GUI ==================
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Manager")
        self.setFixedSize(QSize(700, 500))

        load_passwords()

        # -------- Widgets --------
        self.site_input = QLineEdit()
        self.site_input.setPlaceholderText("Site")

        self.login_input = QLineEdit()
        self.login_input.setPlaceholderText("Login")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")

        self.output = QTextEdit()
        self.output.setReadOnly(True)

        self.add_btn = QPushButton("Add password")
        self.gen_btn = QPushButton("Generate password")
        self.show_btn = QPushButton("Show all")
        self.search_btn = QPushButton("Search")
        self.edit_btn = QPushButton("Edit")
        self.delete_btn = QPushButton("Delete")

        # -------- Layouts --------
        main_layout = QVBoxLayout()
        inputs_layout = QHBoxLayout()
        buttons_layout = QHBoxLayout()

        inputs_layout.addWidget(self.site_input)
        inputs_layout.addWidget(self.login_input)
        inputs_layout.addWidget(self.password_input)

        buttons_layout.addWidget(self.add_btn)
        buttons_layout.addWidget(self.gen_btn)
        buttons_layout.addWidget(self.show_btn)
        buttons_layout.addWidget(self.search_btn)
        buttons_layout.addWidget(self.edit_btn)
        buttons_layout.addWidget(self.delete_btn)

        main_layout.addLayout(inputs_layout)
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self.output)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # -------- Signals --------
        self.add_btn.clicked.connect(self.add_password)
        self.gen_btn.clicked.connect(self.generate_and_fill)
        self.show_btn.clicked.connect(self.show_passwords)
        self.search_btn.clicked.connect(self.search_password)
        self.edit_btn.clicked.connect(self.edit_password)
        self.delete_btn.clicked.connect(self.delete_password)

    # ================== METHODS ==================
    def add_password(self):
        site = self.site_input.text().strip().lower()
        login = self.login_input.text().strip()
        password = self.password_input.text().strip()

        if not site or not login or not password:
            QMessageBox.warning(self, "Error", "Fill all fields!")
            return

        passwords[site] = [login, password]
        save_passwords()
        self.output.setText(f"Password for '{site}' added.")
        self.clear_inputs()

    def generate_and_fill(self):
        password = generate_password()
        self.password_input.setText(password)

    def show_passwords(self):
        self.output.clear()
        if not passwords:
            self.output.setText("Nothing to show.")
            return

        for site, (login, password) in passwords.items():
            self.output.append(f"Site: {site}")
            self.output.append(f"Login: {login}")
            self.output.append(f"Password: {password}")
            self.output.append("-" * 30)

    def search_password(self):
        keyword = self.site_input.text().strip().lower()
        self.output.clear()

        if not keyword:
            QMessageBox.warning(self, "Error", "Enter site or part of it!")
            return

        found = False
        for site, (login, password) in passwords.items():
            if keyword in site:
                self.output.append(f"Site: {site}")
                self.output.append(f"Login: {login}")
                self.output.append(f"Password: {password}")
                self.output.append("-" * 30)
                found = True

        if not found:
            self.output.setText("Nothing found.")

    def edit_password(self):
        site = self.site_input.text().strip().lower()
        login = self.login_input.text().strip()
        password = self.password_input.text().strip()

        if site not in passwords:
            QMessageBox.warning(self, "Error", "Site not found!")
            return

        if not login and not password:
            QMessageBox.warning(self, "Error", "Enter new login or password!")
            return

        old_login, old_password = passwords[site]

        if login:
            old_login = login
        if password:
            old_password = password

        passwords[site] = [old_login, old_password]
        save_passwords()
        self.output.setText(f"Password for '{site}' updated.")
        self.clear_inputs()

    def delete_password(self):
        site = self.site_input.text().strip().lower()

        if site not in passwords:
            QMessageBox.warning(self, "Error", "Site not found!")
            return

        del passwords[site]
        save_passwords()
        self.output.setText(f"Password for '{site}' deleted.")
        self.clear_inputs()

    def clear_inputs(self):
        self.site_input.clear()
        self.login_input.clear()
        self.password_input.clear()


# ================== RUN ==================
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
