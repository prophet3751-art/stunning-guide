print("=" * 30)
print("=" * 30)
goods=["яблоки","помидоры", "ананас"]
while True:
    n ="Виберите действие: ", "1. Добавить товар", "2. Показать список", "3. Удалить товар", "4. Выйти"
    for user_list in n:
        print(user_list)
    i=input()
    if i == "4":
        print("Всего хорошего!")
        break
    try:
        if i =="1":
            string="Введите название товара: "
            goods.append(input(string))
            print("Cписок товаров:", goods)
        elif i =="2":
            print("Cписок товаров:", goods)
        elif i =="3":
            del_el=input("Введите товар который нужно удалить: ")
            goods.remove(del_el)
            print("Cписок товаров: ", goods)
        else:
            print("Введите правельные числа действия!")
    except ValueError:
        print("Введите пральные числа")
