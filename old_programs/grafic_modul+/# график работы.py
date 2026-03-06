import os
import time as t
from datetime import datetime, timedelta

shifts=["6:00-14:00", "14:00-22:00", "22:00-6:00", "Day off"]

work_schedule={}

def read_grafic():
    if os.path.exists("grafic.txt"):
        with open("grafic.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts= line.strip().split("|")
                date= parts[0].strip()
                shift= parts[1].strip()
                work_schedule[date] = shift

def save_schedule(schedule, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for date, shift in schedule.items():
            file.write(f"{date} | {shift}\n")
        print(f"\n Grafic was saved in file '{filename}'")

# def save_grafic():
#     with open("grafic.txt", "w", encoding="utf-8") as file:
#         for date, shift in work_schedule.items():
#            file.write(f"{date} | {shift}\n") 

def ask_something(prompt):
    while True:
        user_input= input(prompt).strip()
        if user_input:
            return user_input
        else:
            print("Enter something!")

def generate_dates():
    start_date_str = ask_something("Введи стартовую дату (дд-мм-гггг): ")
    num_days_str = ask_something("Сколько дней вперёд запланировать?: ")

    # Преобразуем ввод
    start_date = datetime.strptime(start_date_str, "%d-%m-%Y")
    num_days = int(num_days_str)

    dates = []
    for i in range(num_days):
        day = start_date + timedelta(days=i)
        dates.append(day.strftime("%d-%m-%Y"))
    return dates

def assign_shifts(dates, shifts):
    for date in dates:
        print(f"\nChoose the shift for {date}:")
        for i, shift in enumerate(shifts, start=1):
            print(f"{i}: {shift}")

        while True:
            choice = input("Enter number of shift: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(shifts):
                work_schedule[date] = shifts[int(choice) - 1]
                break
            else:
                print("Number is not correct. Try again.")


def show_grafic():
    if not work_schedule:
        print("Your grafic: ")
        read_grafic()
    if work_schedule:
        for date, shift in work_schedule.items():
            print(f"{date} | {shift}")
    else:
        print("none")

def add_shift():
    while True:
        add_date = input("Enter Date (Example: 23-07-2025): ").strip()
        if not add_date:
            print("Введите дату!")
            continue

        print("Chose Date")
        for i, shift in enumerate(shifts, start=1):
            print(f"{i}: {shift}")

        choice = input("Number of shift (1-4): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(shifts):
            work_schedule[add_date] = shifts[int(choice) - 1]
            print("Shift added.")
            break
        else:
            print("Enter something")

               
def remove_shift():
    del_shift=input("Enter date to remove: ")
    if del_shift in work_schedule:
        del work_schedule[del_shift]
        print("Shift was removed.")
    else:
        print("This date is not correct")

while True:
    show_grafic()
    t.sleep(2)
    print("\nChoise the number: \n")
    t.sleep(1)
    print("1. Added shift.")
    t.sleep(1)
    print("2. Remove shift.")
    t.sleep(1)
    print("3. Exit")
    t.sleep(1)
    print("4. Auto-generate schedule with shifts")
    user=input("Number please: ")

    if user=="3":
        save_schedule(work_schedule, "grafic.txt")
        print("Good luck!")
        break
    elif user=="1":
        add_shift()
        save_schedule(work_schedule, "grafic.txt")
    elif user=="2":
        remove_shift()
        save_schedule(work_schedule, "grafic.txt")
    elif user=="4":
        dates= generate_dates()
        assign_shifts(dates, shifts)
        save_schedule(work_schedule, "grafic.txt")
    

    
    
