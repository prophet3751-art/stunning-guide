import os

goods=[]

if os.path.exists("goods.txt"):
    with open("goods.txt", "r", encoding="utf-8") as file:
        goods.sort=[line.strip() for line in file]
while True:
    print("\nТекущий список товаров: ")
    if goods:
        for i, item in enumerate(goods, 1):
            print(f"{i}.{item}")
    else:
        print("список пуст.")

    new_item = input("Введите название товара (или 'end' для выхода): ").strip()
    if new_item.lower() == "end":
        print("До свидания!")
        break  # Выход из цикла
    elif new_item=="":
        print("Введите название товара!")
    else:
        goods.append(new_item)
        with open("goods.txt", "w", encoding="utf-8") as file:
            for item in goods:
                file.write(item + "\n")