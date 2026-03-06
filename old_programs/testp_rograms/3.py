import os
import time as t

goods_list = []

# Загружаем из файла
if os.path.exists("goods_list.txt"):
    with open("goods_list.txt", "r", encoding="utf-8") as file:
        goods_list = [line.strip() for line in file]

# Сохранить список
def save_wish_list():
    with open("goods_list.txt", "w", encoding="utf-8") as file:
        for item in goods_list:
            file.write(item + "\n")

# Удалить один товар
def remove_item():
    item_remove = input("Enter item to remove: ")
    if item_remove in goods_list:
        goods_list.remove(item_remove)
        print("Item is removed.")
    else:
        print("Item not found in the list.")

# Показать список
def show_goods():
    if not goods_list:
        print("Your wish list is empty.")
    else:
        print("Your wish list:")
        for номер, товар in enumerate(goods_list, 1):
            print(f"{номер}. {товар}")

# Главный цикл
while True:
    show_goods()
    t.sleep(1)
    print("What do you want to buy?")
    t.sleep(1)
    print("Enter your wishes or 'stop' to end the program.")
    print("Enter 'clear' to clear all, or 'remove' to delete one item.")
    t.sleep(1)
    
    n = input("Your input: ").strip().lower()

    if n == "stop":
        print("Have a nice day, bro!")
        save_wish_list()
        break
    elif n == "clear":
        goods_list.clear()
        save_wish_list()
        print("List is cleared.")
    elif n == "remove":
        remove_item()
        save_wish_list()
    else:
        goods_list.append(n)
        print("Item added to your wish list.")
        save_wish_list()








# import os
# import time as t
# goods_list=[]

# if os.path.exists("goods_list.txt"):
#     with open("goods_list.txt", "r", encoding="utf-8") as file:
#         goods_list=[line.strip() for line in file]

# def save_wish_list():
#     with open("goods_list.txt", "w", encoding="utf-8") as file:
#         for item in goods_list:
#             file.write(item + "\n")
# def remove_item():
#     item_remove = input("Enter item to remove: ")
#     if item_remove in goods_list:
#         goods_list.remove(item_remove)
#         print("Item is removed.")
#     else:
#         print("Item not found in the list.")
# def show_goods():
#     if not goods_list:
#         print("Your wish list is empty.")
#     else:
#         print("Your wish list: ")
#         for list, numer in enumerate(goods_list, 1):
#             print(f"{list}. {numer}")

# while True:
#     show_goods()
#     t.sleep(2)
#     print("What you want to buy?")
#     t.sleep(2)
#     print("Enter your wishes or 'stop' if you want to end this program: ")
#     t.sleep(2)
#     n=input("Enter 'clear' if you want to clear all.")
    
#     if n=="stop":
#         print("Have a nice day? bro!")
#         save_wish_list()
#         break
#     elif n=="clear":
#         goods_list.clear()
#         save_wish_list()
#     elif n=="remove":
#         try:
#             remove_item()
#             save_wish_list()
#         except ValueError:
#             print("Your wish list already cleaned.")
#     else:
#         goods_list.append(n)
#         print("Your wishes is added.")
#         save_wish_list()
#         show_goods()
    