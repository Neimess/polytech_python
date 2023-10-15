money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
mounth = 0
while True:
    if mounth == 0:
        money_capital = money_capital + salary - spend
        mounth += 1
    else:
        spend = spend * (1+increase)
        money_capital = money_capital + salary - spend
        if money_capital < 0:
            break
        mounth += 1
print("Количество месяцев, которое можно протянуть без долгов:", mounth)
