score = int(input("Введите количество баллов (0–100): "))

if score < 0 or score > 100:
    print("Ошибка ввода")
elif score >= 90:
    print("Оценка: 5")
elif score >= 75:
    print("Оценка: 4")
elif score >= 60:
    print("Оценка: 3")
else:
    print("Оценка: 2")
