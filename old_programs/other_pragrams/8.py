import os

goods=[]

if os.path.exists("app.txt"):
    with open("app.txt", "r", encoding="utf-8") as file:
        goods=[line.strip() for line in file]
def save_file():
    with open("app.txt", "w", encoding="utf-8") as file:
        for item in goods:
            file.write(item+"\n")        

while True:
    print("\nТекущий список товаров: ")
    if goods:
        for i, item in enumerate(goods, 1):
            print(f"{i}.{item}")
    else:
        print("список пуст.")
    print("1 - Add items")
    print("2 - sort items")
    print("3 - Exit")
    print("4 - Remove item")
    choise=input("Enter choise: ")

    try:
        if choise=="3":
            print("Good luck, my friend!")
            save_file()
            print("File saved")    
            break
        elif choise=="1":
            i=input("Enter goods: ")
            goods.append(i)
            save_file()
            print("Item added \nFile saved.")    
        elif choise=="2":
            goods.sort()
            save_file()
            print("File saved")    
        elif choise=="4":
            g=input("Remove: ")
            goods.remove(g)
            save_file()
            print("File saved")    
        else:
            print("Error")
    except ValueError:
        print("Error2")