months = {
    "январь": 1,
    "февраль": 2,
    "март": 3,
    "апрель": 4,
    "май": 5,
    "июнь": 6,
    "июль": 7,
    "август": 8,
    "сентябрь": 9,
    "октябрь": 10,
    "ноябрь": 11,
    "декабрь": 12
}
month_input = input("Введите месяц (например, январь): ").lower()
day = int(input("Введите день (число от 1 до 31): "))
if month_input not in months:
    print("Неверный месяц. Пожалуйста, введите корректное название месяца.")
else:
    month = months[month_input]
    if (month == 3 and day >= 20) or (month in [4, 5]) or (month == 6 and day < 21):
        season = "Весна"
    elif (month == 6 and day >= 21) or (month in [7, 8]) or (month == 9 and day < 22):
        season = "Лето"
    elif (month == 9 and day >= 22) or (month in [10, 11]) or (month == 12 and day < 21):
        season = "Осень"
    else:
        season = "Зима"
print(f"{day} {month_input} относится к сезону: {season}.")
