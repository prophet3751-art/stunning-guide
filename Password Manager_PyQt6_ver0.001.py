import os
import random
import string 
import sys 
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, 
    QPushButton, QTextEdit, QHBoxLayout, QComboBox, QLabel
)
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont

from cryptography.fernet import Fernet as fr
# ==================================================================
with open("key.key", "rb") as f:
    key = f.read()
fernet = fr(key)

from translations import translations
passwords = {}
# ====================================================================
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password
# ====================================================================
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
# ====================================================================
def save_passwords():
    with open("passwords.txt", "wb") as file:  # пишем байты
        for site, (login, password) in passwords.items():
            encrypted_password = fernet.encrypt(password.encode())
            file.write(f"{site}|{login}|".encode() + encrypted_password + b"\n")
# ====================================================================
font = QFont("Arial", 15)
 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.current_language = "en"
        

        load_passwords()

        
        self.setFixedSize(QSize(900,500))
#                       Виджеты:
# создаем выпадающий список:
        self.site_combo = QComboBox()
        self.lable = QLabel("")

        self.select_lang = QComboBox()
        self.select_lang.addItem("English", "en")
        self.select_lang.addItem("Русский", "ru")
        self.select_lang.addItem("Украiнська", "ua")
        self.lable_lang = QLabel()
# Поле ввода сайта:
        self.site_input = QLineEdit()
        self.site_input.setStyleSheet("color: lightblue")
# Поле ввода логина:
        self.login_input = QLineEdit()
        self.login_input.setStyleSheet("color: lightblue")
# Поле ввода пароля:
        self.password_input = QLineEdit()
        self.password_input.setStyleSheet("color: lightblue")
# Поле вывода информации:
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setFont(font)
        self.output.setFontItalic(True)
        self.output.setStyleSheet("color: deepskyblue")
        
# кнопки:
        self.add_btn = QPushButton()
        self.show_btn = QPushButton()
        self.gen_btn = QPushButton()
        self.del_site = QPushButton()
        self.searching = QPushButton()
        self.copy_btn = QPushButton()

# Layout:
        main_layout = QVBoxLayout() # По вертикали
        buttons_layout = QHBoxLayout() #по горизонтали
        inputs_layout = QHBoxLayout() #по горизонтали
# Добавляем поля ввода:
        inputs_layout.addWidget(self.site_input)
        inputs_layout.addWidget(self.login_input)
        inputs_layout.addWidget(self.password_input)
# Добавляем кнопки:
        buttons_layout.addWidget(self.add_btn)
        buttons_layout.addWidget(self.show_btn)
        buttons_layout.addWidget(self.gen_btn)
        buttons_layout.addWidget(self.del_site)
        buttons_layout.addWidget(self.searching)
        buttons_layout.addWidget(self.copy_btn)

        main_layout.addLayout(inputs_layout)
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self.output)
# Выпадающий список:
        main_layout.addWidget(self.lable)
        main_layout.addWidget(self.site_combo)

        inputs_layout.addWidget(self.lable_lang)
        inputs_layout.addWidget(self.select_lang)
        
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
# сигналы 
        self.add_btn.clicked.connect(self.add_password)
        self.show_btn.clicked.connect(self.show_passwords)
        self.gen_btn.clicked.connect(self.generate_and_fill)
        self.del_site.clicked.connect(self.delete_password)
        self.searching.clicked.connect(self.search_password)
        self.copy_btn.clicked.connect(self.copy_password)
# Сигналы для выпалающего списка:
        self.site_combo.currentTextChanged.connect(self.on_site_selected)

        self.select_lang.currentIndexChanged.connect(self.change_language)

        self.site_update()
        self.update_text()
# Методы:
    def change_language(self):
        self.current_language = self.select_lang.currentData()
        self.update_text()
# ____________________________________________________________
    def update_text(self):
    # Для кнопок:
        self.setWindowTitle(translations[self.current_language]["title"])

        self.add_btn.setText(translations[self.current_language]["add_btn"])
        self.show_btn.setText(translations[self.current_language]["show_btn"])
        self.searching.setText(translations[self.current_language]["search_btn"])
        self.gen_btn.setText(translations[self.current_language]["gen_btn"])
        self.del_site.setText(translations[self.current_language]["del_btn"])
        self.copy_btn.setText(translations[self.current_language]["copy_btn"])
    #  Для полей:
        self.site_input.setPlaceholderText(translations[self.current_language]["site_input_placeholder"])
        self.login_input.setPlaceholderText(translations[self.current_language]["login_input_placeholder"])
        self.password_input.setPlaceholderText(translations[self.current_language]["password_input_placeholder"])
    # Лейблы:
        self.lable_lang.setText(translations[self.current_language]["lable_lang"])
        self.lable.setText(translations[self.current_language]["chose_site_lable"])
# ____________________________________________________________
    def site_update(self):
        self.site_combo.blockSignals(True)
        self.site_combo.clear()
        self.site_combo.addItem("Select site")
        for site in passwords:
            self.site_combo.addItem(site)
            self.site_combo.blockSignals(False)
# ____________________________________________________________
    def on_site_selected(self, site):
        if site == "Select site":
            self.clear_inputs() 
            self.output.clear()
            return
        
        login, password = passwords.get(site, ("", ""))
        self.output.setText(f"{login}: {password}")
        self.login_input.setText(login)
        self.password_input.setText(password)
        self.site_input.setText(site)
# ____________________________________________________________
    def copy_password(self):
        site = self.site_input.text().strip().lower()


        if not site:
            self.output.setText("Enter site first")
            return
        
        if site not in passwords:
            self.output.setText("Site not found")
            return
        password = passwords[site][1]
        QApplication.clipboard().setText(password)
        self.output.setText("Password copied to clipboard.")
# ____________________________________________________________

    def search_password(self):
        keyword = self.site_input.text().strip().lower()
        self.output.clear()

        if not keyword:
            self.output.setText("Enter site")
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
            self.output.setText("Nothing found")
# ____________________________________________________________
    def delete_password(self):
        site = self.site_input.text().strip().lower()

        if site not in passwords:
            self.output.setText("Nothing found")
            return
        del passwords[site]
        save_passwords()
        self.output.setText(f"Password and Site {site} deleted")
        
        self.clear_inputs()
        self.site_update()

    def clear_inputs(self):
        self.site_input.clear()
        self.login_input.clear()
        self.password_input.clear()

# ____________________________________________________________
    def generate_and_fill(self):
        password = generate_password()
        self.password_input.setText(password)
# ____________________________________________________________
    def add_password(self):
        site = self.site_input.text().strip().lower()
        login = self.login_input.text().strip()
        password = self.password_input.text().strip()

        if not site or not login or not password:
            self.output.setText("Please fill all fields.")
            return
    
        passwords[site] = [login, password]
        save_passwords()
        self.output.setText(f"Password for {site} added.")


        self.clear_inputs()
        self.site_update()
# ____________________________________________________________
    def show_passwords(self):
        self.clear_inputs()
        self.output.clear()

        if not passwords:
            self.output.setText("Nothing to show")
            return
        
        for site, (login, password) in passwords.items():
            self.output.append(f"Site:  {site}\n")
            self.output.append(f"Login:  {login}\n")
            self.output.append(f"Password:  {password}")
            self.output.append("-" * 30)
# _________________________________________________________________
# =========================================================================
app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())