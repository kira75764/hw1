number = int(input("Введите число от 1 до 10: "))

if number < 1 or number > 10:
    print("Ошибка ввода")
else:
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)