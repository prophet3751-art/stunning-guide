
def calculator():
    a = float(input("Введите певое число: "))
    b = float(input("Введите второе число: "))
    operation = input("Выберите операцию: (+, -, *, /): ")
    
    if operation == "+":
        result = a+b
        return result
    elif operation == "-":
        result = a-b
        return result
    elif operation == "*":
        result = a*b
        return result
    elif operation == "/":
        if b == 0:
            result = "Ошибка: деление на 0!"
            return result
        else:
            result = a/b
            return result
    else:
        return "неизвестная операция"
result = calculator()
print("Результат: "+ str(result))