def calculator():
    while True:
        a = input("Введите первое число (или 'нет' для выхода): ")
        if a.lower() == "нет":
            print("До встречи!")
            break
        b = input("Введите второе число: ")
        operation = input("Выберите операцию (+, -, *, /, **): ")

        try:
            a = float(a)
            b = float(b)

            if operation == "+":
                result = a + b
            elif operation == "-":
                result = a - b
            elif operation == "*":
                result = a * b
            elif operation == "/":
                if b != 0:
                    result = a / b
                else:
                    print("Ошибка: деление на ноль!")
                    continue
            elif operation == "**":
                result = a ** b
            else:
                print("Неизвестная операция.")
                continue

            print("Результат:", result)
        except ValueError:
            print("Ошибка: нужно вводить числа.")
