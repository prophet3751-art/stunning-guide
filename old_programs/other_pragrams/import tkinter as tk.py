import tkinter as tk
from tkinter import messagebox, simpledialog
import os

tasks = []

FILENAME = "todo.txt"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) == 2:
                    tasks.append((parts[0], parts[1]))

def save_tasks():
    with open(FILENAME, "w", encoding="utf-8") as file:
        for task, deadline in tasks:
            file.write(f"{task} | {deadline}\n")

def update_listbox():
    listbox.delete(0, tk.END)
    for i, (task, deadline) in enumerate(tasks, 1):
        listbox.insert(tk.END, f"{i}. {task} (до {deadline})")

def add_task():
    task = simpledialog.askstring("Добавить дело", "Введите новое дело:")
    if task:
        deadline = simpledialog.askstring("Добавить дедлайн", "Введите дедлайн (например, 2025-07-10):")
        if deadline:
            tasks.append((task, deadline))
            update_listbox()
            save_tasks()
        else:
            messagebox.showwarning("Внимание", "Дедлайн не введён.")
    else:
        messagebox.showwarning("Внимание", "Дело не введено.")

def delete_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Внимание", "Выберите дело для удаления.")
        return
    index = selected[0]
    removed = tasks.pop(index)
    update_listbox()
    save_tasks()
    messagebox.showinfo("Удалено", f"Удалено дело: {removed[0]}")

def on_exit():
    save_tasks()
    root.destroy()

# Создаём главное окно
root = tk.Tk()
root.title("Список дел")

# Список дел
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(padx=10, pady=10)

# Кнопки
frame = tk.Frame(root)
frame.pack(pady=5)

btn_add = tk.Button(frame, text="Добавить дело", command=add_task)
btn_add.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(frame, text="Удалить дело", command=delete_task)
btn_delete.pack(side=tk.LEFT, padx=5)

btn_exit = tk.Button(frame, text="Выход", command=on_exit)
btn_exit.pack(side=tk.LEFT, padx=5)

# Загружаем задачи и показываем
load_tasks()
update_listbox()

# Запускаем главный цикл
root.mainloop()
