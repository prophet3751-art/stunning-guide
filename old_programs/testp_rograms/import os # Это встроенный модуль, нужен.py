import os #   Это встроенный модуль, нужен чтобы проверить, существует ли файл. Без него программа может упасть, если файла ещё нет.
goods = []    
if os.path.exists("goods.txt"): #если файл "goods.txt" существует:
    with open("goods.txt", "r", encoding="utf-8") as file: #Открывает файл (r — чтение, w — запись) и автоматически закрывает
        goods = [line.strip() for line in file]

while True:
    print("\nВыберите действие:")
    print("1. Добавить товар")
    print("2. Показать список")
    print("3. Удалить товар")
    print("4. Выйти")
   
    i = input("Ваш выбор: ")
    
    if i == "4":
        with open("goods.txt", "w", encoding="utf-8") as file:
            for item in goods:
                file.write(item + "\n")
        print("Список сохранен. Всего хорогего!")
        break

    try:
        if i == "1":
            item = input("Введите название товара: ")
            goods.append(item)
            print("Товар добавлен.")
        elif i == "2":
            print("Список товаров:")
            for g in goods:
                print("-", g)
        elif i == "3":
            del_el = input("Введите товар, который нужно удалить: ")
            goods.remove(del_el)
            print("Товар удалён.")
        else:
            print("Введите правильный номер действия!")
    except ValueError:
        print("Ошибка! Возможно, товара нет в списке или вы ввели не то.")         