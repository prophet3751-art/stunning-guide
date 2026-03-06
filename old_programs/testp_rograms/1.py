goods=["яблоки","помидоры", "ананас"]
for list in goods:

    while True:
        n="Виберите действие: ", "1. Добавить товар", "2. Показать список", "3. Удалить товар", "Выйти"
        for user_list in n:
            print(user_list)
        i=input()
        if i =="1":
            string="Введите название товара: "
            print(string)
            goods.append(input())
            print(goods)
        elif i =="2":
            print(goods)
        elif i =="3":
            del_el=input("Введите товар который нужно удалить: ")
            goods.remove(del_el)