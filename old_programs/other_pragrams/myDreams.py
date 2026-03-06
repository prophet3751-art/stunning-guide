import os
import time as t

have_to=[]

if os.path.exists("have_to_list.txt"):
    with open("have_to_list.txt", "r", encoding="utf-8") as file:
        have_to=[line.strip() for line in file]

def save_file():
    with open("have_to_list.txt", "w", encoding="utf-8") as file:
        for item in have_to:
            file.write(item+ "\n")

def show_me():
    if not have_to:
        print("Nothing in your notice")
    else:
        print("Your deals: ")
        for num, deals in enumerate(have_to, 1):
            print(f"{num}. {deals}")

def add_somthing():
    add_task=input("Enter your task: ")
    have_to.append(add_task)
    print("Task added")

def delete_something():
    try:
        remove_num=int(input("Enter number of task: "))
        have_to.pop(remove_num-1)
    except IndexError:
        print("Again")

def clear_all():
    ask=input("Are you shure? Y/N")
    if ask.lower()=="y":
        have_to.clear()
        save_file()
    else:
        print("ok")

while True:
    show_me()
    t.sleep(2)
    print("Choise operation: ")
    t.sleep(1)
    print("1. Add the task")
    t.sleep(1)
    print("2. Remove the task")
    t.sleep(1)
    print("3. clear all")
    t.sleep(1)
    print("4. Exit")

    choice=input("Your choise: ")
    try:
        if choice=="4":
            print("Goodbay, my friend!")
            save_file()
            break
        elif choice=="1":
            add_somthing()
            save_file()
        elif choice=="2":
            delete_something()
            save_file()
        elif choice=="3":
            clear_all()
    except ValueError:
        print("Error 404=)")
