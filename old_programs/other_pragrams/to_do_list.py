import os

# Загружаем дела из файла, если он есть
tasks = []
if os.path.exists("todo.txt"):
    with open("todo.txt", "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(" | ")
            if len(parts)==2:
                tasks.append((parts[0].strip(), parts[1].strip()))

def show_tasks():
    if not tasks:
        print("Список дел пуст.")
    else:
        print("\nВаши дела:")
        for i,(task, deadline) in enumerate(tasks, 1):
            print(f"{i}. {task} (до {deadline})")
    print("=" * 30)

def add_task():
    task = input("Введите новое дело: ")
    deadline =input("Введите дедлайн (например, 2025-07-10): ")
    tasks.append((task, deadline))
    print("Дело с дедлайном добавлено.")

def delete_task():
    show_tasks()
    try:
        num = int(input("Введите номер дела для удаления: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Удалено: {removed[0]}")
        else:
            print("Неверный номер.")
    except ValueError:
        print("Введите число.")

def save_tasks():
    with open("todo.txt", "w", encoding="utf-8") as file:
        for task, deadline in tasks:
            file.write(f"{task} | {deadline}\n")

    

# Главный цикл программы
while True:
    print("\nМеню:")
    print("1 - Показать дела")
    print("2 - Добавить дело")
    print("3 - Удалить дело")
    print("4 - Выйти")
    choice = input("Выберите действие: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
        save_tasks()
    elif choice == "3":
        delete_task()
        save_tasks()
    elif choice == "4":
        save_tasks()
        print("Пока! Все дела сохранены.")
        break
    else:
        print("Неверный выбор. Попробуй снова.")
