import os  # Модуль os нужен, чтобы проверять — существует ли файл

goods = []  # Здесь будет храниться список товаров

# Если файл с товарами уже существует — загружаем список из него
if os.path.exists("goods.txt"):
    with open("goods.txt", "r", encoding="utf-8") as file:
        goods = [line.strip() for line in file]  # Считываем построчно и убираем \n

# Основной цикл программы
while True:
    print("\nВыберите действие:")
    print("1. Добавить товар")
    print("2. Показать список")
    print("3. Удалить товар")
    print("4. Выйти")

    i = input("Ваш выбор: ")

    if i == "4":
        # Сохраняем список в файл перед выходом
        with open("goods.txt", "w", encoding="utf-8") as file:
            for item in goods:
                file.write(item + "\n")  # Каждую строку с новой строки
        print("Список сохранён. Всего хорошего!")
        break  # Выход из программы

    try:
        if i == "1":
            item = input("Введите название товара: ")
            goods.append(item)  # Добавляем товар в список
            print("Товар добавлен.")

        elif i == "2":
            print("Список товаров:")
            for g in goods:
                print("-", g)  # Выводим каждый товар с тире

        elif i == "3":
            del_el = input("Введите товар, который нужно удалить: ")
            goods.remove(del_el)  # Удаляем товар
            print("Товар удалён.")

        else:
            print("Введите правильный номер действия!")

    except ValueError:
        print("Ошибка! Возможно, товара нет в списке или вы ввели не то.")
