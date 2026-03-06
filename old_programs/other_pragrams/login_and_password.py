import time

correct_login="prophet"
correct_password="3751"
attempts=3
def log_in():
    if login!=correct_login:
        print("Неправильный логин")
    else:
        print("Неправильный пароль")
        

while attempts > 0:
    time.sleep(2)
    try:
        login=input("Введите логин: ")
        password=int(input("Введите пароль: "))
        if login==correct_login and password==correct_password:
            print("Вход разрешен")
            break
        else:
            attempts-=1
            log_in()
            print("Попыток осталось: ", attempts)
        if attempts==0:
            print("Ваш банковский счет заблокирован =P")
    except ValueError:
        print("Ошибка: введите числа в поле для пароля")