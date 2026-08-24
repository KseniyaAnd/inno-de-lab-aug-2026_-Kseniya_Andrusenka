first_num = float(input("Введите первое число: "))
second_num = float(input("Введите второе число: "))
operation = input("Выберите оператор (+, -, *, /): ")

if operation == "+":
    result = first_num + second_num
elif operation == "-":
    result = first_num - second_num
elif operation == "*":
    result = first_num * second_num
elif operation == "/":
    if second_num != 0:
        result = first_num / second_num
    else:
        result = "Ошибка: Деление на ноль!"
else:
    result = "Ошибка: Неверный оператор!"

print(f"Результат: {first_num} {operation} {second_num} = {result}")

