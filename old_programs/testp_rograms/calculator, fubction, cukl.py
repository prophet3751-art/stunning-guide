print("=" * 30)
def calculator():
    while True:
            a = input("Введите первое число (или 'нет' для выхода): ")
            if a.lower() == "нет":
                print("Досвидания")
                break
            b = float(input("Введите второе число: ")) 
            operation = input("Выберите операцию: (+, -, *, /,**): ")
            try:
                a = float(a)
                b = float(b)  
                if operation == "+":
                    result = a+b
                elif operation == "-":
                    result = a-b
                elif operation == "*":
                    result = a*b
                elif operation == "/":
                    if b == 0:
                        result = "Ошибка: деление на 0!"
                        continue
                    result = a/b
                elif operation == "**":
                    result = a**b
                else:
                    print("неизвестная операция")
                    continue
                print("Результат: ", result)
            except ValueError:
                print("Ошибка: нужно вводить числа")
calculator()
print("    Простой калькулятор")
print("=" * 30)
